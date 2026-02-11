# Opdracht 1 input function
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.



import math # Required for the square root function.

# Get float based inputs.
inputA = float(input("Geef de lengte van de eerste zijde\n"))
inputB = float(input("Geef de lengte van de tweede zijde\n"))

outputC = math.sqrt(inputA**2 + inputB**2) # The formula.

print("De lengte van de schuine zijde is:", outputC) # Print output.

exit()