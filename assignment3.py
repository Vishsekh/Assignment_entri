def has_unique_chars(s):
    seen = []
    for char in s:
        if char in seen:
            return False
        seen.append(char)
    return True

if __name__ == "__main__":
    inputs = input("Enter a string: ")
    result = has_unique_chars(inputs)
    if result:
        print("The string has all unique characters.")
    else:
        print("The string does not have all unique characters.")
