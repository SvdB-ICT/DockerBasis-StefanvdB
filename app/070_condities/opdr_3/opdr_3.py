# Opdracht 3 condities
# Naam student: Stefan van den Berg
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

# Function for translating age to dictionary entry.
def GetTitle(inputJaar = 0): 
    output = ""
    if(leeftijd.get("baby")[0] <= inputJaar <= leeftijd.get("baby")[1]):
        output = "baby"

    if(leeftijd.get("kinderen")[0] <= inputJaar <= leeftijd.get("kinderen")[1]):
        output = "kinderen"

    if(leeftijd.get("volwassenen")[0] <= inputJaar <= leeftijd.get("volwassenen")[1]):
        output = "volwassenen"

    if(leeftijd.get("ouderen")[0] <= inputJaar <= leeftijd.get("ouderen")[1]):
        output = "ouderen"
    return output

leeftijdInput = int(input("Geef uw leeftijd in aantal jaar\n"))  # Get Input in integer form

leeftijdTitel = GetTitle(leeftijdInput) # Change input into entry using function

kortingHoeveelheid = int(kortings_percentages.get(leeftijdTitel)) # Define a simplified value

# Printing the information
print("U behoort tot de groep {}".format(leeftijdTitel))
print("U krijgt {}% korting".format(kortingHoeveelheid))
print("U betaalt daarom {}".format(normale_toegangsprijs - ((normale_toegangsprijs) * (kortingHoeveelheid/100))))
