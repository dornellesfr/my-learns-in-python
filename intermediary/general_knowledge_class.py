from abc import ABC, abstractclassmethod


class Account(ABC):
    def __init__(self, number) -> None:
        self._number = number
        self._money = 0

    @abstractclassmethod
    def draw(self): ...

    def deposit(self, value) -> None:
        self._money += value

    @property
    def number(self):
        return self._number


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Bank:
    ...


class Client(Person):
    def __init__(self, name: str, age: int, account: Account) -> None:
        super().__init__(name, age)
        self._account = account

    @property
    def account(self):
        return self._account


class CheckingAccount(Account):
    def __init__(self, number) -> None:
        super().__init__(number)

    def draw(self, take):
        if take - self._money > -100:
            self._money -= take
            return None
        raise ValueError('You cannot use')

class SavingAccount(Account):
    ...
