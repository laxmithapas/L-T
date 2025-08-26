str = input("Enter the string:")
vowels = "aeiouAEIOU"
for i in str:
    if i in vowels:
        str = str.replace(i, "")
print("String after removing vowels:", str)
