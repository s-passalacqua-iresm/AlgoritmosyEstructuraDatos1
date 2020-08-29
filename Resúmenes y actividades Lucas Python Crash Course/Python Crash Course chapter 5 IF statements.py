#Conditional tests

car="subaru"
print(car=="audi") #check if the car is an audi(false, it's a subaru)

# Test using lower method: it doesn't change value: it's done for it to be true

name="John"
print(name.lower()=="john")

age1=18
print(age1==18) #test if age=18 (true)

age2=20
print(age2>=16) #check if age is greater than or equal to 16 (true, it's 20)

print(age1>8 and age2>19) # 2 conditions must be met to be true

print(age1>10 or age2>30) # just 1 condition must be met for it to be true

# Check if a value is in the list= IN

RequestedColours= ["red", "blue", "yellow", "green"] # LIST
print("brown" in RequestedColours) #false, brown isn't on the list
print("yellow" in RequestedColours) # true, yellow is on the list

# Check if a value isn't in the list= NOT IN

print("yellow" not in RequestedColours) #check if yellow isn't in the list: false: it is
print("black" not in RequestedColours) #check if black isn't in the list: true: it isn't

#Boolean Expressions = True or False (UsersCanEdit=False)

UsersCanEdit=False
AudioActive=True 

#EX 5.1- Conditional tests: create 10 conditional tests with predictions and messages

colour="red"
print("Is colour == red? I predict true")
print(colour=="red")

book="big"
print("Is the book == big? I predict false")
print(book=="small")

bottle="blue"
print("Is the bottle == blut? I predict true")
print(bottle=="blue")

movie="interesting"
print("Is the movie== interesting? I predict false")
print(movie=="boring")

colour="green"
print("Is colour == green? I predict true")
print(colour=="green")

house="big"
print("Is the house == big? I predict false")
print(book=="small")

dog="brown"
print("Is the dog == brown? I predict true")
print(dog=="brown")

kitchen="big"
print("Is the kitchen== big? I predict false")
print(kitchen=="small")

colour="pink"
print("Is colour == pink? I predict true")
print(colour=="pink")

phone="cheap"
print("Is the phone == cheap? I predict false")
print(phone=="expensive")

#EX 5.2: more conditional tests....

#Equality and inequality

bike="expensive"
print(bike=="expensive")

tv="nice" 
print(tv=="ugly")

# Test using lower method

name="John"
print(name.lower()=="john")

# Tests uncluding numbers and >, >=, <, <= + and/or

age3=25
age4=37
print(age3>=23 and age4>39)
print(age3<23 or age4<=37)

# Test if an item is/ isn't in a list

fruits=["banana", "apple", "orange"]
print("orange" in fruits)
print("watermelon" not in fruits)


# IF STATEMENTS Examples

cars=["audi", "bmw", "subaru", "toyota"] # = LIST

for car in cars: # =LOOP
    if car == "bmw": # = CONDITION = double = and :
        print(car.upper())
    else:     #on the contrary = same line as IF; don't forget the :
        print(car.title())  

# Not equal !=  !: not; =: equal

CarWanted="red"
if CarWanted != "blue":
    print("Give me the blue car")
else:
    print("I love this blue car!")

#Multiple conditions + ELSE

#and

salary=40000
if salary>=1000 and salary<=30000:
    print("You earn really well!")
else:
    print("Get a new job, man!")

#or + ELSE

Age=30
if Age>25 or Age>32:
    print("You are old enough to work in this company!")
else:
    print("Get a new job")

# IF-ELIF-ELSE chain= test more than 2 possible situations

age=18
if age<4:
    print("Your admission cost is $0")
elif age<18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# Multiple elif blocks = they are unlimited
# use price equaled to ages and then write a message: simpler and easier to modify and read
age=13
if age<4:
    price=0
elif age<12:
    price=10
elif age<=18:
    price=23
elif age<= 30:
    price=30
else:
    price=45
print(f"Your admission cost is $ {price}")

# Omitting ELSE: using another ELIF instead: more specific

age=13
if age<4:
    price=0
elif age<12:
    price=10
elif age<=18:
    price=23
elif age<= 30:
    price=30
elif age>30:
    price=45
print(f"Your admission cost is $ {price}")

# Multiple conditions with IF (no elif, no else)

ingredients=["onions", "tomatoes", "mushrooms"]

if "lettuce" in ingredients:
    print("Adding lettuce")
if "onions" in ingredients:
    print("Adding onions")
if "mushrooms" in ingredients:
    print("Adding mushrooms")
print("\n Your pizza is ready! Bon apetitte")

