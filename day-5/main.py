# Using loops to determine the average heights of students
# Sample inputs 151 145 179
student_heights = input().split()

new_student_heights = [int(num) for num in student_heights]

total_height = sum(new_student_heights)

print(f"total height = {total_height}")

number_students = len(new_student_heights)

print(f"number of students = {number_students}")

average_height = total_height / number_students

whole_average_height = float(round(average_height, 0))

print(f"average height = {whole_average_height}")

# Input a Python list of student heights 100 days of code

student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")


# return the highest number 100 days of code
# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score # you're reassigning score here to the highest score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")

# My solution
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

student_scores.sort() # sort function sorts the items in the list in ascending order.

print(f"The highest score in the class is: {student_scores[-1]}")


# calculate the sum of even numbers within the range of 1 and the input
target = int(input("Enter a number: "))
even_numbers = []

for number in range(1, target + 1):
    if number <= 1000 and number % 2 == 0:
        even_numbers.append(number)

sum_even_numbers = sum(even_numbers)

print("Sum of even numbers:", sum_even_numbers)

#100 days
target = int(input()) # Number between 0 and 1000
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# FizzBizz game, it is funny I arrived at the same answer
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for item in range(1, nr_letters + 1):
	password.append(random.choice(letters))


for item in range(1, nr_symbols + 1):
	password.append(random.choice(symbols))


for item in range(1, nr_numbers + 1):
	password.append(random.choice(numbers))

# easy way is to print password
print(password)
 # hard way is to randomize password list 
random.shuffle(password)

print(password)

password_str = ""
for item in password:
	password_str += item
print(f"Your new password is: {password_str}")
