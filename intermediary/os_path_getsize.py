import math


def format_size(bytes_size: int, base: int = 1024) -> str:
    """ Formata um tamanho de bytes para o tamanho apropriado """
    if bytes_size <= 0:
        return "0B"

    name_sizes = "B", "KB", "MB", "GB", "TB", "PB"
    index_sizes = int(math.log(bytes_size, base))
    potency = base ** index_sizes
    final_size = round(bytes_size / potency, 2)
    name_size = name_sizes[index_sizes]
    return f'{final_size} {name_size}'


print(format_size(1000))
print(format_size(1000000))
print(format_size(1000000000))
