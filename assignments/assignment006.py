#f = open ("newsample.txt","w")
#text = f.write("Why the heck is there no text in this file \n cause there sure should be.")
#f.close()

#f = open("newsample.txt")
#text = f.readlines()
#print(text)
#f.close()

#So far, so good. This is just a revision.

f = open("newsample.txt")
lines = f.readlines()

#for line in lines:
    #line = line.replace("\n","")
    #print(line)
#This I think does not do as it does here: https://pythonspot.com/read-file/
#I don't know why.
import os
if not os.path.isfile("loremipsum.txt"):
    print("The file does not exist.")
else:
    with open("loremipsum.txt") as text:
        content = text.read().splitlines()
    for line in content:
        print(line),
#Tested with typo in the filename, works like a charm.