mylist = [1, 2, 3]
print(mylist)
myotherlist = mylist
myotherlist[0] = 5
print(myotherlist)

#I have a list of numbers.
# The numbers are 1, 2, and 3.
# I make another list, which is identical to the first one since I tell it to use the numbers it finds there.
#Then, however, I tell it that for this second list, the first number is 5.
#What I get when I print both lists is two times the same: 5, 2, and 3.
#The reason for this must be that Python thinks when I say myotherlist is mylist,
#then I mean that also mylist is myotherlist. This is a shallow copy.
#Changes to any one of them will cause changes in both.
#In this simple example, to change this behaviour, I can tell it to print mylist before I say that myotherlist is essentially the same, see above.

mylist = ["apples", "pears", "grapes"]
print("List for store A", mylist)
myotherlist = mylist
myotherlist[0] = "peaches"
print("List for store B", myotherlist)
#This change of behaviour could be useful when I have different items, e.g. fruits.
#Say, I have a list of fruits that is the same in stores, but in one of them,
#the customers love peaches. I will then always get peaches for them and replace the
#first other fruit on the list.

