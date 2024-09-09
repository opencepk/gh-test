# scripts/wavelo-config-setting.py
import sys

def main(token):
    print("Hello, World!")
    # Perform a simple operation with the token
    print(f"Received token: {token[:5]}...")  # Print the first 5 characters of the token for demonstration

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wavelo-config-setting.py <token>")
        sys.exit(1)
    
    token = sys.argv[1]
    main(token)