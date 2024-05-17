def length_of_last_word(s):
    # Split the string by spaces
    words = s.split()
    # If there are no words, return 0
    if not words:
        return 0
    # Return the length of the last word
    return len(words[-1])


print(length_of_last_word("hello everyone"))
print(length_of_last_word("testing code"))
print(length_of_last_word("running code"))