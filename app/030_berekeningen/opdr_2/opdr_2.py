# Opdracht 2 berekeningen
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...

# Grabbing inputs to use for calculations
c = float(input("Input, Celcius \n"))
f = float(input("Input, Fahrenheit \n"))

# Calculating Fahrenheit using F = (C × 9/5) + 32
print(c, " graden Celcius is gelijk aan ", round( (c * (9/5)) + 32,1 ), " graden Fahrenheit.")

# Calculating Celcius using C = (F - 32) * 5/9
print(f, " graden Fahrenheit is gelijk aan ", round( (f - 32) * (5/9), 1), " graden Celcius.")

exit()