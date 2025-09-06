from src.dni import Dni


class Controlador:

    def __init__(self,dni):
        self.dni = dni
        self.letter = ""
        self.numbers = ""

    def getDni(self):

        return self.dni

    def checkNumbersDni(self):
        
        dni = self.getNumbers()
        for char in dni.split():
            if char.isdigit():
                continue
            else:
                return False
        return True
    
    def checkValidLetter(self):

        letter = self.getLetter()

        True if letter.isalpha() else False



    def getDni(self):

        return self.dni

    def setLetter(self,char):

        self.Letter = self.dni[::-1]

    def setNumbers(self):

        self.Numbers = self.dni[:9]

    def getLetter(self):

        return self.letter

    def getNumbers(self):

        return self.numbers