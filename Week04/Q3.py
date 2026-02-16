print("\n" + "=" * 50)
print("Question 3: Shuffle the Array")
print("=" * 50)


def shuffle_array(nums, n):
    """
    Interleave first half and second half of array.

    Parameters:
        nums (list): List of 2n elements
        n (int): Half the length of the list

    Returns:
        list: Shuffled list [x1, y1, x2, y2, ...]
    """
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # Elements from index 0 to n-1
    second_half = nums[n:]   # Elements from index n to end

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])   # Add from first half
        result.append(second_half[i])  # Add from second half

    return result


# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()