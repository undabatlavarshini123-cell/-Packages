import numpy as np

# Create Arrays
a = np.array([10, 30, 20, 40])
b = np.array([1, 3, 2, 4])

# Display Arrays
print("Array a =", a)
print("Array b =", b)
print("\n")

# ---------------- Arithmetic Operations ----------------
print("----- Arithmetic Operations -----")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power (a^2) =", np.power(a, 2))
print("Square Root of a =", np.sqrt(a))
print("\n")

# ---------------- Maximum and Minimum ----------------
print("----- Maximum and Minimum -----")
print("Maximum value of a =", np.max(a))
print("Minimum value of a =", np.min(a))
print("Index of Maximum value =", np.argmax(a))
print("Index of Minimum value =", np.argmin(a))
print("\n")

# ---------------- Sum and Product ----------------
print("----- Sum and Product -----")
print("Sum of elements in a =", np.sum(a))
print("Product of elements in a =", np.prod(a))
print("\n")

# ---------------- Statistical Operations ----------------
print("----- Statistical Operators -----")
print("Mean of a =", np.mean(a))
print("Median of a =", np.median(a))
print("Standard Deviation of a =", np.std(a))
print("Variance of a =", np.var(a))
print("\n")

# ---------------- Sorting ----------------
print("----- Sorting -----")
print("Sorted array a =", np.sort(a))
print("\n")

# ---------------- Array Shape and Size ----------------
print("----- Array Properties -----")
print("Shape of a =", a.shape)
print("Size of a =", a.size)
print("Data type of a =", a.dtype)
print("Dimension of a =", a.ndim)
print("\n")

# ---------------- Reshaping ----------------
print("----- Reshaping Array -----")
c = np.array([1, 2, 3, 4, 5, 6])
print("Original array c =", c)
print("Reshaped into 2x3 matrix:")
print(c.reshape(2, 3))
print("\n")

# ---------------- Special Arrays ----------------
print("----- Special Arrays -----")
print("Array of Zeros:")
print(np.zeros((2, 3)))

print("Array of Ones:")
print(np.ones((2, 3)))

print("Identity Matrix:")
print(np.eye(3))
print("\n")

# ---------------- Random Numbers ----------------
print("----- Random Numbers -----")
print("Random integers:")
print(np.random.randint(1, 10, size=(2, 3)))

print("Random decimal numbers:")
print(np.random.rand(2, 3))