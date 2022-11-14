#word = input("What are you looking for? ")
with open('loremipsum.txt', 'r') as text:
   # for line in text:
    #    line = line.lower()
    if word("ipsum") in text:
        print("Found it!")
        break
    else:
        print("This isn't here.")
#This works now. The search is case sensitive.
#How can I make it case insensitive??
#Managed to capitalize input, but then it capitalises every input and does not find lower-case words.
#I can't seem to manage. This really starts to bother me.
#It worked and I ruined it again.