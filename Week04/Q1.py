print("\n" + "=" * 50)
print("Question 1: Robot Return to Origin")
print("=" * 50)


def robot_returns_to_origin(moves):
    """
    Check if robot returns to origin (0,0) after all moves.

    Parameters:
        moves (str): String of moves (U, D, L, R)

    Returns:
        bool: True if robot returns to origin, False otherwise
    """
    # Initialize starting position
    x = 0
    y = 0

    # Loop through each move and update position
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "R":
            x += 1
        elif move == "L":
            x -= 1

    # Return True if back at origin (both x and y are 0)
    return x == 0 and y == 0


# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))