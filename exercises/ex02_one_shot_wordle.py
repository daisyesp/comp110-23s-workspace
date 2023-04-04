"""Ex02 - One-Shot Wordle - Loops!"""
__author__ = "730566314"
SECRET: str = "python"
length: int = len(SECRET)
guess: str = (input(f"What is your {length}-letter guess? "))
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
index: int = 0
while playing:
    if (len(guess) != len(SECRET)):
        guess = input(f"That was not {length} letters! Try again: ")
    else:
        while index < length:
            if SECRET[index] == guess[index]:
                emoji = emoji + GREEN_BOX
            else: 
                exists: bool = False
                match: int = 0
                while (exists is False) and (match < len(SECRET)):
                    if guess[index] == SECRET[match]:
                        exists = True
                    match = match + 1
                if exists is True:
                    emoji = emoji + YELLOW_BOX 
                else: 
                    emoji = emoji + WHITE_BOX
            index = index + 1

        print(emoji)

        if guess != SECRET:
            print("Not quite! Play again soon!")
            playing = False
        if guess == SECRET:
            print("Woo! You got it! ")
            playing = False

            
            