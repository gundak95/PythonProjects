import sys
while True:
    print('Type anything to continue. Type exit to exit.')
    anything=input()
    print(f'You typed {anything}.')
    if anything == "exit":
        sys.exit()
#I have to remember that when the program is buggy despite the code
#being correct, it is quite likely I have not terminated the
#current run of the old code.