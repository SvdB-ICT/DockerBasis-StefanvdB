# Opdracht 3 input functie
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...

# Hier start de for-loop

print("Lijst met pizzas:")
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
print(pizzas)

print("\nGesoorteerde lijst:")
pizzas.sort()
print(pizzas)

print("\nVoeg eigen smaak toe:")
pizzas.append("salami")
print(pizzas)

print("\nVerwijder de minst favoriete:")
pizzas.remove("quattro stagioni")
print(pizzas)

print("\nPrint de eerste 3 pizzas:")
print(pizzas[0:3])

print("\nPrint alleen de middelste pizza:")
print(pizzas[2])

print("\nPrint alleen de laatste 3 pizzas:")
print(pizzas[-3:])