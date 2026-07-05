import pyttsx3

engine = pyttsx3.init()

# Configure voice
engine.setProperty("rate", 180)      # Speech speed
engine.setProperty("volume", 1.0)    # 0.0 - 1.0


def speak(text):
    print(f"Navya: {text}")
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Hello, I am Navya AI.")