import torch
import numpy as np

print("Loading Silero VAD...")

model, utils = torch.hub.load(
    "snakers4/silero-vad",
    "silero_vad",
    trust_repo=True,
)

(get_speech_timestamps,
 save_audio,
 read_audio,
 VADIterator,
 collect_chunks) = utils

print("Silero VAD Loaded!")


def is_speech(audio_chunk, sample_rate=16000):
    """
    Returns True if the audio chunk contains speech.
    """

    if len(audio_chunk) == 0:
        return False

    audio = torch.from_numpy(audio_chunk)

    timestamps = get_speech_timestamps(
        audio,
        model,
        sampling_rate=sample_rate,
    )

    return len(timestamps) > 0