import time

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

    # Define possible movements
    directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

    for dr, dc, move_name in directions:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
            moves.append((tuple(new_state), move_name))
            
    return moves

def depth_limited_dfs(state, path, visited, depth_limit):
    """Recursive helper that performs DFS up to a fixed depth limit."""
    if state == GOAL_STATE:
        return path
    if depth_limit <= 0:
        return None

    visited.add(state)

    for next_state, move in get_moves(state):
        if next_state not in visited:
            result = depth_limited_dfs(next_state, path + [move], visited, depth_limit - 1)
            if result is not None:
                return result

    visited.remove(state)
    return None

def idfs_8_puzzle(start_state, max_depth=20):
    """Main Iterative Deepening loop."""
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_dfs(start_state, [], visited, depth)
        if result is not None:
            return result
    return None

# --- Run Multiple Test Cases ---
if __name__ == "__main__":
    test_cases = [
        ("Simple Scenario (Requires 2 Moves)", (1, 2, 3, 4, 5, 0, 7, 8, 6)),
        ("Moderate Scenario (Requires 4 Moves)", (1, 2, 3, 4, 0, 5, 7, 8, 6)),
        ("Edge-Case Scenario (0 Moves)", (1, 2, 3, 4, 5, 6, 7, 8, 0))
    ]

    for title, state in test_cases:
        print("=" * 50)
        print(f"TEST: {title}")
        print("=" * 50)
        print_board(state)
        
        print("Searching for the optimal solution using IDFS...")
        start_time = time.time()
        solution_path = idfs_8_puzzle(state)
        end_time = time.time()
        
        if solution_path is not None:
            print(f"🎉 Success! Optimal solution found in {len(solution_path)} moves.")
            print(f"Path sequence: {', '.join(solution_path)}")
        else:
            print("❌ Failed to find a solution within the depth limit.")
        print(f"Time taken: {end_time - start_time:.4f} seconds\n")
