## 🔁 GH-StatusRotator
A Python script to automatically rotate your **Discord custom status** using the Discord API — created by **NightKikko**! 🌟

### 📋 Prerequisites
- `🐍` Python 3.x installed
- `🌐` Internet connection
- `🎮` Discord account with a valid **user token**

### 🚀 Installation
1. `📥` **Clone the repository** or download the files manually.
2. `🔧` **Initial setup**:
   - Run `setup.bat` *(optional – create this to install from `requirements.txt` automatically)*
   - Launch the script using `run.bat` *(or manually with `python main.py`)*
     - On first launch, if `status_config.ini` doesn't exist, the script will prompt you for:
       - `🎫` **Discord User Token** — see how to obtain it below.
       - `⏱️` **Rotation Interval** — time (in seconds) between status changes.
       - `💬` **Status Messages** — comma-separated list of statuses you want to rotate through.
     - The script will save this information in `status_config.ini`.
   - You can manually edit the config later if needed.

3. `🖥️` **Run the script**:
   - Double-click `run.bat` or run `python main.py` in your terminal.

### 🔑 How to Get Your Discord User Token
⚠️ **Disclaimer**: This script requires your Discord **user token**. We **DO NOT collect** it — it is only stored locally for automation.

1. `🖥️` Open Discord in your browser (Chrome, Firefox, etc.).
2. `🔍` Press `Ctrl+Shift+I` (or `Cmd+Option+I` on Mac) to open Developer Tools.
3. `📡` Go to the **Network** tab.
4. `📨` Perform an action on Discord (like sending a message) to generate network traffic.
5. `🔎` Filter by `api` and click on a request (e.g., `messages`, `typing`, or `guilds`).
6. `👀` In the **Headers** section, look for the `Authorization` header.
7. `🔐` Copy the token value — it will look like `mfa.XXXX` or `XXXX.XXXX.XXXX`.
8. `📋` Paste it when prompted or add it directly in `status_config.ini`.

⚠️ **Important**: Never share your token — it gives full access to your account. If it’s ever leaked, change your password immediately to revoke it.

### 📂 Project Structure
- `status_config.ini` 🛠️ - Stores your token, interval, and status messages.
- `main.py` 💻 - Core script logic for rotating statuses.
- `requirements.txt` 📋 - Python dependencies (`pystyle`, `requests`, etc.).
- `run.bat` 🕹️ - Optional Windows batch file to launch the script.
- `setup.bat` 🔧 - Optional setup batch file to install dependencies.

### 🎮 Usage
- Once running, the script will cycle through your custom statuses at the set interval.
- Press `Ctrl+C` to stop it gracefully. 🚪

### ⚠️ Warnings
- 🚫 Never share your Discord user token with anyone.
- 🔒 Use this script responsibly. Automating a user account may violate [Discord's Terms of Service](https://discord.com/terms) — use at your own risk.

# ❤️ **Made by NightKikko for discord.gg/guildshub** ❤️
