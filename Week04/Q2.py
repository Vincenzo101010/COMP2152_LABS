# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    """
    Find two numbers that add up to target using nested loops.

    Parameters:
        numbers (list): List of integers
        target (int): Target sum

    Returns:
        tuple: Indices of the two numbers, or None if not found
    """
    # Outer loop: go through each number
    for i in range(len(numbers)):
        # Inner loop: check every number after i
        for j in range(i + 1, len(numbers)):
            # Check if this pair adds up to target
            if numbers[i] + numbers[j] == target:
                return (i, j)

    # No pair found
    return None


# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    """
    Find two numbers that add up to target using dictionary lookup.

    Parameters:
        numbers (list): List of integers
        target (int): Target sum

    Returns:
        tuple: Indices of the two numbers, or None if not found
    """
    seen = {}  # Dictionary to store {number: index}

    for i in range(len(numbers)):
        # Calculate what number we need to reach target
        needed = target - numbers[i]

        # Check if we've seen the needed number before
        if needed in seen:
            return (seen[needed], i)

        # Store current number and its index
        seen[numbers[i]] = i

    # No pair found
    return None


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("\n=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    if result is not None:
        print("  -> " + str(numbers[result[0]]) + " + " + str(numbers[result[1]]) + " = " + str(target))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    if result is not None:
        print("  -> " + str(numbers[result[0]]) + " + " + str(numbers[result[1]]) + " = " + str(target))
    print()