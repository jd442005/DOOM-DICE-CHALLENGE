from itertools import product
from utils.dice_utils import calculate_distribution

def run_part_b():
    orig_die = [1, 2, 3, 4, 5, 6]
    original_dist = calculate_distribution(orig_die, orig_die)

    possible_die_a = [
        [1, 1, 2, 2, 3, 4],
        [1, 2, 2, 3, 3, 4],
        [1, 1, 1, 2, 3, 4]
    ]

    possible_die_b_values = list(range(1, 21))

    print("Searching for valid undoomed dice...")

    for die_a in possible_die_a:
        for die_b in product(possible_die_b_values, repeat=6):
            if calculate_distribution(die_a, die_b) == original_dist:
                print("✅ Solution found!")
                print("New Die A (≤4 spots):", die_a)
                print("New Die B:", list(die_b))
                return
    print("❌ No valid configuration found.")
