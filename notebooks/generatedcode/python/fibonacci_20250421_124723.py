# Generated on: 2025-04-21 12:47:23

Sure! Here's an example of a Python function that uses recursion to calculate the Fibonacci sequence:

```python
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n = 10
print(fibonacci(n))
```

In this code, the `fibonacci` function takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence. It uses recursion to calculate the value based on the previous two numbers in the sequence.