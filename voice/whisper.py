from faster_whisper import WhisperModel
from config import VOICE

print("Loading Whisper model...")

model = WhisperModel(
    VOICE["whisper_model"],
    device="cpu",
    compute_type="int8"
)

print("Whisper Loaded!")


def transcribe(audio_path: str) -> str:
    """
    Convert an audio file into text.
    """

    segments, _ = model.transcribe(
        audio_path,
        language="en",
        beam_size=5
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()