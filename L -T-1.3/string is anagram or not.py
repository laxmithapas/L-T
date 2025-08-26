def is_anagram(str1, str2):
    """
    Check if two strings are anagrams of each other.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
    """
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Remove any non-alphabetic characters
    str1 = ''.join(char for char in str1 if char.isalpha())
    str2 = ''.join(char for char in str2 if char.isalpha())
    
    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

def main():
    """Main function to demonstrate the anagram checker."""
    print("Anagram Checker")
    print("================")
    
    # Get input from user
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    # Check if they are anagrams
    if is_anagram(str1, str2):
        print(f"'{str1}' and '{str2}' are anagrams!")
    else:
        print(f"'{str1}' and '{str2}' are NOT anagrams.")
    
    # Additional test cases
    print("\nTest Cases:")
    print("===========")
    
    test_cases = [
        ("listen", "silent"),
        ("triangle", "integral"),
        ("hello", "world"),
        ("Dormitory", "Dirty room"),
        ("Eleven plus two", "Twelve plus one"),
        ("python", "typhon")
    ]
    
    for str1, str2 in test_cases:
        result = is_anagram(str1, str2)
        status = "✓" if result else "✗"
        print(f"{status} '{str1}' vs '{str2}': {result}")

if __name__ == "__main__":
    main()
