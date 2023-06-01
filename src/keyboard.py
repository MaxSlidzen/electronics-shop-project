from src.item import Item


class MixinLanguage:
    """
    Класс Mixin со значением языка клавиатуры по умолчанию
    """
    def __init__(self) -> None:
        self._language = "EN"


    @property
    def language(self):
        """
        Возвращает текущий язык клавиатуры.
        """
        return self._language


    def change_lang(self) -> 'MixinLanguage':
        """
        Метод смены языка клавиатуры
        """
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
        return self


class KeyBoard(Item, MixinLanguage):
    """
    Класс для представления клавиатуры в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализация экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
