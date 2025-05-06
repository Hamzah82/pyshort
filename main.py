import pyshorteners
from pyshorteners.exceptions import ShorteningErrorException
import os
import json

CRED_FILE = "cred.txt"

def load_bitly_credential():
    """Load Bit.ly credential from file if exists"""
    if os.path.exists(CRED_FILE):
        with open(CRED_FILE, 'r') as f:
            try:
                return json.load(f).get('bitly_api_key')
            except json.JSONDecodeError:
                return None
    return None

def save_bitly_credential(api_key):
    """Save Bit.ly credential to file"""
    with open(CRED_FILE, 'w') as f:
        json.dump({'bitly_api_key': api_key}, f)

def shorten_url(url, provider):
    """Function to shorten URL based on selected provider"""
    try:
        s = pyshorteners.Shortener()
        
        if provider == '1':  # Bit.ly
            bitly_api_key = load_bitly_credential()
            
            if not bitly_api_key:
                print("\nBit.ly requires an API key.")
                print("You can get a free API key at https://bit.ly")
                bitly_api_key = input("Enter your Bit.ly API key: ")
                save_bitly_credential(bitly_api_key)
                print("API key has been saved for future use")
            
            s = pyshorteners.Shortener(api_key=bitly_api_key)
            return s.bitly.short(url)
        
        elif provider == '2':  # TinyURL
            return s.tinyurl.short(url)
        
        elif provider == '3':  # Da.gd
            return s.dagd.short(url)
        
        else:
            return "Invalid provider selection"
    
    except ShorteningErrorException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("=== URL Shortener ===")
    print("Select URL shortening provider:")
    print("1. Bit.ly (requires API key)")
    print("2. TinyURL")
    print("3. Da.gd")
    
    provider = input("Enter your choice (1-3): ")
    long_url = input("Enter the URL to shorten: ")
    
    # URL validation
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'https://' + long_url
    
    short_url = shorten_url(long_url, provider)
    
    print("\nResult:")
    print(f"Original URL: {long_url}")
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
