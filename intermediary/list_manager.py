# adicionar
# listar
# desfazer = ctrl + z
# refazer = ctrl + shift + z
import os


def todo_list():
    tasks = []
    backup = []
    while True:

        print('Commands:')
        print('List, undo, redo, clear, close')
        item = input('Or add new task: ')

        if item == 'close':
            break

        def redo_task():
            if tasks == backup:
                print()
                print('Nothing to redo')
                return
            len_to_redo = len(tasks)
            tasks.append(backup[len_to_redo])

        def undo_task():
            if tasks == []:
                print()
                print('Nothing to undo')
                return
            tasks.pop()

        def add_task(task):
            tasks.append(task)
            backup.append(task)

        def clear():
            os.system('clear')

        def list_tasks():
            print()
            print('TASKS:')
            print(*tasks, sep='\n')
            print()

        commands = {
            "list": list_tasks,
            "undo": undo_task,
            "redo": redo_task,
            "clear": clear,
        }

        if item not in commands:
            add_task(item)
        elif item == 'list':
            pass
        else:
            action = commands.get(item)
            action()

        list_tasks()


if __name__ == "__main__":
    todo = todo_list()
