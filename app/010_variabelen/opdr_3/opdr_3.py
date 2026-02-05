# Opdracht 1
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...

my_dict = {"naam": "Willem", "achternaam": "van der Broek", "leeftijd": "23", "favoriete kleur": "blauw"} # The required dictionary

valid_keys = {"naam", "achternaam", "leeftijd", "favoriete kleur"} # For easy validation of keysc

def printInfo():
    print("Naam: ", my_dict["naam"])
    print("Achternaam: ", my_dict["achternaam"])
    print("Leeftijd: ", my_dict["leeftijd"])
    print("Favoriete kleur: ", my_dict["favoriete kleur"])

printInfo() # Print the current information

while True: # Keep asking until interupted with break
    inputYN = input("Wil je een aanpassing maken? (y/n) ")
    if inputYN == "y":
        while True: # Keep asking until interupted with break
            key = input("Welke waarde wil je aanpassen? (naam, achternaam, leeftijd, favoriete kleur) ")
            if key in valid_keys: # Checks validity of the input
                break # Valid input and thus proceeds to next step
            print("Deze waarde bestaat niet. Probeer opnieuw.")

        value = input("Wat wil je er van maken? ")
        my_dict[key] = value # Changes the directory entry using the given value

        printInfo() # Prints the new information
        
    # Allows you to exit the program
    elif inputYN == "n":
        print("Top, tot ziens!")
        break

    # Error handling
    else:
        print("Ongeldige invoer, typ 'y' of 'n'.\n")

exit() # Exit