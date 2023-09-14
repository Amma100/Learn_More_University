import re

word = input("Enter file to be opened: ")
file_handle = open(word, 'r')

for line in file_handle:
    wr = line.rstrip()

    x = re.findall("[\w)]{2,30} [\w-]{2,15}:", wr)
    if x:
        for i in x:
            n = i.split()
            print(n)
