import json
from intermediary.save_class.creation_instances_and_save \
    import PATH_FILE, Person

with open(PATH_FILE, 'r') as file:
    instances = json.load(file)

    p1 = Person(**instances[0])
    p2 = Person(**instances[1])
    p3 = Person(**instances[2])

    print(p1.name)
    print(p2.name)
    print(p3.name)
