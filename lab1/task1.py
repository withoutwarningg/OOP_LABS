from abc import ABC, abstractmethod
from typing import Union, List

class PhysicalObject(ABC):
    """
    Абстрактный класс, описывающий материальные объекты.

    Attributes:
        name (str): Название объекта.
        weight (float): Вес объекта в килограммах.
        material (str): Материал, из которого сделан объект.

    Methods:
        move(self, destination: str) -> str:
            Перемещает объект в указанное место.

        break_object(self) -> str:
            Разрушает объект.

    Примеры:
    >>> obj = ConcretePhysicalObject("Table", 50.0, "Wood")
    >>> obj.move("Living Room")
    'Object moved to Living Room'

    >>> obj.break_object()
    'Object is broken'
    """
    def __init__(self, name: str, weight: float, material: str):
        self.name = name
        self.weight = weight
        self.material = material

    @abstractmethod
    def move(self, destination: str) -> str:
        """Перемещает объект в указанное место."""
        ...

    @abstractmethod
    def break_object(self) -> str:
        """Разрушает объект."""
        ...


class LivingBeing(ABC):
    """
    Абстрактный класс, описывающий живые существа.

    Attributes:
        name (str): Имя существа.
        age (int): Возраст существа.
        species (str): Вид существа.

    Methods:
        eat(self, food: str) -> str:
            Существо питается указанным видом пищи.

        sleep(self, hours: int) -> str:
            Существо засыпает на указанное количество часов.


    """
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

    @abstractmethod
    def eat(self, food: str) -> str:
        """Существо питается указанным видом пищи."""
        ...

    @abstractmethod
    def sleep(self, hours: int) -> str:
        """Существо засыпает на указанное количество часов."""
        ...


class DigitalEntity(ABC):
    """
    Абстрактный класс, описывающий цифровые сущности.

    Attributes:
        name (str): Название цифровой сущности.
        data (List[Union[int, str]]): Данные, связанные с цифровой сущностью.
        encryption_key (str): Ключ шифрования данных.

    Methods:
        upload_data(self, data: List[Union[int, str]]) -> str:
            Загружает новые данные в цифровую сущность.

        encrypt_data(self) -> str:
            Шифрует данные цифровой сущности с использованием ключа.


    """
    def __init__(self, name: str, data: List[Union[int, str]], encryption_key: str):
        self.name = name
        self.data = data
        self.encryption_key = encryption_key

    @abstractmethod
    def upload_data(self, data: List[Union[int, str]]) -> str:
        """Загружает новые данные в цифровую сущность."""
        ...

    @abstractmethod
    def encrypt_data(self) -> str:
        """Шифрует данные цифровой сущности с использованием ключа."""
        ...
