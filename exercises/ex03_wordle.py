"""Ex03 - Structured Wordle"""
__author__ = "730566314"
def contains_char(word: str, character: str) ->bool:
    """Checks if any single character in second string is in any index of first string """
    assert len(character) == 1
    if character in word:
        return True
    else:
        return False

def emojified(guess: str, secret: str)-> str:
    """If guess indicies match indicies of secret word, it will return codified color emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    letter = 0
    while (letter < len(guess)):
        check_match = contains_char(secret, guess[letter])
        if(check_match is False):
            emoji = emoji + WHITE_BOX
        else:
            if(check_match is True):
                if(secret[letter] == guess[letter]):
                    emoji = emoji + GREEN_BOX
                else:
                    emoji = emoji + YELLOW_BOX
        letter = letter +1
    return emoji

def input_guess(right_length: int)-> str:
    """Checks if guess word matches lnegth of secret word"""
    length = True
    user_guess: str = input(f"Enter a {right_length} character word: ")
    while length:
        if (len(user_guess) != right_length):
            user_guess = input(f"That wasn't {right_length} chars! Try again: ")
        else:
            length = False
    return user_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "perro"
    word_length = len(secret_word)
    turn_number = 1
    GREEN_BOX: str = "\U0001F7E9"
    green_emoji = GREEN_BOX
    turn = True
    while ((turn is True and turn_number < 7)):
        print(f"=== Turn {turn_number}/6 ===")
        guessed_word = input_guess(word_length)
        emoji_section = emojified(guessed_word, secret_word)
        print(emoji_section)
        if (guessed_word == secret_word):
            print (f"You won in {turn_number}/6 turns! ")
            turn = False
        else:
            turn_number = turn_number + 1
            if (turn_number == 7):
                print ("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()