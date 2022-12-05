import random

def travelDestination(answerNumber):
    if answerNumber == 1:
        return "Sicily"
    
    if answerNumber == 2:
        return "Rome, then Sicily."
    
    elif answerNumber == 3:
        return "First Naples, then Sicily."
    
    elif answerNumber == 4:
        return "definitely Sicily."

r = random.randint(1,5)
plan=travelDestination(r)