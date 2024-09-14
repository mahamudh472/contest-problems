

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)

# print(fact(5))


#print your name 10 times without using any loop

i = 1
def name():
    global i
    if i <= 10:
        print("Mahmud", i)
        i+=1
        name()
name()

def power(n, p):
    if p==0:
        return 1
    return n*power(n, p-1)

print(power(2, 5))