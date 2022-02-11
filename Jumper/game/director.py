from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.word import Word


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        
        is_playing (boolean): Whether or not to keep playing.
        
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._is_playing = True
        self._letters = Parachute()
        self._parachet = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.
        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ")
        self._seeker.move_location(new_location)
        
    def _do_updates(self):
        """Keeps watch on what letters are guessed and which are still needed.
        Args:
            self (Director): An instance of Director.
        """
        self._word.x(self._letters)
        
    def _do_outputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
    
        self._parachet.write_text(loseOne)
        if self._word.is_guessed():
            self._is_playing = False