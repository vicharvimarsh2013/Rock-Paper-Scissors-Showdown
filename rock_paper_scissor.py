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

#Write your code below this line 👇
outcomes=[rock,paper,scissors]
import random
computer=random.randint(0,2)
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(outcomes[user])
print("Computer chose:")
print(outcomes[computer])
if user==0 and computer==2:
  print("You win")
elif user==2 and computer==0:
  print("You lose")
elif user>computer:
  print("You win")
elif user<computer:
  print("You lose")

