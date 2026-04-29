from flask import Flask, request
import os
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def resize_image(filepath):
    img = Image.open(filepath)
    img = img.resize((300, 300))  # Transform step
    img.save(filepath)

@app.route("/")
def home():
    return "MiniDrive Amazon Web Services Running"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    resize_image(filepath)  # 🔥 ETL step

    return f"Uploaded and resized {file.filename}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)