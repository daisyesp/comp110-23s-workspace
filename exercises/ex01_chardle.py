"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730566314."

enter_word: str = input("Enter a 5-character word: ")
if (len(enter_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

enter_character: str = input("Enter a single character: ")
if (len(enter_character) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + enter_character + " in " + enter_word)
count: int = 0

if (enter_word[0] == enter_character):
    print(enter_character + " found at index 0 ")
    count = count + 1

    if (enter_word[1] == enter_character):
        print(enter_character + " found at index 1 ")
        count = count + 1
    
    if (enter_word[2] == enter_character):
        print(enter_character + " found at index 2 ")
        count = count + 1

    if (enter_word[3] == enter_character):
        print(enter_character + " found at index 3 ")
        count = count + 1

    if (enter_word[4] == enter_character):
        print(enter_character + " found at index 4 ")
        ount = count + 1

if (count == 0):
    print("No instances of " + enter_character + " found in " + enter_word)

if (count == 1):
    print(str(count) + " instance of " + enter_character + " found in " + enter_word)
    
if (count > 1):
    print(str(count) + " instances of " + enter_character + " found in " + enter_word)