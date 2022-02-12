import random
from game.drawer import Drawer

class Word:
    """The word that will be used for the jumper game
    
    Attributes:
        _word (List[str]): The list of words
    """

    def __init__(self):
        """Constructs a list of words from which one will be chosen for the game.

        Args:
            self (Word): An instance of Word.
        """
        self._words = ['cow', 'rabbit', 'radio', 'fish', 'potato', 'phone', 'video', 'taco', 'cake', 'moon', 'soap', 'music', 'movie', 'water', 'flower', 'dance', 'play', 'watch']
        self._word =  self.get_word()   
        self.drawer = Drawer()

    def get_word(self):
        """Gets a random word from the list of words.
            
        Returns:
            A random word from the list.
        """
        return random.choice(self._words)

    def guess(self, letter, pos):
        
        if (letter in self._word):
            return True
        else:
            return False
    
    def showDraw(self, letters):
        self.drawer.drawWord(self._word, letters)
        self.drawer.draw()

    def updateState(self):
        self.drawer.updateState()