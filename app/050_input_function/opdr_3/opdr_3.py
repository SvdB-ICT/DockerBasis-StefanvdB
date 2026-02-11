# Opdracht 3 input functie
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...

entry = input("Geef een lijst van objecten, gescheiden door een komma:\n") # Raw input.
entries = entry.split(",") # Splits the string into a list, separated where the commas are.
myList = [] # Create an empty list to store the stripped entries.

# Go through every entry and make sure they don't have any spaces.
for e in entries:
    myList.append(e.strip())

myList.sort(reverse=True) # Sorts the list in reverse order.

print(myList) # Prints the list.

exit()