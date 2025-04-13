# Phase 15: Execution Orchestrator
from phase_01 import generate_response
from phase_02 import detect_emotion

def run_all():
    detect_emotion()
    user_input = input("Talk to SoulMate: ")
    response = generate_response(user_input)
    print(response)

if __name__ == "__main__":
    run_all()