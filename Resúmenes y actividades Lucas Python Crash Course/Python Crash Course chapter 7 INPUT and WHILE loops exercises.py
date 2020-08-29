# input() function:   variable=input("Question") ; print("...", variable)

age=input("How old are you?")
print("I am ", age)

#Every time a number is written with input, it becomes a string. 
# int() function: converts string into integer to operate with numbers written with input

age=int(age) #convert age: from string (input) to integer: int(variable name)

print(age>=18) #check if inserted age is >= 18

#Another example:

Height=input("How tall are you, in inches?")
Height=int(Height)

if Height >= 18:
    print("\n Congrats! You are tall enough to ride")
else:
    print("You aren't tall enough to ride")

#Modulo operator: % = it divides 2 numbers and gives the remainder

print("If you divide 4 by 3, the remainder is: ", 4%3)

#Check if number is even (divisible by 2) or odd (else: divisible by 1)

number=input("Write a number and I'll tell you whether it's even or odd: ")
number=int(number)

if number % 2 == 0: #if number divided by 2 gives 0 as remainer, then..
    print(f"Number {number} is an even number")
else:
    print(f"Number {number} is an odd number")

# EX 7.1. Rental car

rentalcar=input("What kind of rental car would you like?")
print(f"Let me see if I can find you a {rentalcar}")

# EX 7.2. Restaurant seating

dinnergroup=input("How many people are there in your dinner group?")
dinnergroup=int(dinnergroup)

if dinnergroup > 8:
    print("You'll have to wait for a table because there are more than 8 people in your dinner group")
else:
    print("Your table is ready, since there are 8 or less people in your dinner group")

# EX 7.3. Multiples of 10

askednumber=input("Write any number of your interest: ")
askednumber=int(askednumber)

if askednumber % 10 == 0:
    print(f"The number you've written -number {askednumber}- is divisible by 0")
else:
    print(f"The number you've written -number {askednumber}- isn't divisible by 0")

# While loops: run as long as or while a certain condition is true
#VS for loops: take a collection of items and execute code once for each item in the collection

# While loops: counting from 1 up to 5

currentnumber=1

while currentnumber <=5:
    print(currentnumber)
    currentnumber+=1   # or: currentnumber=currentnumber+1 (counting numbers)

#Choosing when to quit:

message= "" #it starts empty and then it's completed

while message != 'quit':
    message=input("Tell me something, and I will repeat it back to you: . \n You can enter 'quit' to end the programme")
    print(message)

    if message != 'quit':
        print(message)


