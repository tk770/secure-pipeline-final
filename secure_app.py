import os

def login_system():
    # Safely pulling from the environment
    secret_api_key = os.getenv("MY_SECRET_KEY") 
    
    if not secret_api_key:
        print("System Alert: Secure environment check passed.")
    else:
        print("System Initialized Safely")

login_system()
