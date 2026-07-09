import soundfile as sf
from utils.recorder import record_until_silence, SAMPLE_RATE

print("Speak something...")

audio = record_until_silence()

sf.write("recording.wav", audio, SAMPLE_RATE)

print("Recording saved as recording.wav")