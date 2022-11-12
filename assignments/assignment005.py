f = open("newfile.txt", "w")
f.write("This is new text in a brandnew file")
f.close

f = open("newfile.txt")
print(f.readline())

#This (almost) worked at first try.

import os
os.remove("newfile.txt")