from pydub import AudioSegment
import numpy as np

def analyze_loudness_per_second(mp3_path):
    audio = AudioSegment.from_mp3(mp3_path)
    duration_sec = int(audio.duration_seconds)
    loudness_data = []
    for i in range(duration_sec):
        segment = audio[i*1000:(i+1)*1000]
        samples = np.array(segment.get_array_of_samples())
        rms = np.sqrt(np.mean(samples**2))
        max_possible = np.iinfo(samples.dtype).max
        rms_norm = rms / max_possible
        dB = 20 * np.log10(rms_norm) if rms_norm > 0 else -240
        loudness_data.append({'time': i, 'dB': abs(round(dB, 2))})
    return loudness_data
