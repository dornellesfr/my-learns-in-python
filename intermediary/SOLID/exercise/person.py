from abc import ABC, abstractclassmethod

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


class Client(Person):
    def __init__(self, name: str, age: int, account: Account) -> None:
        super().__init__(name, age)
        self._account = account

    @property
    def account(self):
        return self._account