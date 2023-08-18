num =int(input("enter num"))

i=int(input("enter 1 to check palindrome\n enter 2 to check even or odd"))
def check(num):
    if i==1:
        temp = i
        rev = 0
        while (i> 0):
            dig = i % 10
        rev = rev * 10 + dig
        num =i // 10
        if (temp == rev):
            print("The number is palindrome")
        else:
            print("Not a palindrome")
    else:
        if(i%2!=0):
            print("odd")
        else:
            print('even')
print(check(num))