f = open("newfile.txt", "w")
f.write("This is new text in a brandnew file")
f.close()

f = open("newfile.txt")
print(f.readline())
f.close()

#This (almost) worked at first try.

import os
os.remove("newfile.txt")
#This only works when you close the file first.
#Closing only works when you put the two brackets after "close" (duh).