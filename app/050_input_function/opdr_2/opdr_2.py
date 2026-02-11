# Opdracht 2 berekeningen
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
inputString = "------------\nWat wil je doen?\n1 = Lijst inzien, 2 = Een persoon verwijderen\n3 = Een persoon toevoegen, 4 = Een persoon toevoegen op een specifieke plek\n5 = Exit\n------------\n"

def PrintCurrentList():
    print(gasten)

while True: # True during entire duration of the script
    i = input(inputString) # Get user input
    
    # Goes through the allowed inputs and executes the corresponding functions
    match i:
        case "1": # Print the current list
            print("Je hebt optie 1 geselecteerd.")
            PrintCurrentList()

        case "2": # Remove a person from the list
            print("Je hebt optie 2 geselecteerd.")
            PrintCurrentList()
            teVerwijderenGast = input("Wie wil je verwijderen uit de lijst? (Hoofdlettergevoelig!) ")
            if teVerwijderenGast in gasten:
                gasten.remove(teVerwijderenGast)
                print("Je hebt {} verwijderd uit de lijst.".format(teVerwijderenGast))
            else:
                print("Die persoon staat niet op de lijst.")

        case "3": # Add a person to the end of the list
            print("Je hebt optie 3 geselecteerd.")
            nieuweGast = input("Wie wil je toevoegen aan de lijst? ")
            gasten.append(nieuweGast)
            print("Je hebt {} toegevoegd aan de lijst.".format(nieuweGast))

        case "4": # Add a person at a specific position in the list
            print("Je hebt optie 4 geselecteerd.")
            PrintCurrentList()
            nieuweGast = input("Wie wil je toevoegen aan de lijst? ")
            positie = int(input("Op welke positie wil je deze persoon toevoegen? (1 t/m {}) ".format(len(gasten) + 1)))
            if positie < 1 or positie > len(gasten) + 1:
                print("Ongeldige positie. Vul een getal in tussen 1 en {}.".format(len(gasten) + 1))
            else:
                gasten.insert(positie - 1, nieuweGast)
                print("Je hebt {} toegevoegd aan de lijst op positie {}.".format(nieuweGast, positie))

        case "5": # Exit the program
            print("Je hebt optie 5 geselecteerd. Tot ziens!")
            exit()

        case _: # Error handling
            print("Vul een geldige optie in.")