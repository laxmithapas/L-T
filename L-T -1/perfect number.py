# Program to check if a number is a Perfect Number

# Step 1: Take input
num = int(input("Enter a number: "))

# Step 2: Initialize sum of divisors
sum_of_divisors = 0

# Step 3: Find all proper divisors
for i in range(1, num):
    if num % i == 0:        # i divides num
        sum_of_divisors += i  # add to sum

# Step 4: Compare sum with the number
if sum_of_divisors == num:
    print(f"{num} is a Perfect Number ✅")
else:
    print(f"{num} is NOT a Perfect Number ❌")
