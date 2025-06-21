import threading
import time
from .audio_utils import analyze_loudness_per_second

def stream_loudness(mp3_path, socketio, sid):
    loudness_data = analyze_loudness_per_second(mp3_path)
    socketio.emit('loudness_all', loudness_data, to=sid)
