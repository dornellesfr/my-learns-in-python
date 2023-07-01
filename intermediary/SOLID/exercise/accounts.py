from abc import ABC, abstractclassmethod


class Account(ABC):
    def __init__(self, agency: int, acc_number: int, money: float = 0) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._money = money

    @abstractclassmethod
    def draw(self, value: float) -> float: ...

    @property
    def agency(self) -> int:
        return self._agency

    @property
    def acc_number(self) -> int:
        return self._acc_number

    @property
    def money(self) -> float:
        return self._money

    def deposit(self, value: float) -> None:
        if value < 1:
            raise ValueError('Just values more than 0 are allowed')
        self._money += value
        self.details()

    def details(self) -> None:
        print(f'Agency: {self.agency}')
        print(f'Acc: {self.acc_number}')
        print(f'Cash: R${self.money:.2f}')
        print()

    def __repr__(self) -> str:
        attr1 = f'Agency: {self.agency}\n'
        attr2 = attr1 + f'Acc: {self.acc_number}\n'
        attr3 = attr2 + f'Cash: R${self.money:.2f}'
        return attr3


class CheckingAccount(Account):
    def __init__(
        self,
        agency: int,
        acc_number: int,
        money: float = 0,
        limit: float = 0
    ) -> None:
        super().__init__(agency, acc_number, money)
        self.limit = limit

    def draw(self, value: float) -> float:
        value_pos_draw = self._money - value
        if value_pos_draw >= (self.limit * -1):
            self._money -= value
            self.details()
            return self.money
        raise ValueError('You cannot use draw this money')

    def __repr__(self) -> str:
        attr1 = f'Agency: {self.agency}\n'\
            f'Acc: {self.acc_number}\n'\
            f'Cash: R${self.money:.2f}\n'\
            f'Credit: R${self.limit:.2f}'
        return attr1


class SavingAccount(Account):
    def draw(self, value: float) -> float:
        value_pos_draw = self._money - value
        if value_pos_draw >= 0:
            self._money -= value
            self.details()
            return self.money
        raise ValueError('You have not cash enough')


if __name__ == '__main__':
    cp1 = SavingAccount(1589, 5000)
    # cp1.deposit(500)
    # cp1.draw(500)
    # cp1.details()
    cc1 = CheckingAccount(1589, 4000, limit=400)
