#def pow(base, exp):
#    if exp == 0:
#        return 1
#    else:
#        return base * pow(base, exp - 1)
#n = int(input('Enter the base: ')
#m = int(input('Enter the exponent: '))
#print(f"{n} raised to the power of {m} is {pow(n, m)}")

def pow(base, p):
    if p== 0:
        return 1
    elif p == 1:
        return base
    else:
        return base * pow(base, p - 1)
n = int(input('Enter the base: '))
m = int(input('Enter the exponent: '))
print(f"The power of {n} is ", pow(n, m))