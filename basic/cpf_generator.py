from random import randint


def cpf_generator():
    cpf = []
    for number in range(9):
        cpf.append(randint(0, 9))

    nine_numbers = cpf.copy()

    for position, number in enumerate(range(10, 1, -1)):
        nine_numbers[position] *= number

    digit_1 = (sum(nine_numbers) * 10) % 11
    digit_1 = digit_1 if digit_1 <= 9 else 0

    # Getting second digit
    ten_numbers = cpf[:9]
    ten_numbers.append(digit_1)

    for position, number in enumerate(range(11, 1, -1)):
        ten_numbers[position] *= number

    digit_2 = (sum(ten_numbers) * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    cpf = ''.join([str(numb) for numb in cpf])

    cpf_generated = f'{cpf}{digit_1}{digit_2}'
    print(cpf_generated)


if __name__ == '__main__':
    cpf_generator()
