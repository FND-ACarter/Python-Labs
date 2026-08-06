import socket
import time

print("--- SECURITY TOOL: AUTOMATED NETWORK IP & PORT SCANNER ---")
start_time = time.time()

# 1. Function to grab your network identities
def target_network_assets():
    # Extract the computer's name
    hostname = socket.gethostname()
    # Extract the live IP address linked to that name
    ip_address = socket.gethostbyname(hostname)
    
    print(f"\n[+] Virtual Machine Hostname: {hostname}")
    print(f"[+] Active Private IP Address: {ip_address}")
    return ip_address

# 2. Function to scan a specific port door
def scan_target_port(target_ip, port_number):
    print(f"\n[+] Initiating Scan on Port: {port_number} (SSH)...")
    
    # Set up a virtual probe (Socket connection)
    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe.settimeout(1.0) # Wait exactly 1 second for a response
    
    # Try to connect to the port door
    result = probe.connect_ex((target_ip, port_number))
    
    # 3. The Condition Gate (Checking response code)
    if result == 0:
        print(f"[!] ALERT: Port {port_number} is OPEN and listening!")
    else:
        print(f"[-] Secure: Port {port_number} is Closed/Filtered.")
        
    probe.close()

# 4. Execute the automated steps
my_ip = target_network_assets()
scan_target_port(my_ip, 22)

end_time = time.time()
print(f"\nScan completed in {end_time - start_time:.2f} seconds.")
