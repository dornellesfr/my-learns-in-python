class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'
