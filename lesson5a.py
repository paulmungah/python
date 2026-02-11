# Python Function
# They are a block of code/statements that performs a given task/action
# Functions are defined using the def keyboard. (define)
# We have two main types of functions i.e. :
# 1. In built finctions > they come preinstalled with the interpreter i.e. print() , pop (), range (), append () etc .......
# 2. User defined functions ==> They are created by a programmer to solve a given task . 
#  To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello, how are you?")

# below we call the function by use of its name 
greetings()

print("====================")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is :",sum)

addition()

print("==================")
# function to multiply three values 
def multiply():
    num1 = 5
    num2= 3
    num3 = 55
    product= num1*num2*num3
    print("The product is :", product)

multiply()


print("=====================")
# Below is a division function
def divide():
    number1 = int(input("Enter the first number : "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print ("The answer is : ", quotient)

divide()    




