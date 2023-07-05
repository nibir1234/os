# for i in range(10):
#     open(f"{i}.txt", 'w')

#! ==================================================

import subprocess
import os
path = subprocess.run(['pwd'], capture_output=True).stdout.decode()
path = path[1:2] + ":" + path[2:-1] + "/t"
if os.path.exists(path):
    # print("OK")
    files = os.listdir(path)


# print(sorted([item for item in files], reverse=True))

# for index, file in enumerate(files):
# print(index, file, end="\n")

# os.rename(os.path.join(path, file),
#           os.path.join(path, str(index) + '.txt'))


#! ======================================================

# import os
# os.system('pwd')
# os.system("cd ~")
# os.system('ls -la')


# x = subprocess.run(['ls', '-la'])
# x = subprocess.run(['pwd'], capture_output=True).stdout.decode()
# print("-===========================")
# print(x)
