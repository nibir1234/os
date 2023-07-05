import string

file1 = open('filenames.txt', 'r')
Lines = file1.readlines()

for index, line in enumerate(Lines):
    stripped_line = line.strip()
    Lines[index] = stripped_line.translate(
        str.maketrans('', '', string.punctuation))

print(Lines)
print(len(Lines))
