from dni import Dni


class Controlador:

    def __init__(self,dni):
        self.dni = dni
        

    def getDni(self):

        return self.dni

    def checkNumbersDni(self):
        
        numbers = self.getDni()
        if len(numbers) == 8:
            return True
        else:
            return False
