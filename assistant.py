from llm.model import ask_navya
from router.action_router import execute


def process_command(command: str):
    action = ask_navya(command)
    result = execute(action)
    return result