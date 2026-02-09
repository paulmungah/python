# A dictionary is a data type that stores data in terms of key - value pair
# It is introduced by the use of curly braces{}
# The values stored inside of a dictionary can be if any data type
# To access the values in a dictionary we use the keys


phonebook= {
    "Benson" : "25475382929",
    "Mary"  : "2549589784",
    "Stephen" : "254884298"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# printing out benson's number
print(phonebook["Benson"])

print('======================')

player ={
    "name" : "Messi",
    "age ": 40,
    "team " : ["PSg" , "Barcelona" , "Argentina"] ,
    "more"  : {
        "children" : 3,
        "residence" : "US",
        "phone" : (24536638379, 738963999238 , 2168280)
    }

}
# print barcelona  - the second team messi played for 
print(player["team "][1])


# print mesii the second number
print(player["more"]["phone"][1])