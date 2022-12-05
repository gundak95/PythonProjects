import random

def travelDestination(answerNumber):
    if answerNumber == 1:
        return "Sicily"
    
    elif answerNumber == 2:
        return "Rome, then Sicily."
    
    elif answerNumber == 3:
        return "First Naples, then Sicily."
    
    elif answerNumber == 4:
        return "definitely Sicily."

r = random.randint(1,4)
#Why does this work? Should I not define 1,5 here?
plan=travelDestination(r)
print(plan)

def spam():
    print(eggs)
eggs = 42
spam()
#print(eggs) Book has this unnecessary additional line.