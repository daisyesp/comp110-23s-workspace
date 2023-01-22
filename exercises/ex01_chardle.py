"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730566314"



enter_word: str = input("Enter a 5-character word: ")
if (len(enter_word) < 5):
    print("Error: Word must contain 5 characters")
    exit()
enter_character: str = input("Enter a single character: ")
print("Searching for " + enter_character + " in " + enter_word)


count: int = 0



if (enter_word[0] == enter_character):
    count = count + 1
    print(enter_character + " found at index 0 ")

if (enter_word[1] == enter_character):
    count = count + 1
    print(enter_character + " found at index 1 ")
   
if (enter_word[2] == enter_character):
    count = count + 1
    print(enter_character + " found at index 2 ")

if (enter_word[3] == enter_character):
    count = count + 1
    print(enter_character + " found at index 3 ")

if (enter_word[4] == enter_character):
    count = count + 1
    print(enter_character + " found at index 4 ")


if (count == 0):
    print("No instances of" + enter_character + " found in " + enter_word)

if (count == 1):
    print(str(count) + " instance of " + enter_character + " found in " + enter_word)
    

if (count > 1):
    print(str(count) + " instance of " + enter_character + " found in " + enter_word)





