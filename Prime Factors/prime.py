"""
prime.py -- Write the application code here
"""
from math import sqrt


def generate_prime_factors(num):
    """
    Funtion to generate prime factors of 'num'
    """
    generate_prime_factors_list = []
    try:
        num = int(num)
    except ValueError:
        return ValueError
    while num % 2 == 0:
        generate_prime_factors_list.append(2)
        num /= 2
    for i in range(3, int(sqrt(num))+1, 2):
        if num % i == 0:
            generate_prime_factors_list.append(i)
            num /= i
    if num > 2:
        generate_prime_factors_list.append(int(num))

    return generate_prime_factors_list
