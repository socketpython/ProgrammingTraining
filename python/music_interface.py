# music_interface.py
#
# Programmer   : Elad L
# Date         : 22/09/2020
#
# 
# ---------------------------------------------------


# install youtube-dl, requests, playsound via pip install
# Imports
import os
import youtube_dl
import requests
from playsound import playsound
import random
import multiprocessing


# Constants
path = r"C:\Users\Elad_Levi\Desktop\Music" # enter here you music folder's path
names_path = r"C:\Users\Elad_Levi\Desktop\Music\py_cache\names.txt" # enter here you music DB's path
artists_path = r"C:\Users\Elad_Levi\Desktop\Music\py_cache\artists.txt" # enter here you artist DB's path
options = ["Download YouTube video", "Show the music in the DB",
           "Play random music", "Delete song", "Play specific song",
           "Add artist", "Play music by artist",
           "Exit the program"]


def update_db(data):
    global names_path

    data.sort()
    res = ""
    for i in data:
        res += f"{i}\n"
    res = res[:-1]
    with open(names_path, "w") as f:
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
    
    global path, names_path
    
    with open(names_path, "r") as names_file:
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
    
    global names_path
    with open(names_path, "r") as f:
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
    global names_path, path
    with open(names_path, "r") as f:
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
    
    global path
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
    
    global path
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
    global artists_path
    artist_name = input("Enter the name of the artist you want to add: ").lower()
    
    with open(artists_path, "r") as artists:
        data = artists.read()
    if artist_name in data:
        print("Artist is already exist")
        return
    
    with open(artists_path, "a") as artists:
        artists.write(f"{artist_name}\n")


def play_artist():
    global artists_path, names_path, path

    with open(artists_path, "r") as artist:
        artists = artist.read().splitlines()
    index = 1
    for artist in artists:
        print(f"{index}. {artist.title()}")
        index +=1

    try:
        chosen_artist = int(input("Enter the number according to your choice: "))
        artist_name = artists[chosen_artist - 1]
        songs = []
        with open(names_path, "r") as f:
            data = f.read().splitlines()

        for song in data:
            if artist_name in song.lower():
                songs.append(song)

        while True:
            song_name = random.choice(songs)
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
    except:
        print("The number you entered is invalid")
        return


def main():
    choice = 0
    while choice != 8:
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


if __name__ == "__main__":
    main()
