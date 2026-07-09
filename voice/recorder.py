import sounddevice as sd
import queue
import numpy as np

SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_SIZE = 512

audio_queue = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)

    audio_queue.put(indata.copy())


def start_stream():
    """
    Start continuous microphone streaming.
    """

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        blocksize=BLOCK_SIZE,
        dtype="float32",
        callback=callback
    )

    stream.start()

    return stream


def get_audio_chunk():
    """
    Return one audio chunk from the queue.
    """

    return np.squeeze(audio_queue.get())