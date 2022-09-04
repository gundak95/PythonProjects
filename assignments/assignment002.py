alternative_names = {
    "Fabian","Fabi","Fabian Krautgasser","Krauthex","Krautgasser",
}

name=input("What is your name? ")

if name == "Fabs":
    print(f"{name} is absolutely the name by which I know you.")

for name in alternative_names:
    print(f"Hm, I remember you being called something else than {name}.")


else:
    print(f"Are you sure that {name} is your name?")

    
#if name == "Gunda"
    #break

age=input("How old are you? ")
age=int(age)

if age == 27: 
    print ("Since {} squared is {}, I can tell that it is your birthday soon.".format(age,age**2))
else:
    print ("What? You don't look it at all!")