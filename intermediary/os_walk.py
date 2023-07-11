import os
from itertools import count


path = os.path.join('/home', 'fernando', 'Downloads')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(f'{the_counter} Actual folder {root}')

    for dir_ in dirs:
        print(f'    {the_counter} dir: {dir_}')

    for file_ in files:
        print(f'        {the_counter} file: {file_}')
