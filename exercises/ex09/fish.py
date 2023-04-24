"""File to define Fish class."""


class Fish:
    """Fish."""

    age: int = 0  
    
    def __init__(self):
        """---."""
        self.age: int = 0
        return None
    
    def one_day(self):
        """Increases value of the age by 1."""
        self.age += 1
        return None