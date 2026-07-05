from assistant import process_command
from agents.voice_agent import start_voice

print("=" * 40)
print("        Welcome to Navya AI")
print("=" * 40)

mode = input("Choose mode (text/voice): ").strip().lower()

if mode == "voice":
    start_voice()

else:
    while True:
        command = input("\nYou: ")

        if command.lower() == "exit":
            print("Goodbye!")
            break

        result = process_command(command)

        print("\nNavya:", result)