# Por conta do Liskov Subistitution Principle
# você deve usar sempre a SUPERCLASSE como tipagem,
# pois podes usar diferentes subclasses dela (filhos) numa mesma aplicação
# sem quebrar.

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print(f'Sended e-mail: {self.msg}')
        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print(f'Sended SMS: {self.msg}')
        return True


def notify(note: Notification):
    sended_notification = note.send()

    if sended_notification:
        print('Notification sended')
    else:
        print('Notification NOT sended')


if __name__ == '__main__':
    notify(EmailNotification('Oi, tudo?'))
