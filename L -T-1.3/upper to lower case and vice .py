str = input("Enter the string: ")
upper = 0
lower = 0

for i in range(len(str)):
    if str[i].isupper():
        upper = upper + 1
    else:
        lower = lower + 1

print("The number of uppercase letters is:", upper)
print("The number of lowercase letters is:", lower)