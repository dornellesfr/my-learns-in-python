while True:
    left = input('Do you wanna exit? [Y]es: ')
    if left in 'Yy':
        break

    try:
        num1 = int(input('Type number one to calculate: '))
        num2 = int(input('Type number two to calculate: '))
        operator = input('Type a operator to calculate: ')

        if operator not in '+-/*':
            raise ValueError()

    except ValueError:
        print('Fields must be a valid content')
        continue

    sum_operator = operator == '+'
    decrease = operator == '-'
    divide = operator == '/'
    multiply = operator == '*'

    if sum_operator:
        print(num1 + num2)
    if decrease:
        print(num1 - num2)
    if divide:
        print(num1 / num2)
    if multiply:
        print(num1 * num2)
