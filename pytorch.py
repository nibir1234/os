# for i in range(10):
#     open(f"{i}.txt", 'w')

#! ==================================================

import string
from natsort import natsorted  # pip install natsort
import subprocess
import os
path = subprocess.run(['pwd'], capture_output=True).stdout.decode()
path = path[1:2] + ":" + path[2:-1] + "/PyTorch for Deep Learning"
if os.path.exists(path):
    # print("OK")
    files = os.listdir(path)


# print(files)
# print(sorted([item for item in files], reverse=False))
files = natsorted([item for item in files], reverse=False)
# print(files)


#! ===============Reading Lines,
#! ===============Removing whitespaces+\n + punctuation===============

file1 = open('filenames.txt', 'r')
Lines = file1.readlines()
for index, line in enumerate(Lines):
    stripped_line = line.strip()
    Lines[index] = stripped_line.translate(
        str.maketrans('', '', string.punctuation))
# print(Lines)


#! =====================RENAMING========================
for index, file in enumerate(files[:]):
    index = index
    print(index, file, end="\n")
    try:
        os.rename(os.path.join(path, file),
                  os.path.join(path, f"{index}_" + Lines[index]+".mp4"))
        continue
    except FileExistsError:
        print("================================")
        os.rename(os.path.join(path, file),
                  os.path.join(path, f"{index}_" + Lines[index]+f"_{index}.mp4"))


#! ======================================================

# import os
# os.system('pwd')
# os.system("cd ~")
# os.system('ls -la')


# x = subprocess.run(['ls', '-la'])
# x = subprocess.run(['pwd'], capture_output=True).stdout.decode()
# print("-===========================")
# print(x)
