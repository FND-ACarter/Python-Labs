# 1. Define the automated blueprint
def check_user_profile(name, age, military_status):
    print(f"\n--- SCANNING PROFILE: {name} ---")
    print(f"Age: {age}")
    
    if military_status == True:
        print("ACCESS: Active Duty Shield Verified.")
    else:
        print("ACCESS: Standard Civilian Profile.")

# 2. Infinite reuse: Feeding different data into the blueprint
check_user_profile("Andre", 25, True)
check_user_profile("Sarah", 31, False)
check_user_profile("Marcus", 19, True)
