import accounts
from person import Person


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age


if __name__ == '__main__':
    c1 = Client('Fernando', 20)
    print(c1)
    c1.account = accounts.CheckingAccount(1220, 20000, limit=400)
    print(c1.account)
