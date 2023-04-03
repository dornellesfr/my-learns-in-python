def validate_cpf():
    CPF = '04793962030'
    list_cpf = []

    # Getting first digit
    try:
        list_cpf = [int(number) for number in CPF if number.isdigit()]
    except (ValueError, TypeError):
        print('The value digited is not a number')

    nine_numbers = list_cpf[:9]

    for position, number in enumerate(range(10, 1, -1)):
        nine_numbers[position] *= number

    digit_1 = (sum(nine_numbers) * 10) % 11
    digit_1 = digit_1 if digit_1 <= 9 else 0

    # Getting second digit
    ten_numbers = list_cpf[:9]
    ten_numbers.append(digit_1)

    for position, number in enumerate(range(11, 1, -1)):
        ten_numbers[position] *= number

    digit_2 = (sum(ten_numbers) * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    verified_lasts_digits = digit_1 == list_cpf[9] and digit_2 == list_cpf[10]
    if verified_lasts_digits:
        print('This cpf is valid')
    else:
        print('This  cpf is not valid')


validate_cpf()
