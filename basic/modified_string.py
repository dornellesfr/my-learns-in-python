def question():
    name = 'Fernando'
    counter = 0
    str_name = ''

    while counter < len(name):
        str_name = str_name + '*' + name[counter]
        counter += 1

    print(str_name)


# question()
