def add(a, b):
    return a - b  # intentional bug

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return None
    return a / b