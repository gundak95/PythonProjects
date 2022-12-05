#Write code that prints Hello if 1 is stored in spam,
#prints Howdy if 2 is stored in spam,
#and prints Greetings! if anything else is stored in spam.

spam = input()

if spam == "1":
    print ("Hello")
elif spam == "2":
    print ("Howdy")
else:
    print ("Greetings!")

#Write a short program that prints the numbers 1 to 10
#using a for loop.
#Then write an equivalent program that prints the numbers 1 to 10
#using a while loop.


for number in range(1,11):
    print(number)

number=1
while number <11:
    print(number)
    number=number+1