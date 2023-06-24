from log import LogFileMixin


class Eletronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True

    def turn_off(self):
        if self._on:
            self._on = False


class SmartPhone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
        self.log_sucess(f'{self._name} is turned on')

    def turn_off(self):
        super().turn_off()
        self.log_sucess(f'{self._name} is turned off')


if __name__ == "__main__":
    ...
