from pathlib import Path

PATH_DATA = Path(__file__).parent / 'logs.txt'


class Log:
    def _log(self, message):
        raise NotImplementedError("Log not implemented")

    def log_error(self, message):
        return self._log(f"Error: {message}")

    def log_sucess(self, message):
        return self._log(f"Success: {message}")


class LogFileMixin(Log):
    def _log(self, message):
        formated_msg = f'{message} ({self.__class__.__name__})\n'
        with open(PATH_DATA, 'a') as file:
            file.write(formated_msg)


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')


if __name__ == "__main__":
    log_print = LogPrintMixin()
    log_print.log_error("Aconteceu algo inesperado")
    log_print.log_sucess("Funfou")

    log_file = LogFileMixin()
    log_file.log_error('Qualquer coisa')
    log_file.log_sucess('Que legal')
