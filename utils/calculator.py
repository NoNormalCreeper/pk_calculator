import random

def generate_challenge() -> str:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/' and number2 == 0:
        return generate_challenge()
    return f'{number1} {operator} {number2}'
