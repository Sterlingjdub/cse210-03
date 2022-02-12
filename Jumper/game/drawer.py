from ast import For


class Drawer():

    def __init__(self):
        self.estado = 1
    
    def draw(self):
        if(self.estado == 1):
            print("  ___\n /___\\ \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 2):
            print(" \n /___\\ \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 3):
            print(" \n \\   /\n  \\ /\n   0 \n  /|\\ \n  / \\")

        elif(self.estado == 4):
            print("\n  \\ /\n   0 \n  /|\\ \n  / \\")
        
        else:
            print("\n   x \n  /|\\ \n  / \\")
        print("^^^^^^^")

    def updateState(self):
        self.estado = self.estado + 1

    def drawWord(self, word, letters):
        #print(word)
        #print(letters)
        i = 0 
        l = len(word)
        while i < l:
            if (word[i] in letters):
                print(word[i], end="")
            else:
                print("_",end="")
            i = i + 1
        print()