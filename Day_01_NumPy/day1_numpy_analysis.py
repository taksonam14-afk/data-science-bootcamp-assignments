"""
Data Science Bootcamp - NumPy Assignment
Tasks:
1. Marks Matrix using default_rng (10 students x 5 subjects)
2. Total marks and percentage calculation
3. Average marks and standard deviation per subject
4. Subject toppers and indices using np.argmax
5. Pass/Fail identification using Boolean masks
"""

import numpy as np

rng = np.random.default_rng(seed=42)

# Task 1: Create Marks Matrix (10 x 5)
marks = rng.integers(0, 101, size=(10, 5))

# Task 2: Student Performance (Total & Percentage)
total_marks = np.sum(marks, axis=1)
percentage = (total_marks / (5 * 100)) * 100

# Task 3: Subject Performance Analysis
subject_avg = np.mean(marks, axis=0)
subject_std = np.std(marks, axis=0)

# Task 4: Subject Toppers using np.argmax
highest_marks = np.max(marks, axis=0)
topper_indices = np.argmax(marks, axis=0)

# Task 5: Identify Pass and Fail using Boolean Mask
PASS_THRESHOLD = 40
pass_mask = marks >= PASS_THRESHOLD
student_passed = np.all(pass_mask, axis=1)

print("--- Day 1 NumPy Assignment Completed ---")
print("Marks Matrix:\n", marks)
print("Total Marks:", total_marks)
print("Percentages:", np.round(percentage, 2))
print("Subject Averages:", np.round(subject_avg, 2))
print("Subject Toppers (Indices):", topper_indices)
print("Passed Student Indices:", np.where(student_passed)[0].tolist())
