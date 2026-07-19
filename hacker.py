import time

# 1. Set the target password (4 letters)
secret_password = "drea"

print("--- STARTING BRUTE-FORCE SIMULATOR ---")
start_time = time.time()

# 2. Characters to try
characters = "abcdefghijklmnopqrstuvwxyz"
guess_count = 0

# 3. The updated 4-layer guessing loops
for char1 in characters:
    for char2 in characters:
        for char3 in characters:
            for char4 in characters:
                # This lines up all 4 letters to make the guess
                guess = char1 + char2 + char3 + char4
                guess_count += 1
                
                if guess == secret_password:
                    end_time = time.time()
                    total_time = end_time - start_time
                    print(f"SUCCESS! Cracked password: '{guess}'")
                    print(f"Total Guesses: {guess_count}")
                    print(f"Time Taken: {total_time:.4f} seconds")
                    exit()
