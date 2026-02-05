# Python lists
# A List in python is a colllection of otems that ordered in a certain way
# A list is introduced by the use of sruare brackets
# The item of a list are stored inside of indexes. Note; In programming we start counting from index Zero(0), bmw, benx, hiance,..
# A list is mutable i.e. the contents of a list can be changed


cars = ["BMW", "Benze", "Hiance" , "Prado" , "Probox", "Mclarel" , "Range"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car on index four is: ", cars[4])

# List slicing - This is creating a list from a bigger list
print(cars[4:])

# printing from index zero to three
print(cars[:4])

print(cars[2:5])
# List - Mutability
# We use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)


# We use pop function to remove an item at the end of the list
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5]="Parejo"
print(cars)

# We can use the sort function to sort out items in alphabetical order
cars.sort(reverse=True)
print(cars)

