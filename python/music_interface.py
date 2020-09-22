# install youtube-dl, requests, playsound via pip install
import os
import youtube_dl
import requests
from playsound import playsound
import random
import multiprocessing


path = r"C:\Users\Elad_Levi\Desktop\Music" # enter here you music folder's path
file_path = r"C:\Users\Elad_Levi\Desktop\Music\py_cache\names.txt" # enter here you music DB's path

options = ["Download YouTube video", "Show the music in the DB",
           "Play random music", "Delete song", "Play specific song",
           "Add artist", "Play music by artist",
           "Exit the program"]


def update_db(data):
    global file_path

    data.sort()
    res = ""
    for i in data:
        res += f"{i}\n"
    res = res[:-1]
    with open(file_path, "w") as f:
        f.write(res)


def download():
    """
    The function requests the URL of and downloads an MP3 file if it is valid
    """
    
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
        
        # Checking that the URL is correct
        if "Video unavailable" in r.text:
            print("The url you entered is invalid")
            return
        ydl.download([url_input])

    manage()
    print("Donload done")


def manage():
    """
    The function is responsible for updating the database if a file is added
    """
    
    global path, file_path
    
    with open(file_path, "r") as names_file:
        names = names_file.read().splitlines()

    files = []
    for _, _, filenames in os.walk(path):
        files.extend(filenames)
        break

    for file in files:
        current_file_path = f"{path}\{file}"
        name, ext = os.path.splitext(file)

        # Checks that the extension is indeed MP3
        # and that the name appears in the database
        if ext == ".mp3" and name not in names:
            name = name[:-12]
            os.rename(current_file_path, f"{path}\{name}{ext}")
            print(f"{file} changed into {name}{ext}")
            names.append(name)
    update_db(names)


def check_choice(choice):
    """
    Checks whether the menu selection is in range
    """
    
    global options
    return 1 <= choice <= len(options)


def menu():
    """
    Prints the menu and returns the selection after checking that it is correct
    """
    
    global options
    print(f"\n\n{'*' * 15}Music Interface{'*' * 15}")
    txt = "Select the desired option from the following options:\n"
    index = 1
    for opt in options:
        txt += f"{index} - {opt}\n"
        index += 1
    print(txt)
    while True:
        choice = input("Enter the number according to your choice: ")

        # Checks whether the value is numeric and in range
        if choice.isnumeric() and check_choice(int(choice)):
            break
        else:
            print("The number you entered is invalid")
    return int(choice)


def show_db():
    """
    Prints the database and returns the list of songs
    """
    
    global file_path
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    counter = 1
    for i in data:
        num = f"{counter}.".ljust(4)
        print(f"{num}{i}")
        counter += 1
    
    return data


def play_random():
    """
    Plays a random song from the folder
    """
    global file_path, path
    with open(file_path, "r") as f:
        names = f.read().splitlines()
    
    while True:
        song_name = random.choice(names)
        song_path = f"{path}\{song_name}.mp3"
        print(f"Playing: {song_name}")
        p = multiprocessing.Process(target=playsound, args=(song_path,))
        p.start()
        print("Enter next, stop or background")
        a = input("-> ").lower()
        if a == "next":
            p.terminate()
            continue
        elif a == "stop":
            p.terminate()
            break
        elif a == "background":
            break
        p.terminate()


def play_song():
    """
    Plays a specific song from the folder
    """
    
    global file_path, path
    while True:
        data = show_db()

        valid = False
        while not valid:
            song_num = int(input("Enter the number of the song you want to play: "))
            if 0 < song_num <= len(data):
                valid = True
            else:
                print("The number you entered is invalid")
        
        song_name = f"{data.pop(song_num - 1)}.mp3"
        song_path = f"{path}\{song_name}"
        if os.path.exists(song_path):
            print(f"Playing: {song_name}")
            p = multiprocessing.Process(target=playsound, args=(song_path,))
            p.start()
            print("Enter next, stop or background")
            a = input("-> ").lower()
            if a == "next":
                p.terminate()
                continue
            elif a == "stop":
                p.terminate()
                break
            elif a == "background":
                break
            p.terminate()
        else:
            print("The file does not exist")
        


def del_songs():
    """
    Deletes songs of the user's choice
    """
    
    global file_path, path
    while True:
        data = show_db()
        
        valid = False
        while not valid:
            song_num = int(input("Enter the number of the song you want to delete: "))
            if 0 < song_num <= len(data):
                valid = True
            else:
                print("The number you entered is invalid")
        song_name = f"{data.pop(song_num - 1)}.mp3"
        song_path = f"{path}\{song_name}"
        if os.path.exists(song_path):
            os.remove(song_path)
            print(f"{song_name} deleted succesfuly")
        else:
            print("The file does not exist")

        update_db(data)

        choice = input("Do you want to continue? (y/n) ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            break


def add_artist():
    pass


def play_artist():
    pass


def main():
    while True:
        choice = menu()
        
        if choice == 1:
            download()
        
        elif choice == 2:
            show_db()
        
        elif choice == 3:
            play_random()

        elif choice == 4:
            del_songs()
        
        elif choice == 5:
            play_song()
        
        elif choice == 6:
            add_artist()
        
        elif choice == 7:
            play_artist()

        elif choice == 8:
            break


if __name__ == "__main__":
    main()
