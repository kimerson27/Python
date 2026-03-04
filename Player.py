from Entity import Entity

class Player (Entity):
    def __init__(self, LVL, EXP, EXP_UP, HP, MP, STM, Streng, Agility, Endurance, Intelligence, Luck):
        """
        :param LVL: INT
        :param EXP: FLOAT
        :param EXP_UP: FLOAT
        :param HP: FLOAT
        :param MP: FLOAT
        :param STM: FLOAT
        :param Streng: INT
        :param Agility: INT
        :param Endurance: INT
        :param Intelligence: INT
        :param Luck: INT
        """
        super().__init__(LVL, EXP, EXP_UP, HP, MP, STM, Streng, Agility, Endurance, Intelligence, Luck)
