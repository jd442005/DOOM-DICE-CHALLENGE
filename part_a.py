from collections import defaultdict

def run_part_a():
    total_combinations = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    print(f"Total combinations: {len(total_combinations)}")

    # Distribution
    distribution = defaultdict(int)
    for a in range(1, 7):
        for b in range(1, 7):
            distribution[a + b] += 1

    print("\nSum Distribution:")
    for s in sorted(distribution):
        print(f"Sum = {s}, Count = {distribution[s]}")

    print("\nSum Probabilities:")
    for s in sorted(distribution):
        probability = distribution[s] / 36
        print(f"P(Sum = {s}) = {probability:.4f}")
