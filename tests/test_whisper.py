from voice.whisper import transcribe

text = transcribe("recording.wav")

print(text)