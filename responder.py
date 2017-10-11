import sys

class Responder:
    def __init__(self):
        #hello words to check
        self.helloWords = ["ciao", "salve"]        
        self.aboutWords = ["chi sei", "che fai"]

    def get_message (self, text):

        for hw in self.helloWords:
            if hw in text.lower():
                return "Ciao sfigato!"
        
        for aw in self.aboutWords:
            if aw in text.lower():
                return "Sono merdit e ti tengo aggiornato sui ritardi dei treni"
        
        return "Che vuoi? So solo dirti se un treno sta in ritardo. Mandami il numero"
