import json

PATH_FILE = './intermediary/save_class/instances.json'


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


p1 = Person('Diego', 12)
p2 = Person('Alexander', 20)
p3 = Person('Ethan', 32)
instances = [vars(p1), vars(p2), vars(p3)]


def save_instances(arr: list):
    with open(PATH_FILE, 'w') as file:
        json.dump(arr, file, ensure_ascii=False, indent=2)


save_instances(instances)
