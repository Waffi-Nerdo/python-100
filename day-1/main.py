print("Hello" + " Miami")

#input function will be replaced with the value provided to the prompt
#input()

lover=input("who is the love of your life? ")

print("so you're in love with " + lover ) 

#both function definitions below would create a funnction that would ask 
#for an input and return the length of that character.

def name_len():
    name = input()
    print(len(name))


def name_len():
    # name = input()
    print(len(input()))

#run the below to call the function
name_len()

#My version of the band name generator project
print("Welcome to the Band name Generator by Ife ")
street =input("what is the name of the steeet you grew up in?:\n")
pet = input("What is the name of your first pet:\n")
print("The name of your band can be " + street + " " + pet)

#Coding solution
print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)