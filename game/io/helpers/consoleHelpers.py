import os
import subprocess


def clear_console():
    os_name = os.name
    if os_name in ('nt','dos'):
        subprocess.call("cls")
    elif os_name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n" * 120)
