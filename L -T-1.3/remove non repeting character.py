str = input("Enter the string:")


for i in str:
    if str.count(i) == 1:
        str = str.replace(i, "")
print("The non-repeating string after replacing:", str)