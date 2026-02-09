# create a python that is able to determine whether a umber enterd is an even nember or odd 
number = int(input("Enter number: "))
if number%2 == 0 :
   print("The number is even")

else :
   print("The number is odd")

# Create a python program that is able to determine whether a person can donate blood based on age and weight of a person . if the weight is greater than 50kg and age is above 18, then the person can donate blood else cannot donate 

weight = float(input("Enter your weight here: "))
age = int(input("Enter yor age: "))

if age >=18 and weight >50 :
   print("You can donate blood")

else :
   print("You cannot donate blood") 