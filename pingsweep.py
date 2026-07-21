import subprocess
import time

print("--- STARTING NETWORK PING SWEEPER ---")
start_time = time.time()

base_ip = "127.0.0."

for host in range(1, 6):
    target_ip = base_ip + str(host)
    response = subprocess.run(["ping", "-c", "1", "-W", "1", target_ip], 
                              stdout=subprocess.DEVNULL, 
                              stderr=subprocess.DEVNULL)
    
    if response.returncode == 0:
        print(f"[+] DEVICE ONLINE: {target_ip}")
    else:
        print(f"[-] Device Offline: {target_ip}")

end_time = time.time()
print(f"Sweep completed in {end_time - start_time:.2f} seconds.")
