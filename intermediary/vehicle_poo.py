class Engine:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Brand:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Car:
    def __init__(self, name: str, engine: Engine, brand: Brand):
        self._name = name
        self._engine = engine
        self._brand = brand

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def set_engine(self, new_engine):
        self._engine = new_engine

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def set_brand(self, new_brand):
        self._brand = new_brand

    def list_characteristics(self):
        print(self.name)
        print(self.engine.name)
        print(self.brand.name)


if __name__ == "__main__":
    gol = Car('Gol', Engine('AP'), Brand('Volkswagen'))
    gol.list_characteristics()
