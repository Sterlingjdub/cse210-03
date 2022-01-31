import random

class Seeker:
    """The person looking for the Hider . 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
        distance (List[int]): The distances travelled.
    """

    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = random.randint(1, 1000)
        
    def get_location(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        return self._location
        
    def move_location(self, location):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = location