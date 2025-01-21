#!/usr/bin/python3
import os
import sys
import random

def create_child():
    """Crea un proceso hijo y ejecuta minion.py."""
    child_pid = os.fork()
    if child_pid == 0:
        random_number = random.randint(5, 10)
        os.execlp("python3", "python3", "minion.py", str(random_number))
    return child_pid

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 gru.py <N>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N <= 0:
            raise ValueError
    except ValueError:
        print("Error: <N> debe ser un número entero mayor que 0.")
        sys.exit(1)

    pid = os.getpid()
    print(f"Gru[{pid}]: Starting process creation.")

    children = []
    for _ in range(N):
        child_pid = create_child()
        print(f"Gru[{pid}]: process created. PID {child_pid}.")
        children.append(child_pid)

    while children:
        try:
            finished_pid, status = os.wait()
            exit_status = os.WEXITSTATUS(status)
            print(f"Gru[{pid}]: process terminated. PID {finished_pid}. Exit status {exit_status}.")

            if exit_status != 0:
                print(f"Gru[{pid}]: Restarting process for failed child.")
                new_child_pid = create_child()
                print(f"Gru[{pid}]: process created. PID {new_child_pid}.")
                children.append(new_child_pid)
            else:
                
                children.remove(finished_pid)
        except ChildProcessError:
            break

    print(f"Gru[{pid}]: All processes finished successfully. Exiting.")
    sys.exit(0)

if __name__ == "__main__":
    main()
