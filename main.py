# Магические методы - dunder методы, методы которые начинаются и заканичваются __
# init по умолчанию не ждет аргументов
# repr - для программистов, возвращает строку по которой видно (и можно воссоздать) состояние объекта repr()
# str - для людей, возвращает строку
# Если не реализован репр и стр, то будет возвращен адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# Если методы сравнения не реализованы то падает ошибка ( не забываем добавлять сравнение, что пришло как в ==)
# contains для реализации проверки in
# самописный объект всегда True, для изменеия поведения нужно написать __bool__
# len вернет ошибку если не переопределить метод len
# что бы объект стал вызываемым (callable) нужно реализовать метод __call__, иначе ошибка
# __iter__ возвращает объект итератор, тот кто реализует итер  = Итаребл
# __next__ должен вернуть следующий объект из контейнера, кто его реализует = Итератор
# __getitem__ нужен для функционала [] аналог списка или словаря, __setitem__ для присвоения. Если не реализовать то будет ошибка.

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

    def __lt__(self, other):
        # Меньше чем
        return self.value < other.value

    def __gt__(self, other):
        # Больше чем
        return self.value > other.value

    def __le__(self, other):
        # Меньше или равно
        return self.value <= other.value

    def __ge__(self, other):
        # Больше или равно
        return self.value >= other.value


class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        while 0 <= self.index < len(self.container): # Можно поменять на if
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration

class Wallet:
    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)  # используется для добавления банкнот в контейнер кошелька. Метод extend
        # расширяет список, добавляя элементы из переданного итерируемого объекта (banknotes) в конец списка. В
        # данном случае, все переданные объекты Banknote добавляются в self.container.
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        #  Реализует проверку in можно не проверять тип item
        return item in self.container

    def __bool__(self):
        # Переопределяем bool, по умолчанию самописный объект True
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        # Позволяет вызывать объекты класса как функцию
        return f'{sum(e.value for e in self.container)} рублей'

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item): # item либо индекс ибо слово из словаря
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == "__main__":
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred)
    wallet[0] = Banknote(500)
    print(wallet)


