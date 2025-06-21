import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from analysis.realtime import stream_loudness

load_dotenv()
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3'}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app, cors_allowed_origins="*")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'mp3file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'})
    file = request.files['mp3file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'success': True, 'url': f'/uploads/{filename}'})
    return jsonify({'success': False, 'error': 'Invalid file'})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@socketio.on('connect')
def handle_connect():
    print('Client connected:', request.sid)

@socketio.on('start_analysis')
def handle_start_analysis(data):
    mp3_url = data.get('url')
    filename = mp3_url.split('/')[-1]
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    socketio.start_background_task(stream_loudness, filepath, socketio, request.sid)

if __name__ == '__main__':
    socketio.run(app, debug=True)
