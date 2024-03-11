## Control Flow and Logical Operators

# Which number do you want to check?
number = int(input("what number do you want to check? "))

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
else:
	print("This number is an odd number")

#nested in coding means that there is the same code structure below the actual code.
height = int(input("How tall are you? "))
bill = 1
if height >= 120: 
	print("you can ride the rollercoaster")
	age = int(input("How old are you? "))
	if age < 12:                     #from line 15 to 20. That is what nested in coding means.sd
		bill = 5
	elif age >= 12 and age <= 18: 
		bill = 7
	else:
		bill = 12

	want_photo = input("Do you want a photo, enter Y or N: ")
	if want_photo == "Y":
		bill += 3
		print(f"Your total bill is {bill}")
	else: print(f"Your final bill is {bill}")   
else:
  print("sorry, you have to grow taller for this ride.")
  

# Leap Year calculator
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


# Pizza Order Practice
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

price = 0 
if size == "S":
  price = 15
elif size == "M":
  price = 20
elif size == "L": 
  price = 25 

if add_pepperoni == "Y" and size == "S" or size == "M":
    price += 2 
elif add_pepperoni == "Y" and size == "L":
   price += 3 

if extra_cheese == "Y":
   price += 1

print(f"Your final bill is: ${price}")


# Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()

# count the number of times the letters in the word "true" occur in the combination of both names
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_no = t + r + u + e

# count the number of times the letters in the word "love" occur in the combination of both names
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_no = l + o + v + e

combined_no = int(str(first_no)+ str(second_no))

if combined_no < 10 or combined_no > 90:
    print(f"Your score is {combined_no}, you go together like coke and mentos.")
elif combined_no >= 40 and combined_no <= 50:
    print(f"Your score is {combined_no}, you are alright together.")
else:
    print(f"Your score is {combined_no}.")


#                /'.    .'\
#                \( \__/ )/
#          ___   / (.)(.) \   ___
#     _.-"`_  `-.|  ____  |.-`  _`"-._
#  .-'.-'//||`'-.\  V--V  /.-'`||\\'-.'-.
# `'-'-.// ||    / .___.  \    || \\.-'-'`
#       `-.||_.._|        |_.._||.-'
#                \ ((  )) /
#                 '.    .'
#                   `\/`

print("Welcome to Island Rush: The number one game in 2024.\nThe motive for this game is to try to stay alive")

start = input("Where would you like to start, the bedroom or the living room? ")

# if "living" in start:
#     print("game over")

# elif: 
