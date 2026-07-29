import hashlib
import time

print("--- SECURITY TOOL: CRYPTOGRAPHIC HASH GENERATOR ---")
start_time = time.time()

# 1. The Variable (Plaintext data)
secret_message = "NavyCyber2026"

# 2. Convert the plaintext string into byte format for processing
message_bytes = secret_message.encode()

# 3. Pass the bytes through the industry-standard SHA-256 Algorithm
sha256_hash = hashlib.sha256(message_bytes).hexdigest()

# 4. Output the transformation straight to your screen
print(f"\n[+] Original Plaintext: {secret_message}")
print(f"[+] Secure Cryptographic Hash: {sha256_hash}")

end_time = time.time()
print(f"\nTransformation executed in {end_time - start_time:.4f} seconds.")
