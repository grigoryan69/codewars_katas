def factorial(n):
    if n > -1 and n < 13:
        return 1 if n == 1 or n == 0 else factorial(n - 1) * n
    raise ValueError('should be less then 13 and more then 0')
