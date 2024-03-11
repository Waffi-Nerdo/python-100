# Randomization Document link - https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences


import random


# to randomly select heads or tail 
a = ['Heads', 'Tails']

for i in range(1):
    print(random.choice(a))

# by assigning heads to 0 and tails to 1
random_number = random.randint(0, 1)

if random_number == 0:
  number = "Tails"
else:
  number = "Heads"
  
print(number)


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])

# 0 is the first and -1 is the last item on the list

# learn append and extend

# other examples of randomization

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

import random

items_no = len(names)

random_names = random.randint(0, items_no - 1)

who_pays = names[random_names]

print(f"{who_pays} is going to buy the meal today!")


# Understanding nested lists.
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

list_1 = ["Strawberries", "Spinach", "Kale", "Nectarines"]

list_2 = ["Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

new_list = [list_1, list_2]

# understanding how to index nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])


print(dirty_dozen[0])
print(dirty_dozen[1])


print(dirty_dozen[1][2])
print(dirty_dozen[1][3])


# practice more 
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")


# Rock Paper Scissors Game
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("Number provided is outside the given range")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")