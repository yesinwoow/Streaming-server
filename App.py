from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# তোমার video folder
VIDEO_PATH = "/storage/3CBE-B049/VIDEO💿💿/Song"

@app.route('/')
def index():
    search = request.args.get('search', '').lower()

    try:
        files = os.listdir(VIDEO_PATH)
    except Exception as e:
        return f"Error: {e}"

    videos = [f for f in files if f.lower().endswith((".mp4", ".mkv", ".avi"))]

    if search:
        videos = [v for v in videos if search in v.lower()]

    return render_template('index.html', videos=videos, search=search)

@app.route('/video/<path:filename>')
def stream_video(filename):
    return send_from_directory(VIDEO_PATH, filename)

if __name__ == '__main__':
    print("🚀 Server running on http://0.0.0.0:8000")
    app.run(host='0.0.0.0', port=8000)