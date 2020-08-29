#ACCESSING VALUES: variable={ key: value, (...)}  / print(variable)[key]

Alien1={"colour": "green", "points": 5}
print(Alien1["colour"])
print(Alien1["points"])

NewPoints=Alien1["points"] #new variable to create message
print(f"You have just earned {NewPoints} points!")

#Adding new values: variable["key"]=value

Alien1["Xposition"]=0
Alien1["Yposition"]=25
print(Alien1)

# Starting with empty dictionaries

Alien2={} #empty dictionary
Alien2["colour"]= "yellow" 
Alien2["points"]= 30 
print(Alien2)

#Modifying values

Alien2["colour"]="purple" #replace value
print(f"The Alien2's colour is now {Alien2['colour']}")

Alien3={"xposition": 0, "yposition": 25, "speed": "medium"}
print(f"Original position: {Alien3['xposition']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed

if Alien3["speed"]=="slow":
    xincrement=1
elif Alien3["speed"]=="medium":
    xincrement=2
else:
    xincrement=3

Alien3["xposition"]=Alien3["xposition"]+ xincrement #initial position 0 + speed medium 2
print(f"New position: {Alien3['xposition']}")

#Removing key-value pairs: del statement
del Alien1["colour"]
print(Alien1)

# A dictionary of similar objects

FavouriteLanguages={ # if the list takes more than 1 line, separate it like this:
    "Lucas": "Phython",
    "Sebas": "Java",
    "Sol": "C++",
    "Franco": "Go"
    }

ProgrammingLanguage=FavouriteLanguages["Lucas"].title()
print(f"Lucas' favourite language is {ProgrammingLanguage}")

# Using get() to access values: when you don't know if a key truly exists in a dictionary
#If "points" exists, it'll print it. If not, it will print a different message instead of showing an error

Alien4={"colour": "black", "speed":"fast"}
PointValue=Alien4.get("points", "No point value assigned")
print(PointValue)

#EX 6.1: Person

CeciliaCaimi={
    "FirstName": "Cecilia", 
    "LastName":"Caimi", 
    "Age": 42, "City": 
    "Almagro"
    }
print(f"Her first name is {CeciliaCaimi['FirstName']}")
print(f"Her last name is {CeciliaCaimi['LastName']}")
print(f"She is {CeciliaCaimi['Age']} years old")
print(f"She lives in {CeciliaCaimi['City']}")

# EX 6.2: Favourite numbers

FavouriteNumbers={
    'Lucas': 10,
    'Cecilia': 9,
    'Julián': 3,
    'Gabriela': 23,
    'Juan': 8
}
print(f"Lucas' favourite number is {FavouriteNumbers['Lucas']}")
print(f"Cecilia's favourite number is {FavouriteNumbers['Cecilia']}")
print(f"Julián's favourite number is {FavouriteNumbers['Julián']}")
print(f"Gabriela's favourite number is {FavouriteNumbers['Gabriela']}")
print(f"Juan's favourite number is {FavouriteNumbers['Juan']}")

#EX 6.3: Glossary

Glossary={
    "Variable": "A name that refers to a value.",
    "Assignment": "A statement that assigns a value to a variable.",
    "Script": "A program stored in a file.",
    "Concatenate": "To join two operands end-to-end.",
    "Semantics": "The meaning of a program.",
}

print(f"Variable: {Glossary['Variable']}")
print(f"\n Assignment: {Glossary['Assignment']}")
print(f"\n Script: {Glossary['Script']}")
print(f"\n Concatenate: {Glossary['Concatenate']}")
print(f"\n Semantics: {Glossary['Semantics']}")

# Looping through a dictionary: FOR

#ALL key- value pairs: .items() method

User1={
    "Username":"Rukasu89",
    "FirstName": "Lucas",
    "LastName": "Lioy",
}

for key, value in User1.items():
    print(f"\n Key: {key}")
    print(f"\n Value: {value}")

FavouriteLanguages={ 
    "Lucas": "Phython",
    "Sebas": "Java",
    "Sol": "C++",
    "Franco": "Go"
    }

for person, language in FavouriteLanguages.items(): #assigs person to key, and language to value!!!
    print(f"{person}'s favourite programming language is {language}'")

#Looping through ALL KEYS:  .keys() method

for name in FavouriteLanguages.keys():
    print(name)

# I add new friends which were not on previous friends' list
# When the name matches one of my friends, It'll display a message

Friends=["Lucas", "Bárbara", "Sol", "Matías"] # 2 from here weren't described before
for name in FavouriteLanguages.keys():

    if name in Friends: #just if the name is in my previous friends' list...
        language=FavouriteLanguages[name]
        print(f" \n {name}, I see you love {language}")

# You can also check if one person has been polled: NOT IN 
if "Erin" not in FavouriteLanguages:
    print("Erin, please study a programming language!")

# Looping through KEYS in PARTICULAR order: sorted() method

for name in sorted(FavouriteLanguages.keys()):
    print(f"{name}, thank you for taking the poll")

# Looping through ALL VALUES: values() method

# Here languages might be repeated

print("The following languages have been chosen: ")
for language in FavouriteLanguages.values():
    print(language)

# set: it just shows non-repeated items:

print("The following languages have been chosen: ")
for language in set (FavouriteLanguages.values()):
    print(language)

#EX 6.4: Glossary 2

Glossary={
    "Variable": "A name that refers to a value.",
    "Assignment": "A statement that assigns a value to a variable.",
    "Script": "A program stored in a file.",
    "Concatenate": "To join two operands end-to-end.",
    "Semantics": "The meaning of a program.",
}

for concept, definition in Glossary.items():
    print(concept)
    print(definition)

# EX 6.5: Rivers:

Rivers={"Nile": "Egypt", "Amazonas": "Brazil", "Paraná": "Argentina"}

for river in sorted(Rivers.keys()):
    print(river)

for country in sorted(Rivers.values()):
    print(country)

# EX 6.6: Polling:

Candidates=["Luis", "Lucas", "María", "Sebas"]

for candidate in Candidates:
    if candidate in FavouriteLanguages:
        print(f" {candidate}, thanks for responding.")
    else:
        print(f" {candidate}, would you mind taking the poll?")

#NESTING

#A list of dictionaries...

#Dictionaries....

Alien1={"colour":"green", "points": 5}
Alien2={"colour": "yellow", "points": 10}
Alien3={"colour": "red", "points": 15}

AliensList=[Alien1, Alien2, Alien3] #list

for Alien in AliensList:  #loop
    print(Alien)

#More complex example:
#1: create empty list to store aliens:

AliensNewList=[] #empty list

#2: make 30 green alients: use range() to create 30 aliens

for AlienNumber in range(30): #range(30) creates 30 aliens
    NewAlienCreated={"colour": "green", "points": 5 , "speed":"slow"} # dictionary of each new alien created
    AliensNewList.append(NewAlienCreated) # Add to AliensNewList each new alien created

#3: change colours of first 3 aliens using if/elif:

for Alien in AliensNewList[:3]: #the first 3
    if Alien["colour"] == "green": # if the alien is green... then,..
        Alien["colour"] = "yellow" #change its colour to yellow
        Alien["speed"] = "medium" #change its speed to medium
        Alien["points"] = 10 #change its score to 10
    elif  Alien["colour"] == "yellow":
        Alien["colour"] = "red" #change its colour to red
        Alien["speed"] = "fast" #change its speed to fast
        Alien["points"]= 15 #change its score to 15

#4: show the first 5 aliens

for Alien in AliensNewList[:5]: #for each alien in the list, print the first 5
    print(Alien)
print("...")

#5: Show how many aliens have been created

print(f"The total number of aliens is: {len(AliensNewList)}") #count number of aliens in list

# A list in a dictionary....

#Store information about a pizza

PizzaInformation={ # this is a dictionary
    "crust":"thick",
    "toppings":["mushrooms", "extra cheese"], #list within dictionary
    }

#Summarize the order:
print(f"You ordered a {PizzaInformation['crust']}-crust pizza " 
"with the following toppings:")

for topping in PizzaInformation["toppings"]:
    print("\t" + topping)

#Another example...

FavouriteLanguagesNew={ #dictionary
"Lucas": ["Python", "Java"], #List
"Cecilia": ["C++", "Go"],
"Franco": ["JavaScript"],
"Juan": ["HTML"],
}

for name, languages in FavouriteLanguagesNew.items(): #items() returns list of key-value pairs
    print(f"{name}'s favourite languages are:")
    for language in languages:
        print(f"\t {language}")

#A dictionary in a dictionary....

Users={ #First dictionary
    "Aeinstein":{ #Dictionary within previous dictionary
        "First": "Albert",
        "Last": "Einstein",
        "Location": "Princeton"
        },
    "Mcurie":{
        "First": "Marie",
        "Last": "Curie",
        "Location": "Paris"
        },
    }

for UserName, UserInfo in Users.items():
    print(f" \n Username: {UserName}")
    FullName=f"{UserInfo['First']} {UserInfo['Last']}"
    Location=UserInfo["Location"]

    print(f"\n Full name: {FullName}")
    print(f"\n Location: {Location}")


# EX 6.7: People

CeciliaCaimi={"FirstName": "Cecilia", "LastName":"Caimi",  "Age": 42, "City": "Almagro"}

JavierCoronel={"FirstName": "Javier", "LastName":"Coronel",  "Age": 31,  "City": "Liniers"}

FlorenciaAndria={ "FirstName": "Florencia", "LastName":"Andria", "Age": 30,"City": "Villa Crespo"}

People=["CeciliaCaimi", "JavierCoronel", "FlorenciaAndria"]

for person in People[:1]:
  print(CeciliaCaimi)
  print(JavierCoronel)
  print(FlorenciaAndria)

# EX 6.8: Pets

Pet1={"Animal": "Dog", "Owner": "Lucas"}
Pet2={"Animal": "Cat", "Owner": "Pilar"}
Pet3={"Animal": "Turtle", "Owner": "Florencia"}

Pets=[Pet1, Pet2, Pet3]  # Don't write them as strings with "..." when creating the list

for pet in Pets:
    print(pet)

# EX 6.9: Favourite places

FavouritePlaces={"Lucas": ['Germany', 'Chile', 'Turkey'], "Cecilia": ['England','Greece'], "Gabriela": ['Argentina']}

for favplace in FavouritePlaces["Lucas"]:
    print("Lucas loves "+ favplace)
   
for favplace in FavouritePlaces["Cecilia"]:
    print("Cecilia loves "+ favplace)

for favplace in FavouritePlaces["Gabriela"]:
    print("Gabriela likes "+ favplace)

# EX 6.10: Favourite numbers

FavouriteNumbers={
    'Lucas': [10, 12, 16],
    'Cecilia': [9, 3, 4],
    'Julián': [3, 23, 45],
    'Gabriela': [23, 8, 12, 34],
    'Juan': [8, 3, 6],
}
print(f"Lucas' favourite numbers are {FavouriteNumbers['Lucas']}")
print(f"Cecilia's favourite numbers are {FavouriteNumbers['Cecilia']}")
print(f"Julián's favourite numbers are {FavouriteNumbers['Julián']}")
print(f"Gabriela's favourite numbers are {FavouriteNumbers['Gabriela']}")
print(f"Juan's favourite numbers are {FavouriteNumbers['Juan']}")

# EX 6.11: Cities

Cities={
    'BuenosAires':{
        "Country": "Argentina",
        "Population": 37000000,
        "Fact": "Friendly city",
        },
    'RiodeJaneiro':{
        "Country": "Brazil",
        "Population": 87000000,
        "Fact": "Nice beaches",
        },
    'London':{
        "Country": "England",
        "Population": 62000000,
        "Fact": "Rainy city",
        },
    }

for city, cityinformation in Cities.items():
    print(f"\n Country: {cityinformation['Country']}")
    print(f"\n Population: {cityinformation['Population']}")
    print(f"\n Fact: {cityinformation['Fact']}")

# EX 6.12: Extensions
#Choose one previous exercise and modify it:

FavouriteNumbers={
    'Lucas': [10, 12, 16],
    'Cecilia': [9, 3, 4],
    'Julián': [3, 23, 45],
    'Gabriela': [23, 8, 12, 34],
    'Juan': [8, 3, 6],
}

FavouriteNumbers['Lucas']=100
FavouriteNumbers['Julián']=1000
FavouriteNumbers['Juan']=10000

print(f"Lucas' favourite numbers are {FavouriteNumbers['Lucas']}")
print(f"Cecilia's favourite numbers are {FavouriteNumbers['Cecilia']}")
print(f"Julián's favourite numbers are {FavouriteNumbers['Julián']}")
print(f"Gabriela's favourite numbers are {FavouriteNumbers['Gabriela']}")
print(f"Juan's favourite numbers are {FavouriteNumbers['Juan']}")
