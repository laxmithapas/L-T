str = (input("Enter the string: "))
const = 0
vowel = 0
for i in str:
    if i in 'aeiouAEIOU': 
        vowel = vowel + 1
    else: 
        const = const + 1
print("The number of const and vowel in the string are {vowel} and {const}")
