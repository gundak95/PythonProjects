f = open("C:/Users/MIIX/Gunda_Data/Python/PythonProjects/assignments/sample.txt","r")
contents = f.read()
print(contents)
#Why do I have to specify the whole path here? When I don't, it doesn't work.
#I am guessing that this cannot work once it is run from a different computer,
#so I would much prefer to use a relative path here.