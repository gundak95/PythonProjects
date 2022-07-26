import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("We have a match!")
else:
    print("Not found.")