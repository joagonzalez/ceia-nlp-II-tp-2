import sys
from src.chatService import session


if __name__ == "__main__": 
    try:
        while True:
            msg = input("You: ")
            if msg.lower() in ["exit", "quit"]:
                break
            session.chat(msg)
            print()  # For better readability
    except KeyboardInterrupt:
        print("\nNos vemos la proxima.")
        sys.exit(0)
