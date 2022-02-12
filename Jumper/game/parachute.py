from game.terminal_service import TerminalService

class Parachute:

    """The object of parachute that will be used for the jumper game.
    A wrong letter guessed will take away a piece of the parachute.
    """

    def __init__(self):
        self._parachute = ["  __ ", " /___\ ", " \   / ", "  \ /  ", "   0  ", "  /|\   ", "  / \  ",  "", "^^^^^^^"]            
        self._terminal_service = TerminalService()

    def draw_parachute(self):
        """
        Draws the parachute in the form of a for loop iterating through a list.
        """
        for piece in self._parachute:
            self._terminal_service.write_text(piece)

    def cut_parachute(self):
        """
        Cut the parachute piece by getting rid of the first item in the list
        """
        self._parachute.pop(0)

    def check_parachute(self):
        """
        Determine if the parachute is over after checking the quantity of items in the list
        """
        return len(self._parachute) == 4

    def parachute_game_over(self):
        """
        If it's a game over, the head will be a X instead of a 0
        """
        self._parachute[0].replace('0', 'X')