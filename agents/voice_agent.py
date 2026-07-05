from utils.speech import listen
from utils.tts import speak
from assistant import process_command


def start_voice():
    print("Voice mode started. Say 'exit' to quit.")

    while True:
        command = listen()

        if not command:
            continue

        print("You:", command)

        if command.lower() == "exit":
            speak("Goodbye")
            break

        response = process_command(command)

        print("Navya:", response)

        speak(response)