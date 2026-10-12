
# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = {}
    most_common = numbers[0]

    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > counts[most_common]:
            most_common = num

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A dictionary counts how often each number appears.
- Could it be optimized? This is already efficient because it goes through the list once.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n) average-case for set operations
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set tracks numbers already seen while the result keeps the original order.
- Could it be optimized? This is already efficient for removing duplicates while keeping order.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n^2) in the theoretical worst case for hash operations
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? A set finds matching numbers without using two loops.
- Could it be optimized? This is already efficient for finding all pairs.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    if n < 0:
        raise ValueError("n cannot be negative")

    capacity = 2
    items = [None] * capacity
    size = 0

    for value in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            new_items = [None] * new_capacity

            for i in range(size):
                new_items[i] = items[i]

            items = new_items
            capacity = new_capacity
            print("Resized list to capacity:", capacity)

        items[size] = value
        size += 1

    return items[:size]

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list reaches its current capacity.
- What is the worst-case for a single append? O(n) when values must be copied.
- What is the amortized time per append overall? O(1).
- Space complexity: O(n).
- Why does doubling reduce the cost overall? It makes resizing happen less often.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for num in nums:
        total += num
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It keeps a running sum instead of adding previous numbers again.
- Could it be optimized? The running sum is already efficient. Extra space could be reduced by changing the original list.
"""
