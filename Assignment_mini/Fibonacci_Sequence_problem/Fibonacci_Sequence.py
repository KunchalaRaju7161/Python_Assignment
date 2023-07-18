# Define the decorator function
# generator_func() -It invokes the original generator function passed as an argument
# fib_gen - to create an iterator object
def fibonacci_decorator(generator_func):
    def fibonacci_generator():
        fib_gen = generator_func()
        while True:
            num = next(fib_gen)
            if num % 2 == 0:
                yield num

    return fibonacci_generator


# Apply the decorator to the Fibonacci sequence generator function
@fibonacci_decorator
def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Test the generator by calling it in a loop and printing the generated even Fibonacci numbers.
fib_gen = fibonacci_sequence()

# It sets up a loop that will iterate 10 times.
# The loop variable _ is used when we don't need to use the loop counter value.
for _ in range(10):
    print(next(fib_gen))
