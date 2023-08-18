num=int(input("enter num"))
def negativefun(num):
    if num>0:
      return  -1*num
    else:
      return -1*abs(num)
print(negativefun(num))