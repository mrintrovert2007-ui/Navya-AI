from voice.recorder import start_stream, get_audio_chunk
from voice.vad import is_speech

stream = start_stream()

print("Listening...")

while True:

    chunk = get_audio_chunk()

    if is_speech(chunk):
        print("Speech")
    else:
        print("Silence")