from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from backend.birds import bird_data

app = Flask(__name__)
bootstrap = Bootstrap5(app)

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

@app.route('/detail/<bird_name>')
def detail(bird_name):
    data = bird_data.get(bird_name)
    if not data:
        return "Bird not found", 404

    bird_info = {
        'image': url_for('static', filename=f'images/{bird_name}'),
        'audio': url_for('static', filename=f'bird_audio/{data["audio"]}'),
        'details': data["details"]
    }
    return render_template('detail_page.html', bird=bird_info)

if __name__ == "__main__":
    app.run(debug=True)
