# Opdracht 3 tekstfuncties
# Naam student: Stefan van den Berg
# Groep:

# Hier komt je code...



# Definition of the tree.
lines = (
    "    *", 
    "   ***",
    "  ******",
    " ********",
    "***********",
    "    ***",
    "    ***",
    "    ***"
)

# Get the parameters to use for tree generation.
def GetParams():
    # Maxxed the inputs to prevent negative inputs.
    treeCount = max(int(input("How many trees do you want to draw? ")), 1)
    spaceBetweenTrees = max(int(input("How many spaces do you want between the trees? ")), 0)

    return treeCount, spaceBetweenTrees # Sends the paramaters out

# This draws the trees in the terminal.
def DrawTrees():
    treeCount, spaceBetweenTrees = GetParams() # Get the parameters for tree generation from the GetParams function.

    longestLine = 0 # Here I get the longest line of the tree to make sure there is no wasted space.
    for line in lines:
        if len(line) > longestLine:
            longestLine = len(line)

    # Some flavor text and debugging.
    print("Longest line is: ", longestLine)
    print("Space between trees will be: ", spaceBetweenTrees)
    print("The amount of tree shall be: ", treeCount)
    print("Now printing trees: \n")

    # Adding together the different parts and printing them.
    for part in lines:
        partString = part.lstrip().center(longestLine)
        
        for tree in range(treeCount-1):
            partString += " " * spaceBetweenTrees
            partString += part.lstrip().center(longestLine)
        
        print(partString)

# Calling the functions
DrawTrees()
exit()