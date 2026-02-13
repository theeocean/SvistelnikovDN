import doctest
from typing import Union


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        self.current_page = 1

    def open_book(self, page: int) -> None:
        """
        Открыть книгу на определенной странице.

        :param page: Номер страницы для открытия
        :raise ValueError: Если номер страницы меньше 1 или больше общего количества страниц

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 320)
        >>> book.open_book(50)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page < 1 or page > self.pages:
            raise ValueError(f"Страница должна быть от 1 до {self.pages}")
        ...

    def get_progress(self) -> float:
        """
        Получить прогресс чтения книги в процентах.

        :return: Процент прочитанных страниц

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 400)
        >>> book.open_book(100)
        >>> book.get_progress()
        25.0
        """
        ...

    def add_bookmark(self, page: int) -> None:
        """
        Добавить закладку на странице.

        :param page: Номер страницы для закладки
        :raise ValueError: Если номер страницы недопустим

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.add_bookmark(125)
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Производитель смартфона
        :param model: Модель смартфона
        :param battery_capacity: Емкость аккумулятора в мАч

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        """
        if not isinstance(brand, str):
            raise TypeError("Производитель должен быть строкой")
        if not brand.strip():
            raise ValueError("Производитель не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model.strip():
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity
        self.battery_level = 100
        self.is_on = False

    def turn_on(self) -> None:
        """
        Включить смартфон.

        :raise RuntimeError: Если смартфон уже включен или разряжен

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 3900)
        >>> phone.turn_on()
        """
        ...

    def charge_battery(self, minutes: int) -> None:
        """
        Зарядить аккумулятор смартфона.

        :param minutes: Время зарядки в минутах
        :raise ValueError: Если время зарядки отрицательное

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 5000)
        >>> phone.charge_battery(30)
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть целым числом")
        if minutes < 0:
            raise ValueError("Время зарядки не может быть отрицательным")
        ...

    def take_photo(self) -> None:
        """
        Сделать фотографию на камеру смартфона.

        :raise RuntimeError: Если смартфон выключен

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 7", 4355)
        >>> phone.turn_on()
        >>> phone.take_photo()
        """
        ...


class CoffeeMachine:
    def __init__(self, water_tank_volume: int, coffee_beans_capacity: int, milk_tank_volume: Union[int, None] = None):
        """
        Создание и подготовка к работе объекта "Кофемашина"

        :param water_tank_volume: Объем резервуара для воды в мл
        :param coffee_beans_capacity: Вместимость контейнера для кофейных зерен в граммах
        :param milk_tank_volume: Объем резервуара для молока в мл (опционально, для моделей с капучинатором)

        Примеры:
        >>> coffee_machine = CoffeeMachine(1500, 250, 500)
        >>> simple_coffee_machine = CoffeeMachine(1200, 200)  # модель без капучинатора
        """
        if not isinstance(water_tank_volume, int):
            raise TypeError("Объем резервуара для воды должен быть целым числом")
        if water_tank_volume <= 0:
            raise ValueError("Объем резервуара для воды должен быть положительным числом")
        self.water_tank_volume = water_tank_volume
        self.water_level = 0

        if not isinstance(coffee_beans_capacity, int):
            raise TypeError("Вместимость контейнера для кофе должна быть целым числом")
        if coffee_beans_capacity <= 0:
            raise ValueError("Вместимость контейнера для кофе должна быть положительным числом")
        self.coffee_beans_capacity = coffee_beans_capacity
        self.coffee_beans_level = 0

        if milk_tank_volume is not None:
            if not isinstance(milk_tank_volume, int):
                raise TypeError("Объем резервуара для молока должен быть целым числом")
            if milk_tank_volume <= 0:
                raise ValueError("Объем резервуара для молока должен быть положительным числом")
        self.milk_tank_volume = milk_tank_volume
        self.milk_level = 0
        self.is_on = False

    def make_espresso(self) -> None:
        """
        Приготовить порцию эспрессо.

        :raise RuntimeError: Если недостаточно воды или кофе

        Примеры:
        >>> coffee_machine = CoffeeMachine(1500, 250)
        >>> coffee_machine.add_water(1000)
        >>> coffee_machine.add_coffee_beans(200)
        >>> coffee_machine.turn_on()
        >>> coffee_machine.make_espresso()
        """
        ...

    def add_water(self, volume: int) -> None:
        """
        Добавить воду в резервуар кофемашины.

        :param volume: Объем добавляемой воды в мл
        :raise ValueError: Если объем превышает свободное место в резервуаре

        Примеры:
        >>> coffee_machine = CoffeeMachine(2000, 300)
        >>> coffee_machine.add_water(1500)
        """
        if not isinstance(volume, int):
            raise TypeError("Объем воды должен быть целым числом")
        if volume <= 0:
            raise ValueError("Объем воды должен быть положительным числом")
        ...

    def turn_on(self) -> None:
        """
        Включить кофемашину.

        :raise RuntimeError: Если кофемашина уже включена

        Примеры:
        >>> coffee_machine = CoffeeMachine(1800, 280)
        >>> coffee_machine.turn_on()
        """
        ...


if __name__ == "__main__":
    doctest.testmod(verbose=True)  # тестирование примеров, которые находятся в документации