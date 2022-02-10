from game.seeker import Seeker

class Parachute:
    
    def __init__(self):
        self.seeker = Seeker()
        self.parachute = ["  __ ", " /___\ ", " \   / ", "  \ /  ", "   0  ", "  /|\   ", "  / \  ",  "", "^^^^^^^"]            

    def draw_parachute(self):
        """
        Draws the parachute in the form of a for loop iterating through a list.
        """
        for piece in self.parachute:
            self.console.write(piece)

    def cut_parachute(self):
        """
        Cut the parachute piece by getting rid of the first item in the list
        """
        self.parachute.pop(0)

    def check_parachute(self):
        """
        Determine if the parachute is over after checking the quantity of items in the list
        """
        return len(self.parachute) == 4

    def parachute_game_over(self):
        """
        If it's a game over, the head will be a X instead of a 0
        """
        self.parachute[0].replace('0', 'X')
