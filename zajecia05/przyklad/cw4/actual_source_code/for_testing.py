def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b