def odd(num):
    if num%2==0:
        return False
    else:
        return True
for i in range(int(input())):
    b, a = map(int, input().split())

    if a==1 and b==1:
        print("Tonya")
    elif a==1 and odd(b)==True:
        print("Tonya")
    elif odd(b) == True and odd(a)== True:
        print("Tonya")
    elif odd(b) == False and odd(a) == False:
        print("Tonya")
    elif odd(b)== False and odd(a) == True:
        print("Burenka")
    elif odd(b) == True and odd(a)== False:
        print("Burenka")

