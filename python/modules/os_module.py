import os
import time

curDir = os.getcwd()
print(curDir)

os.mkdir('new_folder')

time.sleep(2)

os.rename('new_folder', 'folder')

time.sleep(2)

os.rmdir('folder')
