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

me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if me >=3 or me < 0 :
  print("You choose an invalid number. You lose!")
else:
  rock_paper_scissors = [rock, paper, scissors]
  my_turn = rock_paper_scissors[me]
  computer_turn = rock_paper_scissors[computer]

  if me == 0 :
    print(my_turn)
    if computer == 2:
      print(f"Computer chose:\n{computer_turn}")
      print("You win!")
    elif computer == 1:
      print(f"Computer chose:\n{computer_turn}")
      print("You lose!")
    else:
      print(f"Computer chose:\n{computer_turn}")
      print("Draw")
  elif me == 1 :
    print(my_turn)
    if computer == 0:
      print(f"Computer chose:\n{computer_turn}")
      print("You win!")
    elif computer == 2:
      print(f"Computer chose:\n{computer_turn}")
      print("You lose!")
    else:
      print(f"Computer chose:\n{computer_turn}")
      print("Draw")
  else:
    print(my_turn)
    if computer == 1:
      print(f"Computer chose:\n{computer_turn}")
      print("You win!")
    elif computer == 0:
      print(f"Computer chose:\n{computer_turn}")
      print("You lose!")
    else:
      print(f"Computer chose:\n{computer_turn}")
      print("Draw")
