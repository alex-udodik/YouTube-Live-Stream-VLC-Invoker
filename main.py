import requests
import time
import subprocess
import os

from dotenv import load_dotenv
from bs4 import BeautifulSoup

def checkIfYouTubeChannelIsLive(channel_id, key):
    response = requests.get("https://www.googleapis.com/youtube/v3/search?channelId=" + channel_id + "&eventType=live&type=video&key=" + key)
    data = response.json()
    
    items = data["items"]
    
    if len(items) > 0:
        print("Stream is live.")
        return True
    
    print("Stream is offline.")
    return False

def invokeStreamLink(channel_id):
    print("Attempting to open VLC stream...")
    subprocess.run(["streamlink", "--player",  "C:\Program Files\VideoLAN\VLC\\vlc.exe --file-caching=5000", "https://www.youtube.com/channel/" + channel_id + "/live", "best"])

def main():

    load_dotenv()
    CHANNEL_ID = os.getenv("CHANNEL_ID")
    API_KEY = os.getenv("API_KEY")
    result = False

    while result == False:
        print("Checking if channel is live...")
        result = checkIfYouTubeChannelIsLive(CHANNEL_ID, API_KEY)

        if result == True:
            break
        time.sleep(10)

    invokeStreamLink(CHANNEL_ID)
    
if __name__ == "__main__":
    main()