total=0
for num in range(101):
    total=total+num
print(total)

#Be sure to include (number you want)+1, because 0 also counts as the first integer.
#Tried it and range(100) gives a wrong result.

i=0
print('My name is ')
while i<5:
    print ('Five times Jim.')
    i=i+1

print('My name is')
for i in range(5):
    print('Five times Jim.')

print('Machine, count to 50 in steps of seven starting at 1!')
for i in range(1,51,7):
    print(i)

#Keep in mind that it starts at the starting number, but stops one number BEFORE the stopping number.

#To count down:

for i in range(10,0,-1):
    print(i)
