class MyContextManager:
    def __init__(self, path, mode):
        print('Init')
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        '''Retorno do enter entra pra variável do fim da linha do with'''
        print('Opening file')
        self._file = open(self.path, self.mode, encoding='utf-8')
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file')
        self._file.close()

        print(class_exception)
        print(exception_)
        print(traceback_)

        return True  # The exception was dealed


instance = MyContextManager('path_file.txt', 'w')
with instance as something:
    something.write('Hi\n')
    something.write('Hi2\n')
    something.write('Hi3\n')
