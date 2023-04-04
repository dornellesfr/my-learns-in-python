def multiply_for(multiply: int):
    def number_to_multiply(number: int):
        return number * multiply
    return number_to_multiply


double = multiply_for(2)
triple = multiply_for(3)
quadruple = multiply_for(4)
