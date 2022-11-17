#First program
#print("Enter Name: ")
#name=input()
#if name == "Mary":
    #print("Hello, Mary. We have been waiting for you.")
    #print("Enter your password, Mary. ")
    #password=input()
    #if password == "Starfish":
        #print("You may enter.")
    #else:
        #print("You are not Mary.")
#else:
    #print(f"Hello, {name}. You cannot enter here.")

#Second program
#pretty_names=["Alice","Mary","Diddeldum"]
#name=input()
#if name in pretty_names:
    #print(f"Hi, {name}!")
#else:
    #print("What a name!")

#Third program
print("Hello. What's your name?")
name=input()
print(f"Hello, {name}. How old are you?")
age=input()
age=int(age)
if name == "Alice" and age == 27:
    print("Oh, hi Alice!")
elif age < 27:
    print("You are not Alice, kiddo.")
elif age >= 100 and age <= 1000:
    print("You are not Alice, granny.")
elif age > 1000:
    print("Impossible! Vampires do not exist!")
else:
    print("Okay, but this program is only for Alice.")