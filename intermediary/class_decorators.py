class Multiply:
    def __init__(self, multiply):
        self._multiply = multiply
        # self.func = func

    def __call__(self, func):
        def intern(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiply
        return intern


@Multiply(10)
def soma(x, y):
    return x + y


if __name__ == '__main__':
    result = soma(2, 5)
    print(result)
