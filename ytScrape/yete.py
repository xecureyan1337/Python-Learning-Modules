import requests
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup

## downloading a youtube video

def download_video(url):
    opts = {}
    with YoutubeDL(opts) as yt:
        yt.download ([url])

    print(f"Downloaded video: {url}")

if __name__ == "__main__":
    url = ""
    download_video(url)