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
        return self.file

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file')
        self._file.close()


instance = MyContextManager('path_file', 'w')
with instance as something:
    ...
