# Python script for youtube-dlp

Automatically downloads best video + best audio possible for specified youtube url.

## How to build?

_yt-dlp.exe_ and _ffmpeg.exe_ must be in the source directory.

[yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/download/2024.11.18/yt-dlp.exe)
[ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip) - Extract ffmpeg.exe

Run these commands:

1. `pip install pyinstaller`
2. `pyinstaller --onefile --add-binary ".\ffmpeg.exe;." --add-binary ".\yt-dlp.exe;." .\download.py`
