from copy import copy


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
#then I mean that also mylist is myotherlist.
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

import copy
mylist = ["apples", "pears", "grapes"]
myotherlist = copy.copy(mylist)
myotherlist.append(["peaches", "plums", "mangoes"])
print("My List", mylist)
print("My Other List", myotherlist)

#I found a nice tutorial for copies in python, so from the example above on,
#this is not something I knew before or came up with off the top of my head.
#Making a copy of the list instead of telling python that the lists are identical
#allows me to alter one of the lists while leaving the other intact.
#I added some items to the new list, but not the old one.

import copy
mylist = [["apples", "pears", "grapes"],["flour", "noodles", "rice"]]
myotherlist = copy.copy(mylist)
mylist[0][1] = 'bananas'
myotherlist.append(["courgettes", "celery", "potatoes"])

print("My List", mylist)
print("My Other List", myotherlist)

#This took me forever, because I could not figure out the missing comma between
#"grapes"] and ["flour", but it works now. I replaced pears with bananas in both lists and added
#vegetables only to the second.
#I also found out that this [0][1] goes from big to small, i.e. this is the second of the first,
#the pears of the fruits, not the first of the second, the flour of the staple foods.