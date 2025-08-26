str = input("Enter the string:")

special_characters = "!@#$%^&*()-+?_=,<>/1234567890[]"
for i in str:
    if i in special_characters:
        str = str.replace(i, "")
print("String after removing special characters:", str)
