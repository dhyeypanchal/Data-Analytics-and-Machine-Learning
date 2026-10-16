import numpy as np

# scores = [70, 80, 90]  # Ordinary Python list
# scores_array = np.array(scores)  # Convert to a NumPy array

# print(scores_array)  # [70 80 90]
# print(scores_array.dtype)  # Numeric data type, such as int64


# # A list repeats its contents when multiplied by an integer
# print(scores * 2)  # [70, 80, 90, 70, 80, 90]

# # A NumPy array performs element-wise multiplication
# print(scores_array * 2)  # [140 160 180]


# zeros = np.zeros(3)  # Three zeros
# ones = np.ones(3)  # Three ones
# sequence = np.arange(1, 6)  # Integers from 1 through 5
# steps = np.linspace(0, 1, 5)  # Five evenly spaced values from 0 to 1

# print(sequence)  # [1 2 3 4 5]
# print(steps)  # [0.   0.25 0.5  0.75 1.  ]


# # Two students, each described by three measurements
# data = np.array([
#     [2.0, 7.5, 80],
#     [3.0, 8.0, 90]
# ])

# print(data.shape)  # (2, 3): 2 rows, 3 columns
# print(data.ndim)  # 2: two dimensions
# print(data.size)  # 6: total number of elements


scores = np.array([70, 80, 90, 85, 95])

print(scores[0])  # 70: first element
print(scores[-1])  # 95: last element
print(scores[1:4])  # [80 90 85]: indices 1, 2, and 3


data = np.array([[10, 20, 30], [40, 50, 60]])

print(data[0, 1])  # 20: first row, second column
print(data[:, 0])  # [10 40]: all rows, first column
print(data[1, :])  # [40 50 60]: all columns in second row

# we can also calculate statistics like mean, median, and standard deviation using NumPy functions.
scores = np.array([70, 80, 90, 100])

print(np.mean(scores))  # 85.0: average
print(np.median(scores))  # 85.0: middle value
print(np.std(scores))  # Population standard deviation
print(np.min(scores))  # 70: minimum
print(np.max(scores))  # 100: maximum

# Rows are students; columns are features
data = np.array([
    [2.0, 7.0, 80],
    [4.0, 9.0, 100]
])

print(np.mean(data, axis=0))  # Mean of each column
# [3.0, 8.0, 90.0]

print(np.mean(data, axis=1))  # Mean of each row
# [29.666..., 37.666...]


data = np.array([[1.0, 10.0], [3.0, 20.0], [5.0, 30.0]])

column_means = np.mean(data, axis=0)  # One mean per column
centered = data - column_means  # Broadcast means across rows

print(centered)
# [[-2. -10.]
#  [ 0.   0.]
#  [ 2.  10.]]


# Boolean masking

scores = np.array([55, 72, 88, 91, 63])

mask = scores >= 70  # True for scores of at least 70
passing = scores[mask]  # Select only matching elements

print(mask)  # [False  True  True  True False]
print(passing)  # [72 88 91]

scores = np.array([55, 72, 88, 91, 63])

# Select scores from 70 through 90 inclusive
selected = scores[(scores >= 70) & (scores <= 90)]

print(selected)  # [72 88]