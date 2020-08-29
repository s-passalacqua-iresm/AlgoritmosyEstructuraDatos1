# EX 2.1:  Simple message

message="Hello, Mark"
print(message)

#EX 2.2:  Simple messages: change value: check the newest value is the one that counts

newmessage="Black"
print(newmessage)

newmessage="White"
print(newmessage)  # Changed value of newmessage: the new one appears replacing the old one

#EX 2.3: Personal message

person="Tom" 
PersonalMessage=f"Hello, {person},would you like to learn some Python today?"
print(PersonalMessage)

#EX 2.4: Name cases: printing names using lower, upper and title cases

name="lucas lioy"
print(name.lower()) # lowercase
print(name.upper()) #uppercase
print(name.title()) #title case

#EX 2.5: Famous Quote

FamousQuote="Albert Einstein once said: ' A person who never made a mistake never tried anything new'"
print(FamousQuote)

#EX 2.6: Famous Quote II (use a new variable for the famous person)

FamousPerson="Albert Einstein"
ChangedFamousQuote=f"{FamousPerson} once said: ' A person who never made a mistake never tried anything new'"
print(ChangedFamousQuote)

#EX 2.7: Tabs, skipping lines and Stripping names (left, right and both)

print("Subjects:\n \t Maths \n Biology \n \t History")
# \n skips a line 
# \t  tab

Fullname="*  Lucas Lioy  *"
print(Fullname.rstrip()) #get rid of RIGHT extra whitespace
print(Fullname.lstrip()) #get rid of LEFT extra whitespace
print(Fullname.strip()) # get rid of ALL whitespace: both sides

# EXTRA 1: concatenation and replication

print("Alice"+"Tom") #Concatenation: +
print("Alice"*5)  #Replication: *

# EXTRA 2: print,input and len

print("What's your name?")
name=input() # first variable, then equalled to input()
print("It's good to meet you, " + name.title()) # title() to add capital letter to the initial
print("The length of your name is: ")
print(len(name))

#EXTRA 3: , str(), int() and float () functions

print("How old are you?")
age=input()
print("You will be " + str(int(age)+1)+ " in a year")

# all the answers written in input become STRING, so we must turn str() into int() to add 1 more year and then turn it into str() again to concatenate that in the message

# EXTRA 4: operators:
# ** = exponent; %= modulus/remainder, //= floored quotient