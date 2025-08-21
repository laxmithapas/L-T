# Function to check if a number is prime
def is_prime(n):
    if n <= 1:   # 0 and 1 are not prime
        return False
    for i in range(2, n):   # check divisibility
        if n % i == 0:      # if divisible, not prime
            return False
    return True             # if no divisors, it's prime


# Main program
num = int(input("Enter a number: "))

print(f"\nFactors of {num} are:")

# Loop through numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:    # check if i is a factor
        if is_prime(i): # check if factor is prime
            print(i, "→ Prime")
        else:
            print(i, "→ Not Prime")
