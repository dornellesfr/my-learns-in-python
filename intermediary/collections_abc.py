from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self) -> None:
        self._data = {}
        self._index = 0
        self._next_item = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    @property
    def data(self):
        return self._data

    def __len__(self):
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_item >= self._index:
            raise StopIteration

        value = self._data[self._next_item]
        self._next_item += 1
        return value


if __name__ == '__main__':
    lis = MyList()
    lis.append('Today')
    lis.append('Is')
    lis.append('A')
    lis.append('Good')
    lis.append('Day')
    for item in lis:
        print(item)
