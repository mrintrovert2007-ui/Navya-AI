from llm.model import ask_navya
from router.router import execute

print("=" * 40)
print("        Welcome to Navya AI")
print("=" * 40)

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        print("Goodbye!")
        break

    action = ask_navya(command)

    result = execute(action)

    print("\nNavya:", result)