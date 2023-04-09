def find_first_duplicated(arr: list):
    finded_numbers = set()
    first_number_duplicated = -1
    for number in arr:
        if number in finded_numbers:
            return number

        finded_numbers.add(number)

    return first_number_duplicated

print(find_first_duplicated([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_first_duplicated([9, 1, 8, 9, 9, 7, 2, 1, 6, 8]))
print(find_first_duplicated([1, 3, 2, 2, 8, 6, 5, 9, 6, 7]))