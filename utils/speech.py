import soundfile as sf
from faster_whisper import WhisperModel
from utils.recorder import record_until_silence, SAMPLE_RATE

print("Loading Whisper model...")
model = WhisperModel("base", device="cpu", compute_type="int8")
print("Whisper model loaded!")

def listen():
    # Use your VAD function instead of hardcoded 5 seconds
    audio_data = record_until_silence()
    
    if len(audio_data) == 0:
        return ""

    # Save temporary file (or pass numpy array directly if supported by your faster_whisper version)
    sf.write("recording.wav", audio_data, SAMPLE_RATE)

    segments, info = model.transcribe("recording.wav", language="en", beam_size=5)

    text = " ".join([segment.text for segment in segments]).strip()
    print(f"\nFinal Text: {text}")
    return text