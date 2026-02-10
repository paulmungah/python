# A for loop can also be used to iterate through a list , tuple , string or even dictionary

name= "Bernard"

for letter in name:
    if letter =="n":
        print("The letter is n")
    else:
        print(letter)

print("=======================")

# below is a list of counties
counties = [ "Nairobi" , "Mombasa", "Kisumu", "Nakurur" , "Eldoret", "Kajiado", "Machakos" , "Meru" , "Embu"]

for county in counties :
    print(county)

print("=======================")

for county in counties:
    if "Nairobi" in counties:
        print("The county is Nairobi")
        break
    else:
        print("The county is not part of the list")

print("======================")
# The for loop can also be used to iterate throught a dictionary


player = {
    "age " : 25 ,
    "teams":["PSG", "Monaco", "France"] ,
    "nationality":"French"

}

for values in player:
    print(player[values])

print("=========================")
# loop through the team the player has played for
for team in player["teams"]:
    print(team)



    