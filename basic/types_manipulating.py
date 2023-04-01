def question1():
    try:
        num = int(input('Type a integer: '))
        isEven = num % 2 == 0
        if isEven:
            print(f'{num} is even')
        else:
            print(f'{num} is odd')
    except ValueError:
        print('Content mus be a valid number')


def question2():
    try:
        hour = int(input('What time is it? '))
        morning = 0 <= hour <= 11
        afternoon = 12 <= hour <= 17
        night = 18 <= hour <= 23
        if morning:
            print('Good morning')
        elif afternoon:
            print('Good afternoon')
        elif night:
            print('Good night')
    except Exception:
        print('Content mus be a valid number')


# question1()
# question2()
