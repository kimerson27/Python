from Player import Player

class Game:
    def __init__(self):
        self.gameON = True
        self.player = Player(0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 1, 1, 1)
        self.game_statuses = {'Путешествие':0, 'Побег':1, 'Битва':2, 'Подготовка':3}
        self.game_status = self.game_statuses.get('Путешествие')

    # def update(self):
