import enum

@enum.unique
class Statuses (enum.Enum):

    # TODO: Добавить все необходимые статусы
    none        = 0

    # Стихийные статусы
    burn        = 101 # Горения
    freeze      = 102 # Заморозка льдом
    wet         = 103 # Мокрый
    electric    = 104 # Поражение электричеством
    toxin       = 105 # Токсичные вещества
    poison      = 106 # Отравление
    acid        = 107 # Кислота

    # Отрицательные статусы
    stun        = 201 # Эффект остановки/замирания
    blind       = 202

    # Положительные статусы
    invisible   = 300 # Невидимость
    stealth     = 300 # Повышение скрытности



class Status:

    # TODO: Продумать какие параметры должны быть эффекта статуса (Пример: урон, длительность и т.д.)
    def __init__(self):
        self.percentage = 0
        self.power      = 0
        self.duration   = 0
        self.stability  = 0
        self.damage     = 0
        self.quality    = 0
        self.streng     = 0

        self.type       = Statuses.none