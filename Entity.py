from Status import *

class Entity:
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

        # Показатели уровня
        self.LVL = LVL
        # Текущий показатель опыта
        self.EXP = EXP
        # Необходимое количество опыта для поднятия уровня
        self.EXP_UP = EXP_UP

        # Показатели статус-бара
        self.HP = HP
        self.MP = MP
        self.STM = STM

        # Показатели прокачки
        self.streng = Streng
        self.agility = Agility
        self.endurance = Endurance
        self.intelligence = Intelligence
        self.luck = Luck

        #
        self.status = list[Status]


        # TODO: пересмотреть расчет урона
        def attack ():
            return self.streng

        # TODO: Добавить следующие показатели к свойствам ПЕРСОНАЖЕЙ
        # Cила
        # Сопротивление
        # Атлетика
        # Ловкость
        # Акробатика
        # Ловкость
        # рук
        # Скрытность
        # Интеллект
        # История
        # Магия
        # Природа
        # Расследование
        # Религия
        # Мудрость
        # Восприятие
        # Выживание
        # Медицина
        # Проницательность
        # Уход за животными
        # Харизма
        # Выступление
        # Запугивание
        # Обман
        # Убеждение

