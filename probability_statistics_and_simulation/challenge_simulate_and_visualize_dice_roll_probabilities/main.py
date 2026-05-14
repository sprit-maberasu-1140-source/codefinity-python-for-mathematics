import random
import matplotlib.pyplot as plt
from collections import Counter

def simulate_dice_rolls(num_rolls):
    sums = []
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)
    return sums

def analyze_sums(sums):
    count = Counter(sums)
    most_common = count.most_common(1)[0][0]
    least_common = min(count, key=lambda x: count[x])
    return most_common, least_common, count

def plot_histogram(sums):
    plt.hist(sums, bins=range(2, 14), edgecolor='black', align='left')
    plt.title("Histogram of Sums from Rolling Two Dice 1,000 Times")
    plt.xlabel("Sum")
    plt.ylabel("Frequency")
    plt.xticks(range(2, 13))
    plt.show()

findings = None  # Store findings at module level

def main():
    global findings
    num_rolls = 1000
    sums = simulate_dice_rolls(num_rolls)
    most_common, least_common, count = analyze_sums(sums)
    plot_histogram(sums)
    findings = (
        f"Most common sum: {most_common} (occurred {count[most_common]} times)\n"
        f"Least common sum: {least_common} (occurred {count[least_common]} times)"
    )
    print(findings)

if __name__ == "__main__":
    main()