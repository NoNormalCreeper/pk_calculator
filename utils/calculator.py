import random

def generate_challenge():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    return f'{number1} {operator} {number2}'
