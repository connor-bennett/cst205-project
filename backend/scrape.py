import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# bird webpage
BASE_URL = "https://avisoft.com/animal-sounds/"

# Output folder: inside /static/ for Flask access
OUTPUT_FOLDER = "static/bird_audio"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# request the page
response = requests.get(BASE_URL)
soup = BeautifulSoup(response.content, "html.parser")

# find the sound files
audio_links = soup.find_all("a", href=True)
downloaded = 0

for link in audio_links:
    href = link["href"]
    if href.endswith(".wav") or href.endswith(".mp3"):
        full_url = urljoin(BASE_URL, href)
        filename = full_url.split("/")[-1]
        filepath = os.path.join(OUTPUT_FOLDER, filename)

        # skip download if file already exists
        if os.path.exists(filepath):
            print(f"Skipping {filename} (already exists)")
            continue

        print(f"Downloading: {filename}")
        try:
            audio_data = requests.get(full_url).content
            with open(filepath, "wb") as f:
                f.write(audio_data)
            downloaded += 1
            if downloaded >= 7:
                break  # Limit to 7 files
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

print(f"Finished. {downloaded} audio files saved to {OUTPUT_FOLDER}")
