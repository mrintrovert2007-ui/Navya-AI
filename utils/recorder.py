import sounddevice as sd
import numpy as np


SAMPLE_RATE = 16000
CHANNELS = 1

CHUNK_DURATION = 0.1      # 100 ms
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)


def rms(audio):
    """Calculate volume of an audio chunk."""
    return np.sqrt(np.mean(audio ** 2))


def record_until_silence(
    silence_threshold=0.01,
    silence_duration=1.0,
):
    """
    Record until user stops speaking.
    """

    print("🎤 Waiting for speech...")

    recording = []

    speaking = False

    silent_chunks = 0

    max_silent_chunks = int(silence_duration / CHUNK_DURATION)

    while True:

        chunk = sd.rec(
            CHUNK_SIZE,
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32"
        )

        sd.wait()

        volume = rms(chunk)

        # User started speaking
        if volume > silence_threshold:

            if not speaking:
                print("🟢 Speech detected")

            speaking = True

            silent_chunks = 0

            recording.append(chunk)

        else:

            if speaking:

                recording.append(chunk)

                silent_chunks += 1

                if silent_chunks >= max_silent_chunks:

                    print("🔴 End of speech")

                    break

    return np.concatenate(recording, axis=0)