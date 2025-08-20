# Program to check if a number is a Strong Number

# Step 1: Take input from the user
num = int(input("Enter a number: "))

# Step 2: Keep a copy of the original number
original_num = num

# Step 3: Initialize sum of factorials
sum_of_factorials = 0

# Step 4: Process each digit
while num > 0:
    digit = num % 10        # Get last digit
    num = num // 10         # Remove last digit

    # Step 5: Calculate factorial of the digit
    factorial = 1
    for i in range(1, digit + 1):
        factorial = factorial * i

    # Add factorial to the sum
    sum_of_factorials += factorial

# Step 6: Compare sum with original number
if sum_of_factorials == original_num:
    print(f"{original_num} is a Strong Number ✅")
else:
    print(f"{original_num} is NOT a Strong Number ❌")
