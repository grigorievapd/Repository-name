# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Milk:
    def __init__(self, bottle_volume: float, milk_volume: float, shelf_life: float):
        """
        Создание и подготовка к работе объекта "Молоко"
        :param bottle_volume: Объем бутылки
        :param milk_volume: Объем молока в бутылке
        :param shelf_life: Срок годности в днях
        Примеры:
        »> milk = Milk(1000,500,15) #инициализация экземпляра класса
        """
        if not isinstance(bottle_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if bottle_volume <= 0:
            raise TypeError("Объем бутылки должен быть положительным числом")
        self.bottle_volume = bottle_volume

        if not isinstance(milk_volume, (int, float)):
            raise TypeError("Объем молока должен быть типа int или float")
        if milk_volume < 0:
            raise TypeError("Объем молока не может быть отрицательным числом")
        self.milk_volume = milk_volume

        if not isinstance(shelf_life, (int, float)):
            raise TypeError("Срок годности должен быть типа int или float")
        if shelf_life < 0:
            raise TypeError("Срок годности не может быть отрицательным числом")
        self.shelf_life = shelf_life


    def is_empty_bottle(self) -> bool:
        """
        Функция, которая проверяет, является ли бутылка молока пустой
        :return: Является ли бутылка молока пустой
        Примеры:
        >>> milk = Milk(1000,0, 15)
        >>> milk.is_empty_bottle()
        """

    def remove_milk_from_bottle(self, milk_volume: float) -> None:
        """
        Отлить молоко из бутылки.

        :param milk_volume: Объем требуемого молока
        :raise ValueError: Если количество требуемого молока превышает количество молока в бутылке,
        то возвращается ошибка.
        :return: Объем оставшегося молока
        Примеры:
        >>> milk = Milk(1000, 500, 15)
        >>> milk.remove_milk_from_bottle(50)
        """
        ...

    def milk_expired(self)-> bool:
        """
        Функция которая проверяет испорчено ли молоко.
        :return: Является ли молоко испорченным
        Примеры:
        >>> milk = Milk(1000,500,0)
        >>> milk.milk_expired()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
