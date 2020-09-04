import argparse
import concurrent.futures
import os


parser = argparse.ArgumentParser(description="Gets paths of folders and return the count of file types")
parser.add_argument('-d', type=str,
                   help='Enter paths and between them ","')
args = parser.parse_args()

folders = args.d.split(",")

extensions = {}


def going_through_dir(path, exts):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    for file in f:
        filename, file_extension = os.path.splitext(f'{path}\{file}')
        file_extension = file_extension[1:]
        if exts.get(file_extension) == None:
            exts[file_extension] = 1
        else:
            exts[file_extension] += 1
    return exts
 

print(f"{'-' * 20}FileScanner{'-' * 20}")
for folder in folders:
    with concurrent.futures.ThreadPoolExecutor() as executer:
        extensions = executer.submit(going_through_dir, folder, extensions).result()

counter = 0
for i in extensions.items():
    counter += i[1]

res = ""
for i in extensions.items():
    ext = i[0]
    amount = i[1]
    percent = int((amount / counter) * 100)
    res += f"{ext.ljust(10)} - {amount} files ({percent}%)\n"

print(res[:-1])
print(f"{'-' * 51}")