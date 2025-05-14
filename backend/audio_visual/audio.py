import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def main():
    BASE_URL = "https://avisoft.com/animal-sounds/#birds"
    PROJECT_ROOT = os.getcwd()  
    OUTPUT_DIR = os.path.join(PROJECT_ROOT, "static", "sound_images")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Fetching page
    resp = requests.get(BASE_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Find all .gif URLs in <a> hrefs and <img> srcs to cover all bases
    gif_urls = []
    # Collect from anchor tags
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.lower().endswith(".gif"):
            url = urljoin(BASE_URL, href)
            gif_urls.append(url)
    # Collect from img tags
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if src.lower().endswith(".gif"):
            url = urljoin(BASE_URL, src)
            if url not in gif_urls:
                gif_urls.append(url)

    if not gif_urls:
        print("No GIF URLs found on the page.")
        return
    
    # Send text to see if any images are found
    print(f"Found {len(gif_urls)} images, downloading up to 7...")

    # Download the first 7 to match the birds
    for gif_url in gif_urls[:7]:
        parsed = urlparse(gif_url)
        filename = os.path.basename(parsed.path)
        out_path = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(out_path):
            print(f"Skipping {filename}, already exists.")
            continue

        print(f"Downloading {gif_url} → {filename}")
        img_resp = requests.get(gif_url)
        img_resp.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(img_resp.content)

    print("Done. GIFs saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
