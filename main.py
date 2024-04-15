def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Prompt the user to enter the maximum number of Fibonacci numbers they want to generate
input_str = input("Enter the maximum number of Fibonacci numbers you want to generate: ")

# Split the input string by comma and convert each part to an integer
numbers = [int(num) for num in input_str.split(',')]

# Generate Fibonacci sequence for each input number
for n in numbers:
    fib_numbers = fibonacci(n)
    print(f"Fibonacci sequence for n={n}: {fib_numbers}")
