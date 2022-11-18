import random, sys
positive_answers = ['y','yes','Yes','Y']
negative_answers = ['n','no','No','N']
quit = ['q', 'quit']

possibilities = ['rock','r'],['paper','p'],['scissors','s']

print('Wanna play a game of rock, paper, scissors? y/n')


while True:
    answer = input()
    if answer in negative_answers:
        print('Okay, boring. Bye!')
        sys.exit()
    elif answer in positive_answers:
        print("Okay, let's go!")
        break
    else:
        print('Please give a valid answer.')

print('Remember: you can quit anytime by typing "q".')

#So when I break the loop when player and machine choose the same weapon it goes back without
#counting the instance for the for-loop:

#loop for a game (3 goes):
game = 0
wins= 0
losses = 0

for games in range(3):

    machine_choice = random.randint(1,3)
    if machine_choice == 1:
        machine_choice = possibilities[0][0]
    if machine_choice == 2:
        machine_choice = possibilities[1][0]
    if machine_choice == 3:
        machine_choice = possibilities[2][0]

    print('Choose your weapon. ')
    weapon = input()
    #when player chooses rock
    if weapon in possibilities[0] and machine_choice in possibilities[1]:
        print('Rock against...')
        print(machine_choice)
        print('You lose.')
        losses=losses+1
        

    if weapon in possibilities[0] and machine_choice in possibilities[2]:
        print('Rock against...')
        print(machine_choice)
        print('You win.')
        wins=wins+1
    

    if weapon in possibilities[0] and machine_choice in possibilities[0]:
        print('Rock against...')
        print(machine_choice)
        print('Go again.')
        break


    #when player chooses paper
    if weapon in possibilities[1] and machine_choice in possibilities[2]:
        print('Paper against...')
        print(machine_choice)
        print('You lose.')

    if weapon in possibilities[1] and machine_choice in possibilities[0]:
        print('Paper against...')
        print(machine_choice)
        print('You win.')

    if weapon in possibilities[1] and machine_choice in possibilities[1]:
        print('Paper against...')
        print(machine_choice)
        print('Go again.')
        continue

    #when player chooses scissors
    if weapon in possibilities[2] and machine_choice in possibilities[0]:
        print('Scissors against...')
        print(machine_choice)
        print('You lose.')

    if weapon in possibilities[2] and machine_choice in possibilities[1]:
        print('Scissors against...')
        print(machine_choice)
        print('You win.')

    if weapon in possibilities[2] and machine_choice in possibilities[2]:
        print('Scissors against...')
        print(machine_choice)
        print('Go again.')
        continue

print("Wanna play again?")
answer=input()
if input == 'yes':
    input = 'yes'
if input == 'no':
    input = 'yes'

#Okay, if I want this not to count the times when both machine and player choose the same
#weapon, I will have to rethink it.