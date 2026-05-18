# Creating Tuples
t1 = (10, 20, 30, 40, 50)
t2 = (1, 2, 3, 4, 5)

# Display Tuples
print("Tuple t1 =", t1)
print("Tuple t2 =", t2)
print("\n")

# ---------------- Accessing Elements ----------------
print("----- Accessing Elements -----")
print("First element of t1 =", t1[0])
print("Last element of t1 =", t1[-1])
print("Elements from index 1 to 3 =", t1[1:4])
print("\n")

# ---------------- Tuple Operations ----------------
print("----- Tuple Operations -----")
print("Concatenation =", t1 + t2)
print("Repetition =", t1 * 2)
print("Length of t1 =", len(t1))
print("Maximum value =", max(t1))
print("Minimum value =", min(t1))
print("Sum of elements =", sum(t1))
print("\n")

# ---------------- Membership Test ----------------
print("----- Membership Test -----")
print("Is 20 present in t1?", 20 in t1)
print("Is 100 present in t1?", 100 in t1)
print("\n")

# ---------------- Iterating Through Tuple ----------------
print("----- Iterating Tuple -----")
for i in t1:
    print(i)
print("\n")

# ---------------- Tuple Methods ----------------
t3 = (10, 20, 30, 20, 40, 20)

print("Tuple t3 =", t3)
print("Count of 20 =", t3.count(20))
print("Index of 30 =", t3.index(30))
print("\n")

# ---------------- Nested Tuple ----------------
nested = ((1, 2), (3, 4), (5, 6))

print("----- Nested Tuple -----")
print("Nested Tuple =", nested)
print("First element of first tuple =", nested[0][0])
print("Second element of third tuple =", nested[2][1])
print("\n")

# ---------------- Tuple Packing and Unpacking ----------------
print("----- Packing and Unpacking -----")
person = ("Varshi", 19, "Student")

# Unpacking
name, age, profession = person

print("Name =", name)
print("Age =", age)
print("Profession =", profession)
print("\n")

# ---------------- Converting List to Tuple ----------------
print("----- List to Tuple -----")
my_list = [100, 200, 300]
new_tuple = tuple(my_list)

print("List =", my_list)
print("Converted Tuple =", new_tuple)