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
        """Gets a random word from the list of words.
            
        Returns:
            A random word from the list.
        """
        return random.choice(self._word)

    def guess(self, letter):
            
        for x in range(0, len(self._word)):
            if letter == self._word[x]:
                self._word[x] = letter
        