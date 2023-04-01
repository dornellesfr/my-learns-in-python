name = input('Type your name: ')
age = input('Type your age: ')

if name and age:
    age = int(age)
    print(f'Your name is {name}')
    print(f'Your name reversed is {name[::-1]}')
    if ' ' in name:
        print('Your name contain spaces')
    else:
        print('Your name not contain spaces')
    name_chars = len(name.replace(' ', ''))
    print(f'Your name have {name_chars} letters')
    print(f'First letter of your name is {name[0]}')
    print(f'The last letter in your name is {name[-1]}')
else:
    print('Sorry, your left fields not full filled')
