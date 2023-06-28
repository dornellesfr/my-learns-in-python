def add_repr(cls: object) -> object:
    def my_repr(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls
# Caso de uso foi fazer um decorator para ser usado na classe
# para registrar o __repr__


def home_speak(method_):
    def intern(self, *args, **kwargs):
        result = method_(self, *args, **kwargs)

        if 'Earth' in result:
            return 'You are in home'
        # Manipulação do resultado, se não ele retorna o mesmo
        # Feito na linha 15, que seria o padrão.

        return result
    return intern


# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr
# É possível usar por herança o REPR.


@add_repr
class Team:
    def __init__(self, name):
        self.name = name

    # def __repr__(self) -> str:
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr


@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

    @home_speak
    def my_name(self):
        return f'This planet is {self.name}'

    # def __repr__(self) -> str:
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name}({class_dict})'
    #     return class_repr


if __name__ == '__main__':
    inter = Team('Internacional')
    march = Planet('March')
    earth = Planet('Earth')

    print(inter)
    print(march)
    print(earth)
    print(march.my_name())
    print(earth.my_name())
