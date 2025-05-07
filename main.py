import pyshorteners
from pyshorteners.exceptions import ShorteningErrorException
import os
import json
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

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
                print(f"\n{Fore.YELLOW}⚠️ Bit.ly requires an API key.{Style.RESET_ALL}")
                print(f"{Fore.CYAN}You can get a free API key at {Fore.BLUE}https://bit.ly{Style.RESET_ALL}")
                bitly_api_key = input(f"{Fore.GREEN}🔑 Enter your Bit.ly API key: {Style.RESET_ALL}")
                save_bitly_credential(bitly_api_key)
                print(f"{Fore.GREEN}✅ API key has been saved for future use{Style.RESET_ALL}")
            
            s = pyshorteners.Shortener(api_key=bitly_api_key)
            return s.bitly.short(url)
        
        elif provider == '2':  # TinyURL
            return s.tinyurl.short(url)
        
        elif provider == '3':  # Da.gd
            return s.dagd.short(url)
        
        else:
            return f"{Fore.RED}❌ Invalid provider selection{Style.RESET_ALL}"
    
    except ShorteningErrorException as e:
        return f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}❌ An error occurred: {str(e)}{Style.RESET_ALL}"

def print_banner():
    """Print PYSHORT ASCII art banner"""
    print(f"{Fore.MAGENTA}")
    print("██████╗ ██╗   ██╗███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗")
    print("██╔══██╗╚██╗ ██╔╝██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝")
    print("██████╔╝ ╚████╔╝ ███████╗███████║██║   ██║██████╔╝   ██║   ")
    print("██╔═══╝   ╚██╔╝  ╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ")
    print("██║        ██║   ███████║██║  ██║╚██████╔╝██║  ██║   ██║   ")
    print("╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.CYAN}✂️ {Fore.YELLOW}URL Shortener Tool {Fore.CYAN}✂️{Style.RESET_ALL}")
    print(f"{Fore.GREEN}──────────────────────────────────────────{Style.RESET_ALL}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    
    print(f"\n{Fore.YELLOW}📋 Select URL shortening provider:{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. {Fore.BLUE}Bit.ly {Fore.WHITE}(requires API key){Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. {Fore.BLUE}TinyURL {Fore.WHITE}(no API needed){Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. {Fore.BLUE}Da.gd {Fore.WHITE}(no API needed){Style.RESET_ALL}")
    
    provider = input(f"\n{Fore.GREEN}🔘 Enter your choice (1-3): {Style.RESET_ALL}")
    long_url = input(f"\n{Fore.GREEN}🌐 Enter the URL to shorten: {Style.RESET_ALL}")
    
    # URL validation
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'https://' + long_url
    
    print(f"\n{Fore.YELLOW}⏳ Processing...{Style.RESET_ALL}")
    short_url = shorten_url(long_url, provider)
    
    print(f"\n{Fore.GREEN}✨ {Fore.YELLOW}Result:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}──────────────────────────────────────────{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🔗 Original URL: {Fore.WHITE}{long_url}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}✂️ Shortened URL: {Fore.WHITE}{short_url}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}──────────────────────────────────────────{Style.RESET_ALL}")
    print(f"\n{Fore.MAGENTA}🎉 Done! Thank you for using our tool!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()