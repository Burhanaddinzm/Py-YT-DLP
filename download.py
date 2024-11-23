# Command :
# pyinstaller --onefile --add-binary ".\ffmpeg.exe;." --add-binary ".\yt-dlp.exe;." .\download.py

import subprocess
import re
import traceback
import sys
import os

def get_executable_path(file_name):
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        return os.path.join(sys._MEIPASS, file_name)  # Path to bundled files
    return os.path.join(os.getcwd(), file_name)  # Local directory for scripts

def is_valid_url(url):
    # Simple regex to validate URL
    regex = re.compile(
        r'^(https?://)'  # http:// or https://
        r'([a-zA-Z0-9.-]+)'  # domain name
        r'([:/][0-9]*)?'  # optional port
        r'(/.*)?$',  # optional path
        re.IGNORECASE)
    return re.match(regex, url) is not None

def download_video(url):
    try:
        yt_dlp_path = get_executable_path("yt-dlp.exe")
        subprocess.run([yt_dlp_path, "-f", "bestvideo+bestaudio/best", "--merge-output-format", "mp4", url], check=True)
        print("Download completed successfully.")
    except subprocess.CalledProcessError as cpe:
        print("A subprocess error occurred!")
        error_message = f"CalledProcessError: {cpe.returncode}\nOutput: {cpe.output}\n"
        log_error(error_message)
    except Exception as e:
        print(f"An error occurred while trying to download the video: {e}")
        error_message = traceback.format_exc()
        log_error(error_message)

def log_error(message):
    """Logs error messages to a file."""
    with open('error_log.txt', 'a') as log_file:
        log_file.write(f"{message}\n")

def main():
    url = None
    while url is None:
        user_input = input("Enter the URL that you want to download: ")
        if is_valid_url(user_input.strip()):
            url = user_input
        else:
            print("Invalid URL. Please try again.")

    download_video(url)

if __name__ == "__main__":
    main()
