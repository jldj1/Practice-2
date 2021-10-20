from languages.english import English
from languages.spanish import Spanish
from languages.french import French



class BlackjackGame:
    def __init__(self):
        self.storage = {}

    def addPlayer(self, player_name, lang):
        if player_name not in self.storage:
            self.storage[player_name] = Player(player_name, 100, lang)
            return True
           
        return False

    def getPlayerCash(self, name):
        return self.storage[name].getCash()

    def getAllPlayers(self):
        print(self.storage)

    def startGame(self):

        for name, player_object in self.storage.items():
            print(name, player_object.getLang().start())

class Player: 
    def __init__(self, name, cash, lang):
        self.name = name
        self.cash = cash
        self.lang = lang

    def getCash(self):
        return self.cash

    def getLang(self):
        return self.lang


game1 = BlackjackGame()

lang = English
option = input("select language:")
if option == "es":
    lang = Spanish
elif option == "fr":
    lang = French


game1.addPlayer("Chris", lang)
game1.addPlayer("Jessie", English)
game1.addPlayer("Robert", Spanish)
game1.getAllPlayers()
game1.startGame()
