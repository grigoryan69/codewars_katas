def basic_op(operator, value1, value2):
    return {
        '+': lambda a, b: value1 + value2,
        '-': lambda a, b: value1 - value2,
        '*': lambda a, b: value1 * value2,
        '/': lambda a, b: value1 / value2
    }[operator](value1, value2)