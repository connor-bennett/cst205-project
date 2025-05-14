from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
from backend.birds import bird_data
from backend.audio_visual.image_editing import (
    double_negative,
    apply_sunset_filter,
    apply_grayscale_filter,
)
from PIL import Image
from io import BytesIO
import base64
import random

app = Flask(__name__)
bootstrap = Bootstrap5(app)

def pil_to_data_uri(img: Image.Image) -> str:
    buf = BytesIO()
    img.save(buf, format='PNG')
    b64 = base64.b64encode(buf.getvalue()).decode('ascii')
    return f"data:image/png;base64,{b64}"

@app.route('/')
def hello():
    birds = []
    for image, data in bird_data.items():
        birds.append({
            'image': url_for('static', filename=f'images/{image}'),
            'audio': url_for('static', filename=f'bird_audio/{data["audio"]}'),
            'details': data["details"]
        })
    return render_template('index.html', birds=birds)

@app.route('/detail/<bird_name>', methods=['GET', 'POST'])
def detail(bird_name):
    data = bird_data.get(bird_name)
    if not data:
        return "Bird not found", 404

    img_path = f'static/images/{bird_name}'

    # Random filter selection on POST
    available_filters = ['original', 'negative', 'sunset', 'grayscale']
    choice = random.choice(available_filters) if request.method == 'POST' else 'original'

    # Apply selected filter
    if choice == 'negative':
        img_obj = double_negative(img_path)
    elif choice == 'sunset':
        img_obj = apply_sunset_filter(img_path)
    elif choice == 'grayscale':
        img_obj = apply_grayscale_filter(img_path)
    else:
        img_obj = Image.open(img_path)

    image_data = pil_to_data_uri(img_obj)

    # Data that call in the directory 
    bird_info = {
        'image_data': image_data,
        'audio': url_for('static', filename=f'bird_audio/{data["audio"]}'),
        'ai': url_for('static', filename=f'sound_images/{data["ai"]}'),
        'details': data["details"][0],
        'choice': choice
    }
    return render_template('detail_page.html', bird=bird_info)

if __name__ == "__main__":
    app.run(debug=True)
