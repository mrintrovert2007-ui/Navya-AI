from router.fast_router import fast_route
from llm.model import ask_navya
from router.action_router import execute


def process_command(command: str):

    action = fast_route(command)

    if action:
        print("[Fast Router]")
    else:
        print("[LLM]")
        action = ask_navya(command)

    return execute(action)