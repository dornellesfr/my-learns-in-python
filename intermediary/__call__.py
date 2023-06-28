class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, name):
        print(f'{name} is calling: {self.phone}')


if __name__ == '__main__':
    call_one = CallMe('998453723')
    call_one('Fernando')
