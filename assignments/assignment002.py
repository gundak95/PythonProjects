alternative_names = ["Fabian","Fabi","Fabian Krautgasser","Krauthex","Krautgasser"]

while True:
    name=input("What is your name? ")
    if name == "Fabs":
        x=True
        print(f"{name} is absolutely the name by which I know you.")
        break
    else:
        if name in alternative_names:
            print(f"Hm, I remember you being called something else than {name}.\n")
        else:
            print(f"Are you sure that {name} is your name?\n")












age=input("How old are you? ")
age=int(age)

if age == 27: 
    print ("Since {} squared is {}, I can tell that it is your birthday soon.".format(age,age**2))
else:
    print ("What? You don't look it at all!")