from collections.abc import Iterable


class MyList:
    def __init__(self) -> None:
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    @property
    def data(self):
        return self._data


if __name__ == '__main__':
    lis = MyList()
    lis.append('Today')
    lis.append('Is')
    lis.append('A')
    lis.append('Good')
    lis.append('Day')
    print(lis.data)
