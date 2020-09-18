# install youtube-dl, requests via pip install
import os
import youtube_dl
import requests


options = ["Download YouTube video", "Manage the names in the 'Music' folder",
           "Exit the program"]


def check(name, names):
    for n in names:
        if n == name:
            return False
    return True


def manage():
    path = r"C:\Users\Elad_Levi\Desktop\Music"
    file_path = r"C:\Users\Elad_Levi\Desktop\Music\py_cache\names.txt"

    names = []
    with open(file_path, "r") as names_file:
        names.extend(names_file.read().splitlines())

    files = []
    for _, _, filenames in os.walk(path):
        files.extend(filenames)
        break


    for file in files:
        current_file_path = f"{path}\{file}"
        name, ext = os.path.splitext(file)
        if ext == ".mp3" and check(name, names):
            name = name[:-12]
            os.rename(current_file_path, f"{path}\{name}{ext}")
            print(f"{file} changed into {name}{ext}")
            with open(file_path, "a") as names_file:
                names_file.write(f"{name}\n")


def download():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url_input = str(input("Enter the url: "))
        if url_input == "exit" or url_input == "":
            return
        r = requests.get(url_input)
        if "Video unavailable" in r.text:
            print("The url you entered is invalid")
            return
        ydl.download([url_input])

    print("Donload done")


def check_choice(choice):
    global options
    return 1 <= choice <= len(options)


def menu():
    global options
    print()
    print()
    print(f"{'*' * 15}Music Interface{'*' * 15}")
    txt = "Select the desired option from the following options:\n"
    index = 1
    for opt in options:
        txt += f"{index} - {opt}\n"
        index += 1
    print(txt)
    while True:
        choice = input("Enter the number according to your choice: ")
        if choice.isnumeric() and check_choice(int(choice)):
            break
    return int(choice)


def main():
    while True:
        choice = menu()
        if choice == 1:
            download()
        elif choice == 2:
            manage()
        elif choice == 3:
            break


if __name__ == "__main__":
    main()
