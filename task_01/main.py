def caching_fibonacci():
    '''This function calculates a mwmber of the Fibonacci series with the number "n". Uses caching in the "cache" dictionary'''
    cache = {}
    def fibonacci(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

### Uncomment lines below to check the function
# fib = caching_fibonacci()
# print(fib(10))  # Виведе 55
# print(fib(15))  # Виведе 610
