class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Бумажная книга (дочерний класс) """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            print("Количество страниц должно быть целым числом")
        if new_pages <= 0:
            print("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self.pages!r})"



class AudioBook(Book):
    """ Аудио книга (дочерний класс) """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            print("Продолжительность должна быть числом с плавающей точкой")
        if new_duration <= 0:
            print("Продолжительность аудио-книги должна быть больше 0")
        self._duration = new_duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, duration = {self.duration!r})"

