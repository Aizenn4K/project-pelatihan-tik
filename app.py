from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load data makanan
with open('data/makanan.json', 'r', encoding='utf-8') as f:
    data_makanan = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', makanan=data_makanan)

@app.route('/hitung', methods=['POST'])
def hitung():
    selected = request.json.get('makanan', [])
    total_kalori = 0
    for item in selected:
        for makanan in data_makanan:
            if makanan["nama"] == item:
                total_kalori += makanan["kalori"]
    return jsonify({"total": total_kalori})

@app.route('/saran', methods=['GET'])
def saran():
    if len(data_makanan) > 0:
        saran_menu = sorted(data_makanan, key=lambda x: x['kalori'])[:3]
        return jsonify(saran_menu)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
