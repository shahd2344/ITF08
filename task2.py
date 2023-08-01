name=(input("Enter your full name"))
number= (input("Enter your mobile number for example 05*-****-***\n "))
year= int(input("Enter year of birth"))
currentAge=2023
age=currentAge-year
number=number.split('-')
print("Name:         ","Age:","    Mobile Number As A List:")
print(name+"      ",age,"     ",number)
print("*******************************")
