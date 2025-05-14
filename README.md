Here's a complete `README.md` file for your CST 205 Final Project — Bird Encyclopedia Flask App, based on the full folder structure, Python modules, templates, and functionality you provided:

---

# 🐦 Bird Encyclopedia — CST 205 Final Project

A Flask web application that allows users to browse, learn about, view, and listen to birds native to the EU region. The app also includes image editing filters (negative, sunset, grayscale) applied live using Pillow (PIL).

## 📁 Project Structure

```
├── app.py                  # Flask application entry point
├── backend/                # Contains backend logic
│   ├── birds.py            # Bird metadata and details
│   └── audio_visual/
│       ├── audio.py        # (reserved for future audio logic)
│       └── image_editing.py# Functions to edit images with PIL
├── scrape.py               # Web scraper to download bird audio clips
├── static/                 # Static files
│   ├── bird_audio/         # Downloaded bird sounds (.wav/.mp3)
│   ├── images/             # Bird image files
│   └── styles.css          # Custom CSS
├── templates/              # HTML templates for Flask
│   ├── index.html          # Homepage
│   └── detail_page.html    # Bird detail view
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Features

* Browse a curated selection of European birds.
* View scientific names, population, location, and description.
* Listen to authentic bird calls sourced from [avisoft.com](https://avisoft.com/animal-sounds/).
* Apply **live image filters** using Pillow:

  * **Negative** (inverts colors)
  * **Sunset** (adds warm tones)
  * **Grayscale** (black-and-white)
* Built-in Bootstrap 5 theming with a dark mode design.
* Spectrogram Viewing of each Bird Noise

## 🧠 Technologies Used

* **Python 3**
* **Flask**
* **Jinja2** (Flask templating)
* **Pillow (PIL)** for image manipulation
* **BeautifulSoup4** and `requests` for scraping audio
* **Bootstrap 5** (via Flask-Bootstrap)

## 🖼️ Image Filters (via `image_editing.py`)

* `double_negative`: Applies negative twice (to demonstrate image inversion)
* `apply_sunset_filter`: Reduces blue and green channels to give a warm sunset tone
* `apply_grayscale_filter`: Converts RGB images to grayscale

## 🔊 Scraper (`scrape.py`)

Downloads the first 7 `.wav` or `.mp3` bird audio files from `https://avisoft.com/animal-sounds/` into `static/bird_audio/`. Automatically skips already downloaded files.

## Spectrogram Scraper ('audio.py')

Downloads the first 7 `.img` or `.gif` bird image files from `https://avisoft.com/animal-sounds/#birds` into `static/sound_images/`. Skips already downloaded files. 

## 📷 Dynamic Filtering Logic

The user can choose a filter via an HTML form (POST). Based on the choice:

```python
if choice == 'negative':
    img_obj = double_negative(img_path)
elif choice == 'sunset':
    img_obj = apply_sunset_filter(img_path)
elif choice == 'grayscale':
    img_obj = apply_grayscale_filter(img_path)
```

This image is converted to a base64 URI and displayed directly, without writing to disk.

## 🛠️ Installation & Usage

1. **Clone this repo**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/bird-encyclopedia.git
   cd bird-encyclopedia
   ```

2. **Install dependencies**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **(Optional) Scrape audio files**:

   ```bash
   python scrape.py
   ```

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. Open your browser to `http://127.0.0.1:5000`

## 🧪 Example Bird Entry (from `birds.py`)

```python
"little_grebe.png": {
    "audio": "zwergta.wav",
    "details": [
        {
            "english": "Little Grebe",
            "german": "Zwergtaucher",
            "scientific": "Tachybaptus ruficollis",
            "location": "Germany, Berlin-Wilhelmsruh",
            "population": "610,000 to 3,500,000",
            "description": "A small, compact diving waterbird..."
        }
    ]
}
```

## 👨‍💻 Credits

* Developed by **Team 8241** for CST 205 Final Project:
* Connor Bennett, Julian Mendoza, Ulises Rodriguez
* Audio data courtesy of [Avisoft Bioacoustics](https://avisoft.com/animal-sounds/)
* Styled using **Bootstrap 5**

