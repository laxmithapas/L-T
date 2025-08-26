str = input("Enter the string:")
result = ""

for i in str:
    if i != " ":
        result += i

print("String after removing spaces:", result)