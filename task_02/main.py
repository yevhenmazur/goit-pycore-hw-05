'''
Import module for operations with regular expressions.
Generator class required for correct type annotation acording to PEP 484
'''
import re
from typing import Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    '''This function extract numbers from a string'''
    pattern = r'\d+[.,]\d+'
    for amount_of_money in re.finditer(pattern, text):
        yield amount_of_money.group()

def sum_profit(text: str, func: callable):
    '''This function accept a callable function and return the sum of the elements'''
    return sum(float(num.replace(',', '.')) for num in func(text))
    

### Uncomment section below to check the function
'''
text = "Загальний дохід працівника складається з декількох частин: \
    1000.01 як основний дохід, доповнений додатковими надходженнями \
    27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
'''