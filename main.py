# Магические методы - dunder методы, методы которые начинаются и заканичваюся __
# init по умолчанию не ждет аргументов


class Banknote:
    def __init__(self, value: int):
        # Для программистов
        self.value = value


    def __repr__(self):
        # Для людей
        return f'Banknote({self.value})'


    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'


if __name__ == "__main__":
    banknote = Banknote(50)
    print(banknote)  # Возвращает str
    print(f'{banknote!r}')  # Возвращает repr

    other = eval(repr(banknote))  # Воссоздание объекта
    print(other)

