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

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
elif player_choice == "2":
    print(scissors)

rps = [rock, paper, scissors]
computer_choice = random.randint(0,len(rps)-1)
print("Computer choose:\n")
print(rps[computer_choice])

if int(player_choice) == computer_choice:
    print("Draw")
elif int(player_choice) == 0:
    if computer_choice == rps[1]:
        print("You lose")
    else:
        print("You win")
elif int(player_choice) == 1:
    if computer_choice == rps[2]:
        print("You lose")
    else:
        print("You win")
elif int(player_choice) == 2:
    if computer_choice == rps[0]:
        print("You lose")
    else:
        print("You win")