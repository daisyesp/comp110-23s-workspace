"""File to define Bear class."""


class Bear:
    """Bear."""
    hunger_score: int = 0
    
    def __init__(self):
        """River."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increases the value of the age by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Simulates bear eating."""
        self.hunger_score += num_fish