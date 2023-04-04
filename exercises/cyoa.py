"""Ex06 - Choose Your Own Adventure."""
__author__ = "730566314"
import random
points: int = 0
player: str = ""
randomfruit: str = random.randint(0, 0)
EMOJI: str = "\U0001f436"


def greet()-> None:
    """Begins the game, and lets player name pet."""
    player = input("What would you like to name your pet dog? ")
    print(f"Great! You pet dog's name is {player}. ")
    return player


def feed_pet():
    """This allows player to select what to feed their pet."""
    fruits = ['apple', 'banana', 'orange']
    print("What would you like to feed your pet dog?")
    print("1. Apple")
    print("2. Banana")
    print("3. Orange")
    print("4. Random")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print(f"You fed your pet dog an {fruits[0]}. Yum! ")
        return fruits[0]
    elif choice == "2":
        print(f"You fed your pet dog a {fruits[1]}. Yum! ")
        return fruits[1]
    elif choice == "3":
        print(f"You fed your pet dog an {fruits[2]}. Yum! ")
        return fruits[2]
    else:
        random_fruit = random.choice(fruits)
        return random_fruit
    

def play_with_pet():
    """This allows player to play with pet."""
    choice = input("Do you want to play with your pet dog? Type 'yes' for 'no'. ")
    if choice == "yes":
        toy = input("What do you want to play with? Choose from stick or ball. ")
    elif choice == "no":
        print("You didn't play with your pet dog. ")


def wash_pet():
    """Allows player to wash their pet."""
    choice = input("Do you want to wash your pet dog? Type 'yes' or for 'no'. ")
    if choice == "yes":
        print("You washed your pet dog. ")
    elif choice == "no":
        print("You didn't wash your pet dog. ")


def sleep_pet():
    """Lets player know their pet is tired."""
    print("Your pet would like to rest now. ")


def point(points:int) -> int:
    """Tracks points."""
    i = 0
    while True if choice == "yes"
    

def main() -> None:
    """Playing the game."""
    greet()
    feed_pet()
    play_with_pet()
    wash_pet()
    sleep_pet()
    print("Your pet dog is now satisified and happy. Thanks for taking care of it! " + EMOJI)
    

if __name__ == "__main__":
    main()