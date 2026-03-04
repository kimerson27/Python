from Game import Game

game = Game()
game.gameON = True

game_status_main_menu ="""
1. Продолжить.
2. Загрузить игру. 
3. Новая игра.
4. Выход
"""

game_status_in_battle = """
0. Открыть меню.
1. Атаковать.
2. Защищаться
3. Сменить стойку 
4. Открыть инвентарь
5. Быстрый слот 1
6. Быстрый слот 2
7. Быстрый слот 3
8. Быстрый слот 4
9. Быстрый слот 5
"""

game_status_menu = """
0. Назад
1. Продолжить.
2. Выйти
"""



while game.gameON:
    # Выбор действия игрока
    while True:
        # TODO: Сделать проверку статуса игры. Если игрок находится в боевом режиме, вызывать только боевое меню

        if game.game_statuses.get('Путешествие') == game.game_status:
            game.game_status = game.game_statuses.get('Бой')

        if game.game_statuses.get('Побег') == game.game_status:
            game.game_status = game.game_statuses.get('Бой')

        if game.game_statuses.get('Битва') == game.game_status:
            game.game_status = game.game_statuses.get('Бой')

        if game.game_statuses.get('Подготовка') == game.game_status:
            game.game_status = game.game_statuses.get('Бой')

        print(game_status_in_battle, end="")

        if int(input("Введите значение: ")) == 0:
            print(game_status_menu, end="")

            if int(input("Введите значение: ")) == 2:
                game.gameON = False

                break
