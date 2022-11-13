#f = open("newfile.txt", "w")
#f.write("This is new text in a brandnew file")
#f.close()

#f = open("newfile.txt")
#print(f.readline())
#f.close()

#This (almost) worked at first try.

import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("This file does not exist.")
#This only works when you close the file first.
#Closing only works when you put the two brackets after "close" (duh).

#Removing worked fine, but printing the text did not.
#This is because the file exists each time, because at the beginning of the
#script, I create it. It then gets deleted.
#Have to comment out the creation for the rest to work.