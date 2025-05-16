import math

def alpha_beta_pruning(depth, node_index, is_maximizing_player, values, alpha, beta, path):
    if depth == 3:
        return values[node_index]

    if is_maximizing_player:
        best = -math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, path + [node_index * 2 + i])
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break 
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, path + [node_index * 2 + i])
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break 
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

optimal_path = []
optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf, [0])

print("The optimal value is:", optimal_value)
print("The optimal path is:", optimal_path)
