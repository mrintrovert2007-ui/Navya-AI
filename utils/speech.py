import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

print("Loading Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Whisper model loaded!")

SAMPLE_RATE = 16000
DURATION = 5


def listen():
    print("🎤 Listening...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write("recording.wav", audio, SAMPLE_RATE)

    segments, info = model.transcribe(
        "recording.wav",
        language="en",
        beam_size=5
    )

    text = ""

    for segment in segments:
        print(f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text}")
        text += segment.text

    text = text.strip()

    print(f"\nFinal Text: {text}")

    return text


if __name__ == "__main__":
    listen()