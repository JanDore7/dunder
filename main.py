# Магические методы - dunder методы, методы которые начинаются и заканичваются __
# init по умолчанию не ждет аргументов
# repr - для программистов, возвращает строку по которой видно (и можно воссоздать) состояние объекта repr()
# str - для людей, возвращает строку
# Если не реализован репр и стр, то будет возвращен адрес в памяти

class Banknote:
    def __init__(self, value: int):
        # Для программистов repr()
        self.value = value


    def __repr__(self):
        # Для людей str()
        return f'Banknote({self.value})'


    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'


if __name__ == "__main__":
    banknote = Banknote(50)
    print(banknote)  # Возвращает str



