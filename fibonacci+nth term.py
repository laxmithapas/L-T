n = int(input("Enter which term (n) you want: "))


first = 0
second = 1

# If user asks for the 0th term
if n == 0:
    print("The 0th term is:", first)

# If user asks for the 1st term
elif n == 1:
    print("The 1st term is:", second)

# For all other cases (n >= 2)
else:
    # We already know first = 0, second = 1
    # Now we calculate from the 2nd term up to nth term
    for i in range(2, n + 1):
        next_term = first + second   # sum of previous two numbers
        first = second               # shift second → first
        second = next_term           # shift next_term → second
    
    print(f"The {n}th term is:", second)
