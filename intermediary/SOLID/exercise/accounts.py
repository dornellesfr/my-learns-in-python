from abc import ABC, abstractclassmethod

class Account(ABC):
    def __init__(self, agency: int, acc_number: int, money=0) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._money = money

    @abstractclassmethod
    def draw(self): ...

    def deposit(self, value) -> None:
        if value < 1:
            raise ValueError('Just values more than 0 are allowed')
        self._money += value
        self.details()
        
    def details(self):
        print(f'Agency: {self.agency}')
        print(f'Acc: {self.acc_number}')
        print(f'Cash: R${self.money:.2f}')
        print()

    @property
    def agency(self):
        return self._agency    

    @property
    def acc_number(self):
        return self._acc_number    

    @property
    def money(self):
        return self._money


class CheckingAccount(Account):
    def __init__(self, agency: int, acc_number: int, money=0, limit=0) -> None:
        super().__init__(agency, acc_number, money)
        self.limit = limit

    def draw(self, take):
        value_pos_draw = self._money - take
        if value_pos_draw >= (self.limit * -1):
            self._money -= take
            self.details()
            return None
        raise ValueError('You cannot use draw this money')


class SavingAccount(Account):
    def draw(self, take: int):
        value_pos_draw = self._money - take
        if value_pos_draw >= 0:
            self._money -= take
            self.details()
            return None
        raise ValueError('You have not cash enough')
    

if __name__ == '__main__':
    cp1 = SavingAccount(1589, 5000)
    # cp1.deposit(500)
    # cp1.draw(500)
    # cp1.details()
    cc1 = CheckingAccount(1589, 4000, limit=400)
    # cc1.draw(401)
    
