import time
from collections import defaultdict

LOG_FILE = "auth.log"
THRESHOLD = 5  # Block IP if failed attempts exceed this limit
BLOCKED_IPS = set()
failed_attempts = defaultdict(int)

def block_ip(ip):
    """Simulates automated incident response (SOAR) by blocking the IP."""
    if ip not in BLOCKED_IPS:
        BLOCKED_IPS.add(ip)
        print(f"\n [ALERT] Brute-force attack detected from IP: {ip}")
        print(f" [AUTOMATED RESPONSE] Executing firewall rule: iptables -A INPUT -s {ip} -j DROP")
        print(f" [STATUS] IP {ip} has been automatically ISOLATED and BLOCKED!\n")

def monitor_logs():
    print(" [SIEM] Threat Detection Engine running. Monitoring auth.log...\n")
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Failed password" in line:
                    parts = line.split()
                    # Extract IP address from log format: "Failed password for <user> from <IP> ..."
                    ip_index = parts.index("from") + 1
                    ip = parts[ip_index]
                    
                    failed_attempts[ip] += 1
                    print(f" [MONITOR] Failed login detected from {ip} (Count: {failed_attempts[ip]})")
                    
                    if failed_attempts[ip] >= THRESHOLD:
                        block_ip(ip)
    except FileNotFoundError:
        print(f"Error: {LOG_FILE} not found. Run simulator.py first!")

if __name__ == "__main__":
    monitor_logs()
