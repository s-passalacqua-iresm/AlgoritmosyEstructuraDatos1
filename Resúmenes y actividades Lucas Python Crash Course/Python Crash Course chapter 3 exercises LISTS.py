# EX 3.1 Names: print 3 friends' names and access each one

Friends=["Cecilia", "Facundo", "Silvina"]

print(Friends[0])
print(Friends[1])
print(Friends[2])

# EX 3.2 Greetings: Send a message to each friend in EX 1

print(f"{Friends[0]} hey, hi, how are you today?")
print(f"{Friends[1]} hey, hi, how are you today?")
print(f"{Friends[2]} hey, hi, how are you today?")

# EX 3.3 Your own list: list with means of transport + statements about them

MeansOfTransport=["Car", "Bus", "Ship", "Plane", "Train", "Bike"]

print(f"The {MeansOfTransport[0]} is the best means of transport")
print(f"The {MeansOfTransport[1]} is the cheapest means of transport")
print(f"The {MeansOfTransport[2]} is the most interesting means of transport")
print(f"The {MeansOfTransport[3]} is the fastest means of transport")
print(f"The {MeansOfTransport[4]} is the most comfortable means of transport")
print(f"The {MeansOfTransport[5]} is the coolest means of transport")






# EX 3.4- Guest list

# Create guests list 

GuestsList=["Cecilia", "Mariano", "Noelia", "Facundo", "Pepi"]
print(GuestsList)

# Invite them to dinner using the list

print(f"{GuestsList[0]} you have been invited to dinner")

print(f"{GuestsList[1]} you have been invited to dinner")

print(f"{GuestsList[2]} you have been invited to dinner")

print(f"{GuestsList[3]} you have been invited to dinner")

print(f"{GuestsList[4]} you have been invited to dinner")

# 3.5. Changing guest list

# Say who can't make it

print(f"The guest who can't make it is: {GuestsList[-1]}")

# Change: replace guest who can't make it by another one and print new list

GuestsList[-1]="Fede" # change Pepi for Fede
print(f"{GuestsList[-1]} you have now been invited to dinner")

# New invitations....

MessageFinalInvitation="The guests to dinner are:  " + str(GuestsList)
print(MessageFinalInvitation)

print(f"{GuestsList[0]} you are still invited to dinner")

print(f"{GuestsList[1]} you are still invited to dinner")

print(f"{GuestsList[2]} you are still invited to dinner")

print(f"{GuestsList[3]} you are still invited to dinner")

print(f"{GuestsList[4]} you are now invited to dinner")

# 3.6 More guests.... Add 3 more guests....: beginning/middle/end

print("There will be 3 more guests to dinner, since there is an extra table")

GuestsList.insert(0, "Silvina") #beginning
GuestsList.insert(2, "Marina") #middle
GuestsList.append("Coni") #end

#New invitations for each person

MessageRealFinalInvitation="The guests to dinner are:  " + str(GuestsList)
print(MessageRealFinalInvitation)

print(f"{GuestsList[0]} you are invited to dinner")

print(f"{GuestsList[1]} you are invited to dinner")

print(f"{GuestsList[2]} you are invited to dinner")

print(f"{GuestsList[3]} you are invited to dinner")

print(f"{GuestsList[4]} you are  invited to dinner")

print(f"{GuestsList[5]} you are  invited to dinner")

print(f"{GuestsList[6]} you are  invited to dinner")

print(f"{GuestsList[7]} you are  invited to dinner")

#3.7: Shrinking Guest list: There is new table + there is just space for 2 guests

print("I am sorry to tell you there is just space for 2 guests...")

FirstUninvited=GuestsList.pop(0)
print(f"{FirstUninvited} I am sorry to uninvite you to dinner since there is no space")

SecondUninvited=GuestsList.pop(1)
print(f"{SecondUninvited} I am sorry to uninvite you to dinner since there is no space")

ThirdUninvited=GuestsList.pop(2)
print(f"{ThirdUninvited} I am sorry to uninvite you to dinner since there is no space")

FourthUninvited=GuestsList.pop(3)
print(f"{FourthUninvited} I am sorry to uninvite you to dinner since there is no space")

FifthUninvited=GuestsList.pop(-1)
print(f"{FifthUninvited} I am sorry to uninvite you to dinner since there is no space")

SixthUninvited=GuestsList.pop(-2)
print(f"{SixthUninvited} I am sorry to uninvite you to dinner since there is no space")


#Invitations to only 2 guests

print(f"{GuestsList[0]} you are the first lucky guest to dinner")

print(f"{GuestsList[1]} you are the second lucky guest to dinner")

# Use DEL to remove the last 2 guests to have en empty list

del GuestsList[-2]
del GuestsList[-1]

print("The new guest list is: "), GuestsList

# EX 3.8: Seeing the world: choose 5 destinations

Locations=["Egypt", "Germany", "Finland", "England", "Italy"]
print(Locations)

# Use sorted to sort them alphabetically temporarily

print(sorted(Locations))

#Show the list is still in its original order

print(Locations)

# Use sorted to sort them alphabetically IN REVERSE temporarily

print(sorted(Locations, reverse=True))

#Show the list is still in its original order

print(Locations)

#Reverse original order (not alphabetically)

Locations.reverse()
print(Locations)

#Reverse again to go back to original order (not alphabetically)

Locations.reverse()
print(Locations)

#Sort them alphabetically permanently

Locations.sort()
print(Locations)

#Sort them alphabetically -IN REVERSE- permanently

Locations.sort(reverse=True)
print(Locations)

# EX 3.9: Dinner guests: LEN function: indicate number of people invited to dinner
print(len(GuestsList))

# EX 3.10: Every function: create a list and use every function learnt in this chapter

Colours=["red", "blue", "yellow", "white", "black"]

#Access elements in a list:

print(Colours[2].title())

#Using individual values from a list: create a message using an element from the list with F-string

message=f"My favourite colour is {Colours[3].title()}"
print(message)

#Modifying elements in a list:
Colours[2]="brown"
print(Colours)

#Adding elements to a list:

# Appending elements to the end of the list= added to the end

Colours.append("yellow")
print(Colours)

#Inserting elements into a list: at any position you want

Colours.insert(4, "green")
print(Colours)

#Removing elements from a list:

# 1) Removing using DEL statement: you know the position

del Colours[2]
print(Colours)

#2) Removing using POP () Method: removes last item in the list and let's you use it

LeastLikedColour=Colours.pop()
print(Colours)
print(LeastLikedColour)

#3) Removing using POP (...) from any position you want in a list

SecondLeastLikedColour=Colours.pop(2)
print(Colours)
print(f"The second colour I like least is {SecondLeastLikedColour.title()}")

#4) Removing items by Value

Colours.remove("green")
print(Colours)

#ORGANIZING LISTS

#Sorting a list permanently= sort() method: sort them alphabetically forever

Colours.sort()
print(Colours)

#Sorting a list permanently= sort() method in REVERSE order: sort them alphabetically

Colours.sort(reverse=True)
print(Colours)

#Sorting  a list temporarily with SORTED() function: you display the list alphabetically but for a short time

print(sorted(Colours))

#Sorting  a list temporarily with SORTED() function in REVERSE order: you display the list alphabetically but for a short time

print(sorted(Colours, reverse=True))

#Printing  LIST IN reverse order (not alphabetically)

Colours.reverse()
print(Colours)

#Finding length in a lit = LEN() function: it counts the ammount of elements you have in your list

print(len(Colours)) # N° of elements I have in my list











