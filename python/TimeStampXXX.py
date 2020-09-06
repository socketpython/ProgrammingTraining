import os
import time
import datetime
import getpass


def going_through_dir(path, current_time):
    files_name = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files_name.extend(filenames)
        break

    files = {}
    for file in files_name:
        filename, file_extension = os.path.splitext(f'{path}\{file}')
        last_modified = time.ctime(os.path.getmtime(f"{path}\{file}"))
        last_modified = datetime.datetime.strptime(last_modified, "%a %b %d %H:%M:%S %Y")
        files[file] = current_time - last_modified
    return files


def changed_last_month(files):
    susp_files = []
    for (file_name, difference) in files.items():
        if difference.days < 31:
            susp_files.append(file_name)
    return susp_files


def main():
    current_time = datetime.datetime.now()
    path = r"c:\Windows\System32"
    first_name = input("Enter your first name: ")
    personal_number = int(input("Enter your personal number: "))
    while True:
        done = False
        while not done:
            choice = input("If you want to scan the 'system32' folder press the enter button, else enter the folder's path: ")
            if choice != "" and os.path.isdir(choice):
                path = choice
                done = True
            elif choice != "":
                print("The path you entered doesn't exist")
            else:
                done = True

        files = going_through_dir(path, current_time)

        susp_files = changed_last_month(files)

        data = f"""
First name: {first_name}
Personal number: {personal_number}
Date of the check: {current_time}
User name: {getpass.getuser()}
"""
        for i in susp_files:
            data += f"\n{i}"
    
        with open("log.txt", "a") as log_file:
            log_file.write(data)
        
        con = input("Continue? (y/n)").lower()
        if con == "y":
            continue
        elif con == "n":
            break
        

if __name__ == "__main__":
    main()
