word = input("What are you looking for? ")

with open('loremipsum.txt', 'r') as text:
    if word in text.readline().lower():
        print("Found it!")
    else:
        print("This isn't here.")
#This works now. The search is case sensitive.
#How can I make it case insensitive??
#Managed to capitalize input, but then it capitalises every input and does not find lower-case words.
#I can't seem to manage. This really starts to bother me.
#It worked and I ruined it again.
#Got it to work again. It also looks for parts of the word. I would like to be able to fix this.