"""
класс машина
положение наэкране в координатах x, y
скорость
здоровье
"""
from random import randint
from time import sleep
from typing import Union

import os
import keyboard
from models import login_user, read_users, Car, Lavel


def exit_game(user):
    """
    Возвращает выход из игры
    """
    user.save()
    sleep(1)
    exit()


def get_table():
    """
    Обновляет статистику пользователей
    """
    user.save()
    users = read_users()
    result = ""
    for something in users:
        result += f"{something}\n" 
    return result


def exit_menu(user) -> None:
    """
    диалог выхода из игры
    pause if key 'q' is pressed 
    """
    os.system('cls')
    keyboard.unhook_all()

    choice = input("Are you sure you want to exit? (Y|N)")

    if choice.lower() == "y":
        print('Exit!')
        exit_game(user)

    elif choice.lower() == "n":
        return None



def table_menu() -> None: 
    """
    Рейнтинг пользователя
    """
    os.system('cls')
    keyboard.unhook_all()
    print(get_table())

    choice = input("Press any key to exit  \n")
    return None


def car_gameplay(car: Car, user) -> None:
    """
    Как управлять машинкой
    """
    if keyboard.is_pressed("a"):
        if car.place_x > 1:
            car.place_x -= 1

    elif keyboard.is_pressed("d"):
        if car.place_x < 8:
            car.place_x += 1

    elif keyboard.is_pressed("w"):
        if car.place_y > 0:
            car.place_y -= 1

    elif keyboard.is_pressed("s"):
        if car.place_y < 9:
            car.place_y += 1
    
    elif keyboard.is_pressed("q"):
        exit_menu(user)
        
    elif keyboard.is_pressed("t"):
        table_menu()


if __name__ == "__main__":

    user = login_user()

    level = Lavel(user=user)
    car = Car(place_x=5, place_y=9)
    latancy = 0.2

    while True:
        
        sleep(latancy)
        # print(car1)
        # car1.move()

        # clear screen
        os.system('cls')

        # обновим данные пользователя +10 очков
        user.update()
        
        # печать уровня
        level.print(car)

        # рассчет столкновения машины и препятствий
        if level.collision(car) == True:
            print('You are LOSE!')
            print(f"You got {user.score} points!!! {user.message}")
            exit_game(user)

        # перемещение машины
        car_gameplay(car, user)
        
        if latancy > 0.05:
            latancy -= 0.001  

