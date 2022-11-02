import requests
import time
import subprocess
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

def checkIfYouTubeChannelIsLive(channel_id):
    
    channel_url = "https://www.youtube.com/channel/" + channel_id + "/live"
    page = requests.get(channel_url, cookies={'CONSENT': 'YES+42'})
    soup = BeautifulSoup(page.content, "html.parser")
    live = soup.find("link", {"rel": "canonical"})
    if live: 
        print("Streaming")
        return True
    else:
        print("Not Streaming")
        return False

def invokeStreamLink(channel_id):
    print("Attempting to open VLC stream...")
    subprocess.run(["streamlink", "--player",  "C:\Program Files\VideoLAN\VLC\\vlc.exe --file-caching=5000", "https://www.youtube.com/channel/" + channel_id + "/live", "best"])

def main():

    load_dotenv()
    CHANNEL_ID = os.getenv("CHANNEL_ID")
    result = False

    while result == False:
        print("Checking if channel is live...")
        result = checkIfYouTubeChannelIsLive(CHANNEL_ID)

        if result == True:
            break
        time.sleep(10)

    invokeStreamLink(CHANNEL_ID)
    

if __name__ == "__main__":
    main()