# loops __ sometimes we may need it to do a piece of work a number of repeated times in such cases we may use loops. 
# A loop is a control structure that allows us to execute a block of code repetedly until a certain condition is met .
# There are two type of loops in python i.e The for loop and the while loop.
# Below is the syntax  of a for loop

"""
for variable in range(n):
    # block of code to be executed

"""

for greeting in range(5):
    print("Hello Moses", greeting)

print('=====================')

for number in range(10,20):
    print(number)
#  find the even numbers in the range of 50 to 71
for number in range(50 , 71, 2):
    print(number)


print("========================")
# create a python program that prints the odd numbers from 100 to 150
for number in range(101, 150 ,2 ):
    print(number)

print("==================")
# create a program that prints the multiples of 3 from 201 to 150
for number in range(201, 149, -3):
    print(number)

print("===========================")
# create a python that prints  that prints leap year


