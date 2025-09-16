from math import sqrt


# Example function to be tested
def fibonacci(n):
    phi = (1 + sqrt(5)) / 2
    return int((phi**n - (-phi) ** -n) / sqrt(5))
