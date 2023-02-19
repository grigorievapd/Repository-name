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



class Hospital:
    def __init__(self, hospital_beds : int, number_of_patients: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param hospital_beds: Количество больничных коек
        :param number_of_patients: Количество пациентов
        Примеры:
        »> hospital = Hospital(45, 0) #инициализация экземпляра класса
        """
        if not isinstance(hospital_beds, (int, float)):
            raise TypeError("Количество больничных коек должно быть типа int или float")
        if hospital_beds <= 0:
            raise TypeError("Количество больничных коек должно быть положительным числом")
        self.hospital_beds = hospital_beds

        if not isinstance(number_of_patients, (int, float)):
            raise TypeError("Количество пациентов должно быть типа int или float")
        if number_of_patients < 0:
            raise TypeError("Количество пациентов не может быть отрицательным числом")
        self.number_of_patients = number_of_patients


    def is_hospital_full(self) -> bool:
        """
        Функция, которая проверяет, является ли больница заполненной
        :return: Больница заполнена
        Примеры:
        »> hospital = Hospital(145,145)
        »> hospital.is_hospital_full()
        """

    def hospitalize(self, patients: int) -> int:
        """
        Функция заправки автомобиля
        :param patients: Количество пациентов, которым необходимо лечь в больницу
        :raise ValueError: Если количество пациентов превышает свободные койки
        Примеры:
        »> hospital = Hospital(145,120)
        »> hospital.hospitalize(15)
        """
        if not isinstance(patients, (int)):
            raise TypeError("Количество пациентов, которым необходимо лечь в больницу должно быть типа int")
        if patients <= 0:
            raise ValueError("Количество пациентов, которым необходимо лечь в больницу должно быть положительным числом")



class Kindergarten:
    def __init__(self, number_of_children: float, number_of_boys: float, number_of_girls: float):
        """
        Создание и подготовка к работе объекта "Детский сад"
        :param number_of_children: Количество детей в группе
        :param name_of_child: Имена детей
        Примеры:
        »> сlass = Class(25,15,10) #инициализация экземпляра класса
        """
        if not isinstance(number_of_children, (int)):
            raise TypeError("Количество детей в классе должно быть типа int")
        if number_of_children <= 0:
            raise TypeError("Количество детей в классе должно быть положительным числом")
        self.number_of_children = number_of_children

        if not isinstance(name_of_child, str):
            raise TypeError("Имя должно быть прописано строкой")
        self.name_of_child = name_of_child

    def child_in_the_group(self) -> bool:
        """
        Функция, которая определяет наличие в группе ребенка с данным именем
        :return: ребенок в группе
        Примеры:
        »> kindergarten = Kindergarten(26, "Kolya")
        »> kindergarten.child_in_the_group()
        """

    def group_is_full(self) -> bool:
        """
        Функция, которая проверяет все  ли пришли сегодня
        :return: Все в сборе
        Примеры:
        »> kindergarten = Kindergarten(26, "Kolya")
        »>kindergarten.group_is_full()
        """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
