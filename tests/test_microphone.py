from voice.recorder import start_stream, get_audio_chunk
import numpy as np

stream = start_stream()

print("Listening...")

while True:
    chunk = get_audio_chunk()

    print(np.max(np.abs(chunk)))