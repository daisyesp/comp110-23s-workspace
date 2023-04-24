"""File to define River class."""
__author__ = "730566314"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River."""
    day: int = 0
    bears: list[int] = []
    fish: list[str] = []
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """If fish is younger than 3 removes it, if bear age is less than 5 remove them."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """Bears will eat 3 fish, if 5 fish in river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """If hunger score is 0, removes bears."""
        new_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
            self.bears = new_bears
        return None

    def repopulate_fish(self):
        """For each pair of fish, 4 new fish will be produced."""
        num_fish = len(self.fish)
        num_fish_new = (num_fish // 2) * 4
        for i in range(num_fish_new):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """If 2 bears, one new bear is added."""
        num_bears = len(self.bears)
        num_bears_new = num_bears // 2
        for i in range(num_bears_new):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Structures number of day, fish population, and bear population."""
        print("~~~ Day " + str(self.day) + ": ~~~ \nFish population: " + str(len(self.fish)) + "\nBear population: " + str(len(self.bears)))
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week in the river."""
        for i in range(7):
            self.one_river_day()
    
    def remove_fish(self, amount: int):
        """Removes fish."""
        self.fish = self.fish[amount:]