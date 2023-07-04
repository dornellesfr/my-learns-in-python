from dataclasses import dataclass, asdict, field


@dataclass
class Person:
    name: str = 'None'
    last_name: str = 'None'
    age: int = 0
    address: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.completed_name = f'{self.name} {self.last_name}'

    # @property
    # def completed_name(self):
    #     return f'{self.name} {self.last_name}'

    # @completed_name.setter
    # def completed_name(self, value):
    #     name, *last = value.split()
    #     self.name = name
    #     self.last_name = ' '.join(last)


if __name__ == '__main__':
    p1 = Person('Fernando', 'Rocha')
    print(p1.completed_name)
    print(asdict(p1))
