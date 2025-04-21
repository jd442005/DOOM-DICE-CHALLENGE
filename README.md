# 🎲 The Doomed Dice Challenge

Welcome to **The Doomed Dice Challenge** – a fun and brain-twisting problem involving dice, probability, and a mischievous Norse god named Loki!

This project is implemented in Python and solves the full problem step-by-step, including both **basic probability calculations** and **reconstructing valid dice under constraints** using logic and code.

---

## 🧩 Problem Statement

### Part A (15–20 Minutes):

You are given two 6-sided dice (Die A and Die B), each with faces `[1, 2, 3, 4, 5, 6]`.

You can only roll **both dice together**, and your **turn is guided by the sum** of both dice.

#### Tasks:
1. **How many total combinations are possible?**  
   ➤ Show the math and code.

2. **Display distribution of all combinations** obtained by rolling both dice.  
   ➤ Output a 6x6 matrix or value-frequency mapping.

3. **Calculate the probability of all possible sums**.  
   ➤ For example, P(Sum = 2) = 1/36 because there's only one combination: (1, 1).

---

### Part B (25–30 Minutes):

⚠️ Loki, the Norse God, curses your dice by **removing all the spots**.

To play your game again, you must reattach the spots — **but** under the following **conditions**:

#### Loki’s Curse:
- Die A:
  - Cannot have more than **4 spots** on any face.
  - May have **repeated values** on faces.
- Die B:
  - Can have **as many spots as needed** (even > 6).
- The **probabilities of each sum must remain exactly the same** as in Part A.

#### Input:
```python
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]
```

#Output:
A function undoom_dice(Die_A, Die_B) must return:

python
Copy
Edit
New_Die_A = [?, ?, ?, ?, ?, ?]  # All ≤ 4
New_Die_B = [?, ?, ?, ?, ?, ?]  # Any values
Such that the distribution of sums is preserved.

✅ Solution Features
Calculates total combinations and probabilities of dice rolls.

Generates valid dice that match original probabilities, even with Loki's constraints.

Uses combinatorics and brute-force logic with optimizations.

📁 Project Structure
```
doomed_dice_challenge/
├── main.py               # Runs the full solution
├── part_a.py             # Solves Part A
├── part_b.py             # Solves Part B
├── utils/
│   └── dice_utils.py     # Shared logic for sum distribution
├── data/
│   └── outputs.txt       # Optional logs
├── requirements.txt
└── README.md             # This file
```
▶️ How to Run
Clone the repo:
```
git clone https://github.com/your-username/doomed-dice-challenge.git
cd doomed-dice-challenge
```
(Optional) Set up a virtual environment:
```
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
```
Run the main script:
```
python main.py
```
📜 License
This project is open-source and free to use under the MIT License.
give this github code format
