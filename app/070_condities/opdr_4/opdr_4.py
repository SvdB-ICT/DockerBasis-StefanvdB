# Opdracht 4 condities
# Naam student: Stefan van den Berg
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]

# Hier de rest van jouw code...

beschikbare_toppings = list(top[0] for top in toppings)

def ToppingSelectie():
    inputString = ""

    while True:
        i = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")
        
        for naam, prijs in toppings:
            if i == naam:
                print(f"U heeft {naam} besteld. Dat kost {prijs}")
                return (naam, prijs)
            
        print("Uw keuze zit niet in ons assortiment")


keuzes = [ToppingSelectie()]
while True:
    i = input("Wil je nog iets toevoegen? y/N\n")
    if(i != "y" and i != "Y"):
        break
    keuzes.append(ToppingSelectie())

print("Uw bestelling bestaat uit:\n")
totaalPrijs = 0.0
for itemNaam, itemPrijs in keuzes:
    print(f"{itemNaam} voor {itemPrijs}")
    totaalPrijs += itemPrijs

print(f"----------------------------------\nIn totaal kost dit {totaalPrijs}")