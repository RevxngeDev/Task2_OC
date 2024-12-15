import os
import sys
import random
import time

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 minion.py <S>")
        sys.exit(1)

    try:
        S = int(sys.argv[1])
        if S <= 0:
            raise ValueError
    except ValueError:
        print("Error: <S> debe ser un número entero mayor que 0.")
        sys.exit(1)

    pid = os.getpid()
    ppid = os.getppid()
    print(f"Minion[{pid}]: created. Parent PID {ppid}.")

    time.sleep(S)

    exit_status = random.choice([0, 1])
    print(f"Child[{pid}]: before terminated. Parent PID {ppid}. Exit status {exit_status}.")

    sys.exit(exit_status)

if __name__ == "__main__":
    main()
