import numpy as np

# Creating arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Display arrays
print("Array a =", a)
print("Array b =", b)
print("\n")

# ---------------- Arithmetic Operations ----------------
print("------ Arithmetic Operations ------")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power (a^2) =", np.power(a, 2))
print("Square Root of a =", np.sqrt(a))
print("Absolute Values =", np.abs(a))
print("\n")

# ---------------- Statistical Operations ----------------
print("------ Statistical Operations ------")
print("Maximum value =", np.max(a))
print("Minimum value =", np.min(a))
print("Sum of elements =", np.sum(a))
print("Product of elements =", np.prod(a))
print("Mean =", np.mean(a))
print("Median =", np.median(a))
print("Standard Deviation =", np.std(a))
print("Variance =", np.var(a))
print("\n")

# ---------------- Trigonometric Operations ----------------
print("------ Trigonometric Operations ------")
angles = np.array([0, 30, 45, 60, 90])

# Convert degrees to radians
radians = np.radians(angles)

print("Angles =", angles)
print("Sine values =", np.sin(radians))
print("Cosine values =", np.cos(radians))
print("Tangent values =", np.tan(radians))
print("\n")

# ---------------- Logarithmic and Exponential ----------------
print("------ Logarithmic and Exponential ------")
print("Exponential (e^a) =", np.exp(a))
print("Natural Log (ln a) =", np.log(a))
print("Log base 10 =", np.log10(a))
print("\n")

# ---------------- Rounding Functions ----------------
decimal_array = np.array([1.2, 2.5, 3.7, 4.9])

print("------ Rounding Functions ------")
print("Original Array =", decimal_array)
print("Rounded =", np.round(decimal_array))
print("Floor =", np.floor(decimal_array))
print("Ceiling =", np.ceil(decimal_array))
print("\n")

# ---------------- Matrix Operations ----------------
print("------ Matrix Operations ------")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)
print("Matrix Addition:\n", m1 + m2)
print("Matrix Subtraction:\n", m1 - m2)
print("Matrix Multiplication:\n", np.dot(m1, m2))
print("Transpose of Matrix 1:\n", m1.T)
print("\n")

# ---------------- Random Numbers ----------------
print("------ Random Numbers ------")
print("Random Integers:\n", np.random.randint(1, 10, (2, 3)))
print("Random Decimal Numbers:\n", np.random.rand(2, 3))