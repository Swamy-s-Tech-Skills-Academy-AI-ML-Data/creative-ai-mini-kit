# Generated on: 2025-04-21 12:47:26

Sure! Here's a Python implementation of the Sieve of Eratosthenes algorithm to check if a number is prime:

```python
def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False
    
    for p in range(2, int(n**0.5)+1):
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
    
    return prime

def is_prime(n):
    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Test the is_prime function
number = 17
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
```

This code defines a function `sieve_of_eratosthenes` to generate a list of Boolean values indicating whether each number up to `n` is prime, and another function `is_prime` to check if a given number is prime using the list obtained from `sieve_of_eratosthenes`. The test code at the end of the script checks if the number 17 is prime using the `is_prime` function.