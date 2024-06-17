# Function to generate Fibonacci sequence
def fibonacci(n):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # If n is less than or equal to 0, return an empty list as no terms to generate
    if n <= 0:
        return []
    # If n is 1, return the list with the first Fibonacci number which is 0
    elif n == 1:
        return [0]

    # Loop to generate the next Fibonacci numbers until we have n numbers
    while len(fib_sequence) < n:
        # Calculate the next Fibonacci number
        # fib_sequence[-1] is last element of list
        # fib_sequence[-2] is second last element of list
        next_number = fib_sequence[-1] + fib_sequence[-2]
        # Add the next number to the sequence
        fib_sequence.append(next_number)

    # Return the Fibonacci sequence
    return fib_sequence

n = 13
fib_sequence = fibonacci(n)
print(f"First {n} terms of the Fibonacci sequence: {fib_sequence}")
