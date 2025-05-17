import requests
import time
import configparser
import os
from pystyle import Colors, Colorate

def format_message(prefix, message):
    cologreen_prefix = Colorate.Color(Colors.green, f"  [{Colors.white}!{Colors.green}]")
    return f"{cologreen_prefix}{Colors.reset} {message}"

def load_config():
    config = configparser.ConfigParser()
    config_file = 'status_config.ini'
    
    if not os.path.exists(config_file):
        print(format_message("!", "Config file not found, creating new one..."))
        token = input(f"   {Colors.green}┌───({Colors.reset}{os.getenv('COMPUTERNAME', 'unknown')}{Colors.green})\n   └──$ {Colors.reset}Enter your Discord token: ")
        interval = input(f"{Colors.green}   └──$ {Colors.reset}Enter the rotation interval (in seconds): ")
        statuses = input(f"{Colors.green}   └──$ {Colors.reset}Enter status messages (comma-separated): ")
        config['SETTINGS'] = {
            'token': token.strip(),
            'interval': interval.strip(),
            'statuses': statuses.strip()
        }
        
        with open(config_file, 'w') as f:
            config.write(f)
        print(format_message("!", "Configuration saved to status_config.ini"))
    else:
        config.read(config_file)
        
        if 'SETTINGS' not in config or not all(key in config['SETTINGS'] for key in ['token', 'interval', 'statuses']):
            print(format_message("!", "Incomplete configuration, please fill in the details..."))
            token = input(f"   {Colors.green}┌───({Colors.reset}{os.getenv('COMPUTERNAME', 'unknown')}{Colors.green})\n   └──$ {Colors.reset}Enter your Discord token: ")
            interval = input(f"{Colors.green}   └──$ {Colors.reset}Enter the rotation interval (in seconds): ")
            statuses = input(f"{Colors.green}   └──$ {Colors.reset}Enter status messages (comma-separated): ")
            
            config['SETTINGS'] = {
                'token': token.strip(),
                'interval': interval.strip(),
                'statuses': statuses.strip()
            }
            
            with open(config_file, 'w') as f:
                config.write(f)
            print(format_message("!", "Configuration updated in status_config.ini"))
    
    return config['SETTINGS']['token'], float(config['SETTINGS']['interval']), config['SETTINGS']['statuses'].split(',')

def change_status(token, status_text):
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    payload = {
        "custom_status": {
            "text": status_text,
            "expires_at": None
        }
    }
    
    try:
        response = requests.patch(url, headers=headers, json=payload, timeout=5)
        if response.status_code == 200:
            return True, status_text
        else:
            return False, f"API Error: {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """
          ▄████  ██░ ██      ██████ ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ █    ██   ██████ 
         ██▒ ▀█▒▓██░ ██▒   ▒██    ▒ ▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▒██    ▒ 
        ▒██░▄▄▄░▒██▀▀██░   ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░░ ▓██▄   
        ░▓█  ██▓░▓█ ░██      ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░  ▒   ██▒
        ░▒▓███▀▒░▓█▒░██▓   ▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ▒██████▒▒
         ░▒   ▒  ▒ ░░▒░▒   ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
          ░   ░  ▒ ░▒░ ░   ░ ░▒  ░ ░    ░      ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░▒  ░ ░
        ░ ░   ░  ░  ░░ ░   ░  ░  ░    ░        ░   ▒    ░       ░░░ ░ ░ ░  ░  ░  
              ░  ░  ░  ░         ░                 ░  ░           ░           ░  
                                                                                 
    """
    print(Colorate.Vertical(Colors.green_to_white, banner))
    print(format_message("!", "Discord Status Rotator by NightKikko"))
    
    token, interval, statuses = load_config()
    statuses = [status.strip() for status in statuses if status.strip()]
    
    if not statuses:
        print(format_message("!", "No valid status messages provided. Exiting."))
        return
    
    print(format_message("!", f"Loaded {len(statuses)} status messages. Interval: {interval}s"))
    
    while True:
        for status in statuses:
            success, message = change_status(token, status)
            if success:
                print(format_message("!", f"Status changed to '{message}'"))
            else:
                print(format_message("!", message))
            time.sleep(interval)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(format_message("!", "Status rotator stopped by user."))