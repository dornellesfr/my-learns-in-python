class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def raise_exception():
    exception_ = MyError('Error Message', 'a', 'b', 'c')
    exception_.add_note('Theres a especific error here')
    raise exception_


try:
    raise_exception()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = AnotherError('Throw again')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('New errors here')
    raise exception_ from error
