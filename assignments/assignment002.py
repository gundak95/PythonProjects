import copy
mylist = [["apples", "pears", "grapes"],["flour", "noodles", "rice"]]
myotherlist = copy.copy(mylist)
mylist[0][0] = 'bananas'
myotherlist.append(["courgettes", "celery", "potatoes"])

print("My List", mylist)
print("My Other List", myotherlist)

#This took me forever, because I could not figure out the missing comma between
#"grapes"] and ["flour", but it works now. I replaced apples with bananas in both lists and added
#vegetables only to the second.