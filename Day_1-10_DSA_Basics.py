# DSA Practice - Days 1 to 10
# Language: Python

# ==============================
# Day 1: Introduction to DSA
# ==============================

# ==============================
# Day 2: Lists and Indexing
# ==============================

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[-1])

numbers[1] = 25
print(numbers)


# ==============================
# Day 3: Array Traversal
# ==============================

# Program 1: Print all elements
numbers = [5, 10, 15, 20, 25]

for num in numbers:
    print(num)

# Program 2: Find the sum
total = 0

for num in numbers:
    total += num

print("Sum:", total)

# Program 3: Count numbers greater than 10
count = 0

for num in numbers:
    if num > 10:
        count += 1

print("Count:", count)


# ==============================
# Day 4: Largest and Smallest
# ==============================

numbers = [10, 5, 20, 8, 15]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# ==============================
# Day 5: Linear Search
# ==============================

numbers = [10, 20, 30, 40, 50]
target = 30
index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break

print("Index:", index)


# ==============================
# Day 6: Reverse Traversal
# ==============================

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")

print()


# ==============================
# Day 7: List Operations
# ==============================

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)
print(numbers)

numbers.pop(3)
print(numbers)

numbers.remove(30)
print(numbers)


# ==============================
# Day 8: Time Complexity
# ==============================

# O(1): Access by index
numbers = [10, 20, 30, 40, 50]
print(numbers[0])

# O(n): One loop
for num in numbers:
    print(num)

# O(n^2): Nested loops
for i in numbers:
    for j in numbers:
        print(i, j)


# ==============================
# Day 9: Space Complexity
# ==============================

# O(1): Sum using one variable
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(total)

# O(n): Create a copy
copied = []

for num in numbers:
    copied.append(num)

print(copied)


# ==============================
# Day 10: Swapping
# ==============================

# Program 1: Swap variables
a = 5
b = 12

a, b = b, a
print(a, b)

# Program 2: Swap first and last elements
numbers = [5, 10, 15, 20, 25]

numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# Program 3: Swap elements at indexes 1 and 4
numbers = [10, 20, 30, 40, 50, 60]

numbers[1], numbers[4] = numbers[4], numbers[1]
print(numbers)
