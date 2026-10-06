
GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0)

def print_board(state):
    """Helper function to print the 3x3 board cleanly."""
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print("-" * 11)

def get_moves(state):
    """Finds all valid next states by moving the empty tile (0)."""
    moves = []
    empty_idx = state.index(0)
    row, col = empty_idx // 3, empty_idx % 3

    # Define possible movements: (row_change, col_change, move_name)
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

    for dr, dc, move_name in directions:
        new_row, new_col = row + dr, col + dc
        
        # Check if the move stays within the 3x3 grid boundaries
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            
            # Convert tuple to list to swap elements, then convert back
            new_state = list(state)
            new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
            moves.append((tuple(new_state), move_name))
            
    return moves

def dfs_8_puzzle(start_state, max_depth=20):
    """Solves the 8-puzzle using Depth-First Search up to a maximum depth limit."""
    # The stack stores: (current_state, path_taken, current_depth)
    stack = [(start_state, [], 0)]
    visited = set()

    while stack:
        current_state, path, depth = stack.pop()

        # Target state found
        if current_state == GOAL_STATE:
            return path

        if current_state in visited or depth > max_depth:
            continue

        visited.add(current_state)

        # Explore neighbors (reversed so they are popped in a natural order)
        for next_state, move in reversed(get_moves(current_state)):
            if next_state not in visited:
                stack.append((next_state, path + [move], depth + 1))

    return None  # No solution found within depth limit

# --- Execution Example ---
if __name__ == "__main__":
    # 0 represents the empty tile. This puzzle is 3 moves away from the goal.
    initial_state = (1, 2, 3, 
                     4, 0, 6, 
                     7, 5, 8)

    print("Initial State:")
    print_board(initial_state)

    print("Searching for solution via DFS...")
    solution_path = dfs_8_puzzle(initial_state, max_depth=15)

    if solution_path:
        print(f"🎉 Success! Solution found in {len(solution_path)} moves.")
        print(f"Path sequence: {', '.join(solution_path)}")
    else:
        print("❌ Failed to find a solution within the depth limit.")
