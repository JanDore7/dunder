# Магические методы - dunder методы, методы которые начинаются и заканичваются __
# init по умолчанию не ждет аргументов
# repr - для программистов, возвращает строку по которой видно (и можно воссоздать) состояние объекта repr()
# str - для людей, возвращает строку
# Если не реализован репр и стр, то будет возвращен адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип



class Banknote:
    def __init__(self, value: int):
        # Для программистов repr()
        self.value = value

    def __repr__(self):
        # Для людей str()
        return f'Banknote({self.value})'

    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other):
        # Проверяет на равенство
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value


if __name__ == "__main__":
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    print(fifty == hundred)
    print(fifty == banknote)  # Если не определить eq сравниваться будут ячейки памяти соответственно будет false


