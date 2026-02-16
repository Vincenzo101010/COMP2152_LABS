print("\n" + "=" * 50)
print("Question 4: First Unique Character")
print("=" * 50)


# Helper function: Count all characters in a string
def count_characters(s):
    """
    Count occurrences of each character in a string.

    Parameters:
        s (str): Input string

    Returns:
        dict: Dictionary with character counts
    """
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


# Main function: Find first unique character
def first_unique_character(s):
    """
    Find the index of the first non-repeating character.

    Parameters:
        s (str): Input string

    Returns:
        int: Index of first unique character, or -1 if none
    """
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)

    # Step 2: Loop through string with index to find first unique
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    # Step 3: Return -1 if no unique character found
    return -1


# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()