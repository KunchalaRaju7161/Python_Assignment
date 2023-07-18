def fibonacci_decorator(generator_func):
    def fibonacci_generator():
        fib_gen = generator_func()
        while True:
            num = next(fib_gen)
            if num % 2 == 0:
                yield num

    return fibonacci_generator


@fibonacci_decorator
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_sequence()
for _ in range(10):
    print(next(fib_gen))
