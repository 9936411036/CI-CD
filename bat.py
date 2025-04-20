import os

def main():
    print("Hello from Drone CI 🎉")
    
    # Example: Read secret from environment
    secret = os.getenv("MY_PASS", "No secret found")
    print(f"Secret passed from Drone: {secret}")

if __name__ == "__main__":
    main()