#EX 5.3- Alien Colours

AlienColours= ["green", "yellow", "red"]

if "green" in AlienColours:
    print("You've earned 5 points. Congrats!")

if "brown" not in AlienColours:
    print("You've earned 10 points. Congrats!")

#EX 5.4. Alien colours 2:

if "yellow" in AlienColours:
    print("You've earned 20 points!")
else:
    print("You've earned 50 points")

#EX 5.3. Alien colours 3:

alien="yellow"

if alien== "green":
    print("You've earned 5 points!")
elif alien=="yellow":
     print("You've earned 10 points!")
elif alien=="red":
    print("You've earned 25 points!")
else:
    print("You've earned 0 points.")

#EX 5.6: stages in life

age=30

if age<2:
    print("You are a baby")
elif age==2 or age<4:
    print("You are a toddler")
elif age==4 or age<13:
    print("You are a kid")
elif age==13 or age<20:
    print("You are a teengaer")
elif age==20 or age<65:
    print("You are an adult")
elif age>=65:
    print("you are an elder person")

# EX 5.7: Favourite fruit

FavouriteFruits=["orange", "banana", "apple"]

if "apple" in FavouriteFruits:
    print(" You love apples!")

if "watermelon" in FavouriteFruits:
    print("You love watermelons")

if "tangerine" not in FavouriteFruits:
    print("You don't like tangerines")

if "banana" in FavouriteFruits:
    print("You like bananas")

if "lemon" not in FavouriteFruits:
    print("Come on! You cannot like lemons!!")

# If statements + lists  (FOR + IF)

#There is no cheese to prepare pizzas

PizzaIngredients=["onions", "mushrooms", "cheese"] # List
for ingredient in PizzaIngredients:
    if ingredient=="cheese":
        print("Sorry, there is no cheese today")
    else:
        print(f"Adding {ingredient}")
print("Your pizza is ready now!")

# CHECKING IF LISTS AREN'T EMPTY (if + for + else)

Ingredients=[] # empty list

if Ingredients: # if there ARE ingredients in the list....
    for ingredient in Ingredients: #for each ingredient in the list....
        print("Adding {ingredient}")
    print("Your pizza is ready")
else:  # If there AREN'T any ingredients....
    print("Are you sure you want a plain pizza?") # There are NO ingredients

# MULTIPLE LISTS (for) + if/else statements

AvailableToppings=["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"] # this could be a tuple if it never changed

RequestedToppings=["mushrooms", "french fries", "extra cheese"]

for requestedtopping in RequestedToppings:
    if requestedtopping in AvailableToppings:
        print(f"Adding {requestedtopping}")
    else:
        print(f"Sorry, we don't have {requestedtopping}")
print("Your pizza is ready now!")

#EX 5.8- Hello Admin

Usernames=["Luke", "Anne", "Julia", "Peter", "Admin"]

for username in Usernames:
    if username == "Admin":
        print(f"Hello, {username}, would you like to see a status report?")
    else:
        print(f"Hello, {username}, thanks for logging in again")

# EX 5.9- No users

#Check if the previous list is empty

if Usernames:
    for username in Usernames:
        if username == "Admin":
            print(f"Hello, {username}, would you like to see a status report?")
    else:
        print(f"Hello, {username}, thanks for logging in again")
else:
    print("We must find some users!")        

# EX 5.10- Checking Usernames:

CurrentUsers=["Pepito", "Jaimito", "Love", "Moon", "Sun"]

NewUsers=["Star", "Love", "Sun", "Emperor", "jaimito"]

for newuser in NewUsers:
    if newuser in CurrentUsers:
        print(f"{newuser}, you will need to enter a new username, since yours already exists")
    else:
        print(f"{newuser} is available!")

# Carry out a case-sensitive comparison:

CurrentUsers=["Pepito", "Jaimito", "Love", "Moon", "Sun"]

NewUsers=["Star", "Love", "Sun", "Emperor", "jaimito"]

currentuserslowercase=CurrentUsers[:] # copy list

for newuser in NewUsers:
    if newuser in currentuserslowercase:
        print(f"{newuser.lower()}, you will need to enter a new username, since yours already exists")
    else:
        print(f"{newuser.lower()} is available!")

#EX 5.11: Ordinal numbers:

Numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in Numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("\n2nd")
    elif number == 3:
        print("\n3rd")
    elif number == 4:
        print("\n4th")
    elif number == 5:
        print("\n5th")
    elif number == 6:
        print("\n6th")
    elif number == 7:
        print("\n7th")
    elif number == 8:
        print("\n8th")
    elif number == 9:
        print("\n9th")   