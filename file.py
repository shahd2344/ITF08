"""
with open('file.txt',"r")as file:
    for f in file.readlines():
      f=f.replace('\n'," ")#convert \n to spaces at end of line
      f=f.split(',')# to split base on , as a lists
      print(f)"""
# Get user input
name = input("Enter the name: ")
age = input("Enter the age: ")
birth= input("Enter the date of birth: ")

with open('file.txt',"w")as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Date of Birth: {birth}\n")
file.close()
print("info saved")