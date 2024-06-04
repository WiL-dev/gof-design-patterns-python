"""Mock up of a connection"""

import time

def connect() -> None:
    """Simulates a connection"""
    print("Connecting", end='', flush=True)
    for _ in range(3):
        time.sleep(1)
        print(".", end='', flush=True)

    time.sleep(1)
    print("\nConnected!")
