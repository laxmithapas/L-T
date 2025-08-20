def is_prime(n, d=2):
    
    if n <= 1 or n % d == 0:
        return False
    if d * d > n:
        return True
    
    
    
    return is_prime(n, d + 1)




num = int(input('Enter the number:'))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
