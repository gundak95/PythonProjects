import re

txt = "There once was a ship that sailed to sea, and the name of the ship was the Bally O'Tea."
x = re.search(r"\bs\w+", txt, 2)

print(x.group())