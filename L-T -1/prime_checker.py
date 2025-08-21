def is_prime(n):
    """
    Check if a given number is prime or not.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def main():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
            
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()
