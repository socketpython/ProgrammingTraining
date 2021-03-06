# FileScanner.py
#
# Programmer   : Elad L
# Student no.  : 217
# Date         : 03/10/2020
#
# ---------------------------------------------------

# Imports
import argparse
import concurrent.futures
import os

# Constants
extensions = {}
res = ""
counter = 0
decor = 20

parser = argparse.ArgumentParser(description="Gets paths of folders and return the count of file types")
parser.add_argument('-d', "--directory", type=str, help='Enter paths and between them ","')
args = parser.parse_args()

folders = args.d.split(",")


def going_through_dir(path, exts):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    
    for file in files:
        filename, file_extension = os.path.splitext(f'{path}\{file}')
        file_extension = file_extension[1:]
        if exts.get(file_extension) == None:
            exts[file_extension] = 1
        else:
            exts[file_extension] += 1
    
    return exts
 

def main():
    print(f"{'-' * decor}FileScanner{'-' * decor}")
    for folder in folders:
        with concurrent.futures.ThreadPoolExecutor() as executer:
            extensions = executer.submit(going_through_dir, folder, extensions).result()

    for i in extensions.items():
        counter += i[1]

    for i in extensions.items():
        ext = i[0]
        amount = i[1]
        percent = int((amount / counter) * 100)
        res += f"{ext.ljust(10)} - {amount} files ({percent}%)\n"

    print(res[:-1])
    print(f"{'-' * (2 * decor + 11)}")

if __name__ == "__main__":
    main()
