import os
from itertools import count
from os_path_getsize import format_size


path = os.path.join('/home', 'fernando', 'Downloads')
counter = count()

for root, dirs, files in os.walk(path):
    the_counter = next(counter)
    print(f'{the_counter} Actual folder {root}')

    for dir_ in dirs:
        print(f'    {the_counter} dir: {dir_}')

    for file_ in files:
        complete_path = os.path.join(root, file_)
        size = os.path.getsize(complete_path)
        print(f'  {the_counter} file: {file_}, {format_size(size)}')
