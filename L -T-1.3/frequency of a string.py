str = input("Enter a string: ")

frequency = {}
for char in str:
    if char.isalpha():  
        char = char.lower()
        frequency[char] = frequency.get(char, 0) + 1


print("Character Frequency:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

