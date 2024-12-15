def factorial(num):
    mul = 1
    for i in range(1,num+1):
        mul = mul * i
    return mul
def odd(num):
    count = 0
    for i in range(1 , num+1):
        
        if i%2 != 0:
            count += 1
        else:
            pass
    return count
def comb(num):
    result = factorial(num)/(factorial(1) * factorial(num-1))
    return result

print(comb(1)*comb(5)*comb(10))