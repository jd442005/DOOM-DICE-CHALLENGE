from itertools import product
from collections import Counter

def calculate_distribution(die_a, die_b):
    return Counter([a + b for a, b in product(die_a, die_b)])
