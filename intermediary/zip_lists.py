def zip_lists(l1: list, l2: list):
    interval = min(len(l1), len(l2))
    result = [(l1[i], l2[i]) for i in range(interval)]
    return result


def list_with_all_values(l1: list, l2: list):
    result = [x + y for x, y in zip(l1, l2)]
    return result


if __name__ == "__main__":
    lis1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    lis2 = ['BA', 'SP', 'MG', 'RJ']

    lis3 = [1, 2, 3, 4, 5, 6, 7]
    lis4 = [1, 2, 3, 4]

    a = zip_lists(lis1, lis2)

    print(a)
    print(list(zip(lis1, lis2)))
    b = list_with_all_values(lis3, lis4)
    print(b)
