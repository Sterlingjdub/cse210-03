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
        self.letters = []
        self.hit = 0
        self.tries = 0
        self._is_playing = True
        self._terminal_service = TerminalService()
        # self._letters = Seeker - I tried putting in list(self._word) and kept getting errors. List needed from word for guessing reasons
        
        
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing and self.tries < 4:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.
        Args:
            self (Director): An instance of Director.
        """
        
        user_guess = self._terminal_service.read_letter("\nEnter a letter: ")
        
        if ( self._word.guess(user_guess, self.hit)):
           self._do_updates(user_guess)
        else:
            self.tries = self.tries + 1
            self._word.updateState()
        
    def _do_updates(self, guess):
        """Keeps watch on what letters are guessed and which are still needed.
        Args:
            self (Director): An instance of Director.
        """
        self.hit = self.hit + 1
        self.tries = self.tries + 1
        self.letters.append(guess)
        
    def _do_outputs(self):
        """
        Args:
            self (Director): An instance of Director.
        """
        self._word.showDraw(self.letters)
        #self._parachute.write_text(loseOne)
        #if self._word.is_guessed():
        #    self._is_playing = False