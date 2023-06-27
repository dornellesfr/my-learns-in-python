class Dot:
    def __init__(self, x, y, z='string'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        '''
        O método __add__ é usado para quando você põe + entre os dois itens
        ele pode retornar qualquer coisa.
        ex: return 'Xablau'
        Toda vez que tu somar algo com a classe citada o retorno será
        uma string 'Xablau'
        '''
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Dot(new_x, new_y)

    def __gt__(self, other) -> bool:
        self_result = self.x + self.y
        other_result = other.x + other.y
        return self_result > other_result


p1 = Dot(1, 2)
p2 = Dot(3, 4)
p3 = p1 + p2

p1_gt_p2 = p1 > p2
p2_gt_p1 = p2 > p1

# print(p1)
# print(repr(p2))
# print(p3)
# print(p1_gt_p2)
# print(p2_gt_p1)
