import doctest


class Computer:
    def __init__(self, GPU_memory: int, CPU_brand: str, RAM_memory: int, RAM_strip_current: int, RAM_strip_max: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param GPU_memory: Объем памяти видеокарты
        :param CPU_brand: Производитель процессора
        :param RAM_memory: Общий объем памяти ОЗУ
        :param RAM_strip_current: Текущеее количество плашек ОЗУ
        :param RAM_strip_max: Максимально возможное количество плашек ОЗУ

        Пример:
        >>> work_01 = Computer(1, 'intel', 32, 2, 4) # инициализация экземпляра класса

        """

        if not isinstance(GPU_memory, int):
            raise TypeError("Объем памяти видеокарты должен быть целочисленным числом")
        if not isinstance(RAM_memory, int):
            raise TypeError("Объем памяти ОЗУ должен быть целочисленным числом")
        if not ( (CPU_brand == 'amd') or (CPU_brand == 'intel')):
            raise ValueError("Неизвестный бренд производителя процессора")
        if not isinstance(RAM_strip_current, int):
            raise TypeError("Текущее количество плашек ОЗУ должно быть целочисленным числом")
        if not isinstance(RAM_strip_current, int):
            raise TypeError("Максимальное количество плашек ОЗУ должно быть целочисленным числом")
        if RAM_strip_current > RAM_strip_max:
            raise ValueError("Текущее количество плашек ОЗУ не должно превышать максимальное количество")


        self.GPU_memory = GPU_memory
        self.CPU_brand = CPU_brand
        self.RAM_memory = RAM_memory
        self.RAM_strip_current = RAM_strip_current
        self.RAM_strip_max = RAM_strip_max

    def add_RAM_memory(self, additional_RAM_memory: int) -> None:
            """
            Функция необходима для того чтобы добавить новую плашку ОЗУ в компьютер

            :param self:
            :param additional_RAM_memory: объем памяти ОЗУ на новой плашке ОЗУ
            :return:

            Пример:
            >>> work_01 = Computer(1, 'intel', 32, 2, 4) # инициализация экземпляра класса
            >>> work_01.new_GPU(4)

            """
            if self.RAM_strip_current == self.RAM_strip_max:
                raise ValueError("Установлено максимальное количество плашек ОЗУ")
            if not isinstance(additional_RAM_memory, int):
                raise TypeError("Объем памяти ОЗУ должен быть целочисленным числом")

            self.RAM_memory += additional_RAM_memory
            self.RAM_strip_current += 1

    def new_GPU(self, new_GPU_memory: int) -> None:
            """
            Функция необходима для замены видеокарты на компьютере

            :param self: ссылка на атрибут класса Computer
            :param new_GPU_memory:
            :return: Новое значение памяти видеокарты

            Пример:
            >>> work_01 = Computer(1, 'intel', 32, 2, 4) # инициализация экземпляра класса
            >>> work_01.new_GPU(4)
            """
            if not isinstance(new_GPU_memory, int):
                raise TypeError("Объем памяти видеокарты должен быть целочисленным числом")

            self.GPU_memory = new_GPU_memory

    def launch_game(self, required_RAM_memory: int, required_GPU_memory: int) -> str:
            """
            Данная функция необходима для того, чтобы проверить получится ли запустить игру на компьютере.

            :param self: ссылка на атрибут класса Computer
            :param required_RAM_memory: необходимый объем памяти ОЗУ для запуска игры
            :param required_GPU_memory: необходимый объем памяти видеокарты для запуска игры
            :return: Запущена ли игра

            Пример:
            >>> work_01 = Computer(4, 'intel', 32, 2, 4) # инициализация экземпляра класса
            >>> result = work_01.launch_game(4, 2)
            """
            if not isinstance(required_RAM_memory, int):
                raise TypeError("Объем памяти ОЗУ должен быть целочисленным числом")
            if not isinstance(required_GPU_memory, int):
                raise TypeError("Объем памяти видеокарты должен быть целочисленным числом")
            if not self.RAM_memory >= required_RAM_memory:
                return 'Игра не запущена. Не хватает памяти ОЗУ для запуска игры'
            if not self.GPU_memory >= required_GPU_memory:
                return 'Игра не запущена. Не хватает памяти видеокарты для запуска игры'
            else:
                return 'Игра запущена'


class Human:

    def __init__(self, money: float, gender: str, age: int, stress: float):

        """
        Создание и подготовка к работе объекта "Человек"

        :param money: количество денег у человека
        :param gender: пол человека man или woman
        :param age: возраст человека
        :param stress: коэффициент стресса у человека

        Пример:
        >>> Natasha = Human(10000, 'woman', 23, 0.5) # инициализация Наташи

        """

        if not ( (gender == 'man') or (gender == 'woman')):
            raise ValueError("ошибка при вводе пола человека, напишите man или woman")
        if not isinstance(age, int):
            raise TypeError("Возраст человека должен быть целочисленным числом")
        if not isinstance(money, (float, int)):
            raise TypeError("Количество денег должно быть числом")
        if money < 0:
            raise ValueError("Количество денег должно быть положительным число")
        if not ((stress >= 0) and (stress <= 1)):
            raise ValueError("Коэффициент стресса должен быть от одного до нуля")

        self.gender = gender
        self.money = money
        self.age = age
        self.stress = stress

    def buy_beer(self, price_beer) -> str:

        """
        Функция позволяет выпить пиво для того, чтобы снизить уровень стресса

        :param price_beer: цена на пиво в пятерочке

        :return: новый уровень стресса и количестсва денег

        Пример:
        >>> Natasha = Human(10000, 'woman', 23, 0.5) # инициализация Наташи
        >>> result = Natasha.buy_beer(75)

        """
        if not isinstance(price_beer, (int, float)):
            raise TypeError("Введите положительное число")
        if not price_beer > 0:
            raise ValueError("Цена пива должна быть положительной")
        if self.age < 18:
            return 'Еще нельзя'
        if self.money < price_beer:
            return 'Не хватает денег'
        else:
            self.money -= price_beer
            if (self.stress < 0.9) and (self.stress > 0.1):
                self.stress -= 0.1
            if self.stress >= 0.9:
                self.stress = 1
            if self.stress <= 0.1:
                self.stress = 0
            return 'Пиво куплено'

    def work(self, salary):

        """
        Функция отправляет человека на работу, при этом он получает там зарплату и устает

        :param salary: зарплата человека

        :return: новый уровень стресса и количестсва денег

        Пример:
        >>> Natasha = Human(10000, 'woman', 23, 0.5) # инициализация Наташи
        >>> result = Natasha.work(5000)

        """
        if not isinstance(salary, (int, float)):
            raise TypeError("Введите положительное число")
        if not salary > 0:
            raise ValueError("Зарплата должна быть положительной")
        if self.stress > 0.8:
            return 'Человек больше не может работать'
        else:
            self.money += salary
            self.stress += 0.2
            return 'Вы успешно поработали'




class fridge:

    def __init__(self, door: bool, occupancy: float):
        """

        :param door: переменная отвечает за то, открыта ли дверь. True - дверь открыта
        :param occupancy: занятость холодильника от 0 до 1, где 1 - полностью занят

        Пример:
        >>> Fridge_01 = fridge(True, 0.7)
        """
        if not isinstance(door, bool):
            raise TypeError("")
        if not isinstance(occupancy, (float, int)):
            raise TypeError("")
        if not (occupancy <= 1) and (occupancy >= 0):
            raise ValueError("")

        self.door = door
        self.occupancy =  occupancy

    def open_door(self):

        """
        Функуия открывает дверь от холодильника

        Пример:
        >>> Fridge_01 = fridge(True, 0.7)
        >>> res = Fridge_01.open_door()

        """
        if self.door is True:
            return 'Дверь и так открыта'
        if self.door is False:
            self.door = True
            return 'Дверь открыта'

    def close_door(self):
        """
        Функуия закрывает дверь от холодильника

        Пример:
        >>> Fridge_01 = fridge(True, 0.7)
        >>> res = Fridge_01.close_door()

        """
        if self.door is False:
            return 'Дверь и так закрыта'
        if self.door is True:
            self.door = False
            return 'Дверь закрыта'

    def put_item(self, item_occupancy):
        """
        Функция кладет в холодильник предмет

        :param item_occupancy: объем занимаемого простраснтва предмета относильно объема холодильника

        Пример:
        >>> Fridge_01 = fridge(True, 0.7)
        >>> res = Fridge_01.put_item(0.5)
        """
        if not (item_occupancy <= 1) and (item_occupancy >= 0):
            raise ValueError("")
        if (self.door is True) and (self.occupancy + item_occupancy <= 1):
            return "Предмет теперь в холодильнике"
        if self.door is False:
            return "Откройте дверь"
        if self.occupancy + item_occupancy <= 1:
            return "В холодильнике не хватает места"




if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
