#Data types

#string
# remember each character starts with 0. using [] is call subscripting
print("Hello"[0]) 

#you can combine/concatenate strings using + same as the lesson in Day 1

# Number data type is called an Integer (this refer to both positive and negative numbers). TO declare a data type you just write the number with nothing else
print(123_456_700) #pyhton has the ability to spit out the value without the underscore. This aids readabilty and also mimicks 123,456.700

# Floats are numbers with decimal places lie 3.141

#Boolean - True or False

#you can concatenate strings and numbers. Basically you can concatenate/combine different data types together.

#check the type of the data using type() function

#type conversion of a data type to another is mosttimes called type casting.  

#class examples

num = len(input("what is your name? "))

convert_num_to_string = str(num)

print("the lenght of characters in your name is " + convert_num_to_string )

#Other conversion functions str(), float(), int()

print(int("234"))


#This code adds the first 2 letters of an integar 
two_digit_number = input("Please enter your 2-digit numbers here: ")

first_number = int(str(two_digit_number[0]))
second_number = int(str(two_digit_number[1]))

add_both_nums = first_number + second_number

print(add_both_nums)

#The above code as a function 
def add_two_digits():
    two_digit_number = input("Please enter a two-digit number: ")
    if len(two_digit_number) != 2 or not two_digit_number.isdigit():
        print("Please enter exactly two digits.")
        return
    first_number = int(two_digit_number[0])
    second_number = int(two_digit_number[1])
    add_both_nums = first_number + second_number
    print(add_both_nums)

# Call the function to execute it
add_two_digits()


#division in python returns the division of integars as a float.
intek = 6 / 3
print(intek)

print(type(6 / 3))

# Order of executing functions in your code 
# PEMDAS or PEMDASLR - LR denoting that code is processed from left to right.
# Parenthesis () , Exponents **, Multiplacation *, Divisions /, Addition +, Subtraction - 
# * and /, + and - , both are equally important. The computer exsicutes it from left to right.

#Debug in Thorny

print(6 + 4 / 2 - (1 * 2))

# Division  of any number would result in a float

print(int(5.67))


print(57 / 1.58 * 1.58)


# There are 2 Fs . One is used in making the string have embedded expressions in side denoted by {}
# The second is used for formatting. {bmi.}
# BMI calculation
# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input())

bmi = weight / (height ** 2)
print(round(int(bmi)))

# tip calculator
print("welcome to the Tip calculator")
total_bill = (float(input("what was the total bill? ")))

percent = (float(input("what percentage of tip would you like to give? 10, 12 or 15? ")))

percentage = percent / 100

whole_percentage = 1 + percentage

people = float(input("How many people will split the bill? "))

bill_plus_tip = total_bill * whole_percentage

each_pay = round(bill_plus_tip / people, 2)

print(f"Each person should pay: {each_pay}")


#tip calculator function
def tip_calculator():
    print("welcome to the Tip calculator")
    total_bill = (float(input("what was the total bill? ")))

    percent = (float(input("what percentage of tip would you like to give? 10, 12 or 15? ")))

    percentage = percent / 100

    whole_percentage = 1 + percentage

    people = float(input("How many people will split the bill? "))

    bill_plus_tip = total_bill * whole_percentage

    each_pay = bill_plus_tip / people

    print(f"Each person should pay: {each_pay}")


tip_calculator()  