f = open("sample.txt","a")
f.write("Append")
f.close()

f = open("sample.txt")
print(f.read())
#Why do I have to specify the whole path here?
#Answer: Because somehow the terminal was running from a different folder.
#Fixed it, but did not really understand why it was happening.

#I now understand that when I overwrite a file, it is permanently changed.
#By changing "w" to "a", I do not get the original dolor sit amet back.