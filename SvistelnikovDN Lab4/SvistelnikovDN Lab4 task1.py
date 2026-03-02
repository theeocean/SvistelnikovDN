from abc import ABC, abstractmethod
from typing import Optional, Union


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.

    Инкапсуляция: атрибуты _brand и _model защищены от прямого изменения,
    так как они являются основными характеристиками транспортного средства
    и не должны меняться после создания объекта.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: int) -> None:
        """
        Инициализация базового транспортного средства.

        Args:
            brand: Производитель транспортного средства
            model: Модель транспортного средства
            year: Год выпуска
            max_speed: Максимальная скорость (км/ч)
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._max_speed = max_speed
        self._current_speed = 0

    def __str__(self) -> str:
        """Строковое представление для пользователей."""
        return f"{self._brand} {self._model} ({self._year} г.)"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчиков."""
        return f"{self.__class__.__name__}(brand='{self._brand}', model='{self._model}', year={self._year})"

    def accelerate(self, speed_increase: int) -> int:
        """
        Увеличение текущей скорости.

        Args:
            speed_increase: Значение увеличения скорости

        Returns:
            Текущая скорость после увеличения
        """
        new_speed = self._current_speed + speed_increase
        if new_speed <= self._max_speed:
            self._current_speed = new_speed
        else:
            self._current_speed = self._max_speed
        return self._current_speed

    def brake(self, speed_decrease: int) -> int:
        """
        Уменьшение текущей скорости.

        Args:
            speed_decrease: Значение уменьшения скорости

        Returns:
            Текущая скорость после уменьшения
        """
        new_speed = self._current_speed - speed_decrease
        if new_speed >= 0:
            self._current_speed = new_speed
        else:
            self._current_speed = 0
        return self._current_speed

    @abstractmethod
    def get_vehicle_type(self) -> str:
        """Абстрактный метод для получения типа транспортного средства."""
        pass


class PassengerCar(Vehicle):
    """
    Класс легкового автомобиля, наследующийся от Vehicle.

    Расширяет базовый класс дополнительными атрибутами, специфичными для легковых авто.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: int,
                 body_type: str, passenger_capacity: int) -> None:
        """
        Инициализация легкового автомобиля.

        Расширение конструктора базового класса добавлением специфичных атрибутов.

        Args:
            brand: Производитель
            model: Модель
            year: Год выпуска
            max_speed: Максимальная скорость
            body_type: Тип кузова (седан, хэтчбек, универсал и т.д.)
            passenger_capacity: Вместимость пассажиров
        """
        super().__init__(brand, model, year, max_speed)
        self._body_type = body_type
        self._passenger_capacity = passenger_capacity
        self._current_passengers = 0

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для добавления информации о типе кузова.

        Причина перегрузки: для легкового автомобиля важно указать тип кузова,
        так как это ключевая характеристика для данного типа транспорта.
        """
        base_str = super().__str__()
        return f"{base_str}, тип кузова: {self._body_type}"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для включения специфичных атрибутов.

        Причина перегрузки: необходимо включить в официальное представление
        все атрибуты, специфичные для легкового автомобиля.
        """
        return (f"PassengerCar(brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, body_type='{self._body_type}')")

    def get_vehicle_type(self) -> str:
        """Реализация абстрактного метода базового класса."""
        return "Легковой автомобиль"

    def board_passenger(self) -> Optional[str]:
        """
        Метод посадки пассажира в автомобиль.

        Returns:
            Сообщение о результате посадки или None при успехе
        """
        if self._current_passengers < self._passenger_capacity:
            self._current_passengers += 1
            return None
        return "Нет свободных мест"

    def accelerate(self, speed_increase: int) -> int:
        """
        Перегрузка метода ускорения с учетом количества пассажиров.

        Причина перегрузки: динамика разгона легкового автомобиля зависит
        от загруженности. Чем больше пассажиров, тем медленнее разгон.
        """
        # Уменьшаем эффективность разгона при полной загрузке
        if self._current_passengers == self._passenger_capacity:
            speed_increase = speed_increase // 2

        return super().accelerate(speed_increase)


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующийся от Vehicle.

    Расширяет базовый класс атрибутами для работы с грузом.
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: int,
                 cargo_capacity: int, has_trailer: bool = False) -> None:
        """
        Инициализация грузового автомобиля.

        Args:
            brand: Производитель
            model: Модель
            year: Год выпуска
            max_speed: Максимальная скорость
            cargo_capacity: Грузоподъемность (кг)
            has_trailer: Наличие прицепа
        """
        super().__init__(brand, model, year, max_speed)
        self._cargo_capacity = cargo_capacity
        self._has_trailer = has_trailer
        self._current_cargo_weight = 0

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для добавления информации о грузоподъемности.

        Причина перегрузки: для грузового автомобиля ключевой характеристикой
        является грузоподъемность, которую важно отображать.
        """
        base_str = super().__str__()
        trailer_info = "с прицепом" if self._has_trailer else "без прицепа"
        return f"{base_str}, грузоподъемность: {self._cargo_capacity}кг, {trailer_info}"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для включения специфичных атрибутов.
        """
        return (f"Truck(brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, cargo_capacity={self._cargo_capacity})")

    def get_vehicle_type(self) -> str:
        """Реализация абстрактного метода базового класса."""
        return "Грузовой автомобиль"

    def load_cargo(self, weight: int) -> Optional[str]:
        """
        Метод загрузки груза.

        Args:
            weight: Вес загружаемого груза (кг)

        Returns:
            Сообщение о результате загрузки или None при успехе
        """
        if self._current_cargo_weight + weight <= self._cargo_capacity:
            self._current_cargo_weight += weight
            return None
        return "Превышение грузоподъемности"

    def accelerate(self, speed_increase: int) -> int:
        """
        Перегрузка метода ускорения с учетом загруженности и прицепа.

        Причина перегрузки: грузовые автомобили имеют меньшую динамику
        разгона при полной загрузке и особенно при наличии прицепа.
        Это критически важно учитывать для безопасности.
        """
        # Коэффициент загруженности
        load_ratio = self._current_cargo_weight / self._cargo_capacity if self._cargo_capacity > 0 else 0

        # Уменьшаем разгон в зависимости от загрузки
        if load_ratio > 0.7:
            speed_increase = int(speed_increase * 0.6)
        elif load_ratio > 0.3:
            speed_increase = int(speed_increase * 0.8)

        # Дополнительное замедление при наличии прицепа
        if self._has_trailer:
            speed_increase = int(speed_increase * 0.7)

        return super().accelerate(speed_increase)


if __name__ == "__main__":
    # Примеры использования
    car = PassengerCar("Toyota", "Camry", 2022, 220, "седан", 5)
    truck = Truck("Volvo", "FH16", 2021, 140, 20000, has_trailer=True)

    print(car)  # Toyota Camry (2022 г.), тип кузова: седан
    print(repr(car))  # PassengerCar(brand='Toyota', model='Camry', year=2022, body_type='седан')
    print(car.get_vehicle_type())  # Легковой автомобиль

    car.board_passenger()
    print(car.accelerate(50))  # Ускорение с учетом пассажиров

    print(truck)  # Volvo FH16 (2021 г.), грузоподъемность: 20000кг, с прицепом
    print(repr(truck))  # Truck(brand='Volvo', model='FH16', year=2021, cargo_capacity=20000)
    print(truck.get_vehicle_type())  # Грузовой автомобиль