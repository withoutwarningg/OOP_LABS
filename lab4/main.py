class Transport:
    """
    Базовый класс для транспортных средств
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация объекта Transport

        : brand: Марка транспортного средства
        : model: Модель транспортного средства
        : year: Год выпуска транспортного средства
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Transport

        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Transport для отображения в коде
        """
        return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year={self.year})"


class Car(Transport):
    """
    Дочерний класс для автомобилей
    """
    def __init__(self, brand: str, model: str, year: int, color: str, fuel_type: str):
        """
        Инициализация объекта Car

        : brand: Марка автомобиля
        : model: Модель автомобиля
        : year: Год выпуска автомобиля
        : color: Цвет автомобиля
        : fuel_type: Тип топлива, используемый автомобилем
        """
        super().__init__(brand, model, year)
        self.color = color
        self.fuel_type = fuel_type

    def honk(self) -> str:
        """
        Издать звук автомобильного гудка
        """
        return "Beep Beep!"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Car

        """
        return f"{super().__str__()}, {self.color}, {self.fuel_type} car"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Car для отображения в коде

        """
        return f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year={self.year}, color={self.color}, fuel_type={self.fuel_type})"
