
# ============================================
# DSA PRACTICE WITH PYTHON
# DAYS 11-20
# ============================================


# ============================================
# DAY 11: STRING TRAVERSAL AND CHARACTER COUNTING
# ============================================

# Program 1: Access characters using indexing
word = "DSA"

print("Day 11 - Program 1")
print(word[1])
print(word[-1])


# Program 2: Traverse a string
word = "HELLO"

print("\nDay 11 - Program 2")
for ch in word:
    print(ch)


# Program 3: Count a specific character
word = "banana"
count = 0

for ch in word:
    if ch in "a":
        count += 1

print("\nDay 11 - Program 3")
print("Count of a:", count)


# ============================================
# DAY 12: STRING REVERSAL AND PALINDROME
# ============================================

# Program 1: Reverse a string using a loop
word = "python"
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("\nDay 12 - Program 1")
print(reversed_word)


# Program 2: Check whether a word is a palindrome
word = "level"
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("\nDay 12 - Program 2")
if word == reversed_word:
    print("Palindrome")
else:
    print("Not a palindrome")


# ============================================
# DAY 13: CHARACTER FREQUENCY
# ============================================

# Program 1: Count a specific character
word = "mississippi"
count = 0

for ch in word:
    if ch == "s":
        count += 1

print("\nDay 13 - Program 1")
print("Count of s:", count)


# Program 2: Count the frequency of each character
word = "aabbc"
frequency = {}

for ch in word:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("\nDay 13 - Program 2")
print(frequency)


# Program 3: Find the first repeated character
word = "abca"
seen = set()

print("\nDay 13 - Program 3")

for ch in word:
    if ch in seen:
        print("First repeated character:", ch)
        break
    seen.add(ch)


# ============================================
# DAY 14: TWO-POINTER TECHNIQUE
# ============================================

# Reverse a list by swapping elements
numbers = [1, 2, 3, 4]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print("\nDay 14 - Reverse List")
print(numbers)


# ============================================
# DAY 15: BUBBLE SORT
# ============================================

# Compare adjacent elements and swap when needed
numbers = [7, 3, 5, 2]
n = len(numbers)

for i in range(n):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("\nDay 15 - Bubble Sort")
print(numbers)


# ============================================
# DAY 16: SELECTION SORT
# ============================================

# Find the minimum element and place it correctly
numbers = [8, 3, 6, 2, 5]

for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("\nDay 16 - Selection Sort")
print(numbers)


# ============================================
# DAY 17: INSERTION SORT
# ============================================

# Insert each element into its correct position
numbers = [6, 3, 8, 5]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print("\nDay 17 - Insertion Sort")
print(numbers)


# ============================================
# DAY 18: SORTING REVISION
# ============================================

# Bubble Sort:
# Compares adjacent elements and swaps them if needed.
# Best case: O(n) with an optimization flag.
# Average and worst cases: O(n^2).

# Selection Sort:
# Finds the minimum element in the unsorted portion.
# Best, average and worst cases: O(n^2).

# Insertion Sort:
# Inserts each element into the correct position
# in the sorted portion.
# Best case: O(n).
# Average and worst cases: O(n^2).


# ============================================
# DAY 19: BINARY SEARCH
# ============================================

# Binary Search works on a sorted list.
numbers = [2, 4, 6]
target = 4

left = 0
right = len(numbers) - 1

print("\nDay 19 - Binary Search")

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Target not found")


# ============================================
# DAY 20: BINARY SEARCH CHALLENGE
# ============================================

numbers = [3, 6, 9, 12, 15, 18, 21]
target = 12

left = 0
right = len(numbers) - 1

print("\nDay 20 - Binary Search Challenge")

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Target not found")
