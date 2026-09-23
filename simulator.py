import time
import random

LOG_FILE = "auth.log"

ATTACKER_IPS = ["192.168.1.100", "10.0.0.55", "172.16.0.22"]
USERNAMES = ["root", "admin", "user", "ssh_user"]

print("Starting SSH Login Simulator... (Press Ctrl+C to stop)")

# Write simulated failed login attempts
with open(LOG_FILE, "a") as f:
    for i in range(15):
        ip = random.choice(ATTACKER_IPS)
        user = random.choice(USERNAMES)
        log_entry = f"Failed password for {user} from {ip} port 22 ssh2\n"
        f.write(log_entry)
        f.flush()
        print(f"[SIMULATOR] Generated log: {log_entry.strip()}")
        time.sleep(1)

print("Simulation finished. Check auth.log file.")
