print("Enter Name: ")
name=input()
if name == "Mary":
    print("Hello, Mary. We have been waiting for you.")
    print("Enter your password, Mary. ")
    password=input()
    if password == "Starfish":
        print("You may enter.")
    else:
        print("You are not Mary.")
else:
    print(f"Hello, {name}. You cannot enter here.")
