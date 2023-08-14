# rules taken from https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
#Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]
print("Choices  \n 0 for Rock \n 1 for Paper \n 2 for scissors\n")
human=int(input("Enter your choice:- "))
if human >=3 or human < 0:
    print("You Entered invalid number,You Lose")
else:
    print(image[human])

    ai = random.randint(0,2)

    print(image[ai])

    if human == 0 and ai == 2:
        print("You won ")
    elif ai == 0 and human == 2:
        print("You Lose")
    elif ai > human:
        print("You Lose")
    elif human > ai:
        print("You won")
    elif ai == human:
        print("Draw match")
