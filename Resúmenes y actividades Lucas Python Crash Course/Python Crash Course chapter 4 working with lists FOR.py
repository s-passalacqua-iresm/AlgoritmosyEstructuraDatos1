# EXAMPLE For every magician in the list of magicians, print the magician's name
magicians= ["Alice", "David", "Carolina"]
for magician in magicians: #magicians= list; magician=new variable= use singular (variable) and then plural (list)
    print(f"{magician.title()}, that was an awesome trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank, everyone. That was a great magic show!")
#here we wrote 2 differente messages within the loop; at the end we wrote \n to skip a line between each magician
#The 3rd print has diferent indentation: loop is over: that print will be executed just once

#EX 4.1- Pizzas

# Create a list with 3 kinds of pizza. Use a for loop to print the name of each pizza
#Then create a message and a final message without looping

Pizzas=["onion","garlic","jam"]
for pizza in Pizzas:
    print(f"\n I love {pizza} pizza \n")
print("I am a truly pizza lover!")

# 4.2: Animals

# Think of 3 similar animals and print each name.
# print a statement for each one + add a final line without looping

Animals=["dog", "cat", "turtle"]
for animal in Animals:
    print(f" \n A {animal} is a great pet \n")
print("Any of these animals would be a great pet!")

#range() function: generate a series of numers

for animal in range(1, 4): # I must write one more number than I want: If I want 3, I must write 1-4
    print(animal)

#list() function= it calls range() function: to convert numers into a list

numbers=list(range(1, 6))
print(numbers)

#skipping numbers in list and range () functions:
# there are 3 arguments in range: 1st: starting point; 2nd: finishing point; 3rd: skipping

EvenNumbers=list(range(2, 12, 3)) # starts in 2, finishes in 12, it skips 3 places each time it changes
print(EvenNumbers)

#Make a list of the first 10 square numbers= 

squares=[] #the list starts empty: squares in plural since it's a list
for number in range(1, 11): #As I want from 1-10, I must add 1 more: up to 11
    square=number**2 # square  singular: each element in squares list
    squares.append(square) # Each new value of square  is added (appended) to the list: squares (plural)
#or just: squares.append(number**2): replace square by number**2
print(squares) # when the loop finishes, this is printed

# List comprehensions: how to do the same than before but in just 1 line using loop

squares=[number**2 for number in range (1, 11)] # squares is the list: elevate each number FOR number IN RANGE (....)
print(squares)


# Simple statistics with numbers

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min(numbers) # selects the minimum number from the list
max(numbers) # selects the maximum number from the list
sum(numbers) # sums all the numbers in the list

#EX 4.3 Counting to twenty: loop to print numbers from 1 to 20

for number in range (1, 21):
    print(number)

#EX 4.4 One Million: make a list of numbers 1-1 million + loop to print them

numbers=list(range(1, 1000001))
#print(numbers)

#EX 4.5 SUmming a Million:  make a list 1-1 million and use functions MIN, MAX and SUM

numbers=list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#EX 4.6- Odd numbers: use 3rd argument range () function to make list form 1-20. Use loop to print them

Odd_numbers=list(range(1, 21, 2))
print(Odd_numbers)

#EX 4.7. Threes: Make list of multiples of 3 from 3 to 30. Use loop to print them

ThreesMultiples=list(range(3, 31, 3))
print(ThreesMultiples)

#EX 4.8. Cubes: Make a list of the first 10 cubes and use loop to print them

Cubes=[]
for number in range (1, 11):
    cube=number**3
    Cubes.append(cube)
    print(Cubes)

#EX 4.9.: Cube comprehension: generate list of first 10 cubes

cubes=[number**3 for number in range (1, 11)]
print(cubes)

#Slicing lists: specify index of elements you want to work with

Colours= ["red", "black", "white", "yellow", "green"]
print(Colours[0-2]) #index starts in 0, not in 1

#Omitting the first index, you start at the beginning
print(Colours[:4])

#Omitting the second index, you start from first index up to the end of the list
print(Colours[2:])

#Recalling negative index and omitting second index:

print(Colours[-2:]) # This calls just the last TWO colours

#Looping through a slice= it doesnt loop the whole list: just a SLICE of it

print(" Here are the first colours on the list:")
for colour in Colours[:3]: # the first 3 colours
    print(colour.title())

# Copying a list: slicing original list by omitting 1st and 2nd index:  ([:)])

MyFoods=["pizza", "falafel", "carrot cake"] #create a  list
FriendsFood=MyFoods[:] #I slice the original list and assign it to a new one

# It is relevant to include [:] : no indices, if not, both lists will be the same

print(f"My favourite foods are {MyFoods}")
print(f"My friends' favourite foods are {FriendsFood}")

#example to show they are now independant lists:

MyFoods.append("rice")
FriendsFood.append("couscous")
print(MyFoods)
print(FriendsFood)

# If both lists are just equalled to 0 and the [:] isn't written, both lists will be the same

#EX 4.10. Slices: slice your list: 3 initial/ 3 middle/ 3 end

Countries=["Argentina", "Spain", "Greece", "England", "Canada", "Ireland", "Germany", "France", "Turkey"]

#Slice first 3 countries
print(f"The first 3 countries are: {Countries[0:3]}")

#Slice 3 ountries in the middle
print(f"The 3 countries in the middle are: {Countries[3:6]}")

#Slice 3 last items
print(f"The last 3 countries are: {Countries[6:9]}")

#4.11: My pizzas, your pizzas: Copying lists
FriendPizzas=Pizzas[:]

#Add a new pizza to old and new list ad print messages showing they are different

FriendPizzas.append("Cheese")
Pizzas.append("Vegetables")

print(f"My favourite pizzas are: {Pizzas}")
print(f"My friends' favourite pizzas are: {FriendPizzas}")

#4.12: More loops: choose one list and write 2 loops

for mypizza in Pizzas:
    print(f"My favourite pizza is: {mypizza}")
print("I love them all!")

for theirpizza in FriendPizzas:
    print(f"Their favourite pizza is: {theirpizza}")
print("I like them as well!")

#Tuples: create a list of items which cannot be changed

TriangleDimensions=(200, 50) # Brackets (), not square brackets  []
print(TriangleDimensions [0])  # access items by index
print(TriangleDimensions [1])

#Looping in tuples = same as doing it with lists

for dimension in TriangleDimensions:
    print(dimension)

# Writing over tuples: you can't modify them, but you can assign new values to variables (replace them)

dimensions=(200, 50)
print("Original dimensions")
for dimension in dimensions:
    print(dimension)

dimensions=(400, 100) # these will replace the old ones
print("\n New dimensions")
for dimension in dimensions:
    print(dimension)

#EX 4.13: Buffet

#Store 5 foods in a tuple () and use loop to print each

Foods=("Lasagna", "Meat", "Chicken", "Pork", "Salmon")
for Food in Foods:
    print(Food)

#Try to change one and see how Python rejects this:

#Foods["Pork"]="Eggs"
#print(Foods)

#Replace 2 items and print all the food names

Foods=("Lasagna", "Meat", "Chicken", "Potatoes","Fish")
for Food in Foods:
    print(Food)

# Styling your code: PEP 8 : 
# Indentation: use 4 spaces per indentation level 
# # Use less than 80 characters per line
# Use black lines to better organize your code, but no in excess

#EX 4.14 and 4.15: Read PEP 8 and make one code review based on PEP 8

#It's all OK
