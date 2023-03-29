
from random import randint
from constants import EMPTY_LEVEL, EMPTY_LINE, BASE_STR, color_db


class User:
    #класс пользователей который содержит поля: name, score, date, lavel
    def __init__(
        self, 
        name, 
        score, 
        date, 
        level
    ) -> None:

        self.name = name

        # пример обработки ошибки
        try:
            self.score = int(score)
        except BaseException:
            self.score = 0

        self.date = date
        self.level = int(level)

    def __repr__(self) -> str:
        # TODO сделать переносы строк
        return f"His name is {self.name}!!!!!!!!!! Currently he has {self.score}. (idk what to say here, but {self.date}.) He is in {self.level} right now!!!!!!!!!!\n"
    
    def __str__(self) -> str:
        return f"Name: {self.name} score: {self.score} level: {self.level}"
    
    @property
    def text(self):
        # метод text должен возвращать строку вида:
        return f"{self.name},{self.score},{self.date},{self.level}\n"

    def update(self):
        self.score += 10
        if self.score <= 120:
            self.message = "bruh, so bad..."
        elif self.score > 120 and self.score <= 300:
            self.message = "Not so bad."
        elif self.score > 300 and self.score <= 500:
            self.message = "Good. Pretty good."
        elif self.score > 500 and self.score <= 900:
            self.message = "Very good!"
        elif self.score > 900 and self.score <= 1500:
            self.message = "Awesome!"
        elif self.score > 1500 and self.score <= 3000:
            self.message = "So high score!!!"
        elif self.score > 3000:
            self.message = "YOU ARE THE BEST!!!!!!"
    


    def save(self):
        users = read_users()
        new_users = []
        for user in users:
            if self.name == user.name:
                new_users.append(self)
            else:
                new_users.append(user)
        
        wrigth_users(new_users)

def wrigth_users(_users:...) -> ...:
    """
    Запись в файл
    """
    my_file = open("users.db", "w")

    def get_key(item: User):
        return item.score
    
    _users = sorted(_users, key=get_key, reverse=True)
    for user in _users:
        my_file.write(user.text)
    my_file.close()

def read_users() -> list[User]:
    """
    Функция читает данные из файла с пользователями и возвращает список пользователей
    """
    users = []
    
    # чтение из файла
    my_file = open("users.db", "r")
    for line in my_file:
        # "Joan Koner,1241324,2023.07.06,999"
        # ["Joan Koner", "1241324", "2023.07.06" ", "999\n"]
        line = line.replace("\n", "")

        # line разбить по ,
        _result = line.split(",")

        # конвертировать список в кортэж
        _result = tuple(_result)

        # создать объект пользователя и
        # добавить прочитанного пользователя в список users
        users.append(User(*_result))
        
    my_file.close()
    return users



def login_user() -> User:
    """
    получает пользователей из файла users.db
    запрашивает имя пльзователя и ищет его в списке пользователей. 
    если пользователь найден, то возвращает его
    """
    users = read_users()
    
    # написать программу которая просит пользователя ввести имя
    name = input("WE NEED UR NAME FOR YOUR IP: ")
    
    for user in users:
        if name == user.name:
            print("STOP POSTING ABOUT CLONES *ip bans you*")
            print(user)
            return user
    
        
    # создать пользователя с таким именем
    new_user = User(name=name, score=0, date="2023-03-01",level=1)
    
    users.append(new_user)
    
    # записать всех пользователей в файл
    wrigth_users(users)
    return new_user


class Car:
    def __init__(
        self, 
        place_x:int, 
        place_y:int, 
        speed:int=0, 
        hp:int = 100
    ) -> None:
        self.place_x = place_x
        self.place_y = place_y
        self._speed = speed
        self._hp = hp
        self.speed_limit = 120
        self.score = 0

    def _speed_add(self):
        """
        Определяет скорость игры
        """
        # add speed limit
        if self._speed < self.speed_limit:
            self._speed += 1
        elif self._speed > self.speed_limit:
            self._speed = self.speed_limit
            

    def move(self):
        """
        Передвижение объекта
        """
        self.place_x += self._speed
        self._speed_add()

    def _health_subtract(self):
        """
        Урон объекту
        """
        self._hp -= 30
    
    def _break_speed(self):
        """
        Перерыв между действиями
        """
        self._speed = 0

    def collision(self):
        """
        Столкновение между объектами
        """
        self._break_speed()
        self._health_subtract()

    def __repr__(self):
        return f"""
        My car has {self._hp} hp, {self._speed} speed 
        and in {self.place_x}, {self.place_y} place 
        right now
        """


class Lavel:
    def __init__(self, user) -> None:
        self.data = EMPTY_LEVEL
        self._flag = 0
        self.user = user
    
    def _set_red_fields(self) -> None:
        """
        Уcтановка опасных клеток
        """
        p_1 = randint(1, 8)
        self.data[0][p_1] = 2
        self._flag = 3
    
    def update(self):
        """
        Обновляет поле
        """
        self.data.pop()
        self.data.insert(0, EMPTY_LINE.copy())
        # self.data.insert(0, EMPTY_LINE.deepcopy())
        if self._flag == 0:
            self._set_red_fields()
        else:
            self._flag -= 1

    def collision(self, car: Car) -> bool:
        """
        Возвращает столкновение
        """
        if self.data[car.place_y][car.place_x] == 2:
            # столкновение
            return True
        return False
        
    def print(self, car: Car) -> None:
        """
        Funtion for print screen
        """
        self.update()
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                
                if y == car.place_y and x == car.place_x:
                    print(BASE_STR % (color_db.blue, ' ® '), end="")

                elif self.data[y][x] == 1:
                    print(BASE_STR % (color_db.white, '   '), end="")

                elif self.data[y][x] == 2:
                    print(BASE_STR % (color_db.red, '   '), end="")

                elif self.data[y][x] == 0:
                    print(BASE_STR % (color_db.black, ' . '), end="")
            print()
        print("U score: ", self.user.score)
