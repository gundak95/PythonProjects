#while True:
#    print("Enter your name, gnome!")
#    name = input()
#    if name == "Gundibor":
#        break
#    print("Psh, you are the wrong gnome and just broke your computer.")


#print('Hello, Gundibor.')
#password=''
#while password != '1234':
#    print("Enter your password.")
#    password = input()
#    print('Wrong! Go back to the cave from which you crawled, impostor.')

#print('You are the real Gundibor and may enter.')

#while True:
#    print('Now that I know who you are, tell me your secret.')
#    secret=input()
#    if secret != 'I am only a half-gnome.':
#        continue
#    print('I can tell.')

#Bit of redundancy still left, will fix next time.
#This is basically two ways of doing the same thing. Either I break the loop when
#a certain condition is met or I repeat the loop as long as a certain condition is
#not met.
#Three ways of doing the same thing. Doesn't make sense logically (yet), but the code is okay.

#name = ''
#while name != 'your name':
#    print('Please type your name!')
#    name = input()
#print('Thank you.')
#Order is important. (Didn't get it right at first try.)
#First use of an empty string! Didn't get how they worked before, very useful!

#For Truthy and Falsey values:

name = ''
while not name:
    print('Please enter your name: ')
    name=input()

print('How many guests do you expect?')
number_of_guests=int(input())
if number_of_guests:
    print ('Shalala.')
else:
    print ('How sad.')

