import random

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
        self._word = ['cow', 'rabbit', 'radio', 'fish', 'potato', 'phone', 'video', 'taco', 'cake', 'moon', 'soap', 'music', 'movie', 'water', 'flower', 'dance', 'play', 'watch']
            
    def get_word(self):
        """Gets the list of words.
            
        Returns:
            A random word from the list,
        """
        return random.choice(self._word)
        