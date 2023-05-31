
MINUS_INFINITE = -1000
PLUS_INFINITE = 1000
counter = 0


# recursive implementation of min max algorithm 
# min player chooses the min value, max player chooses the max value 


def minimax_min(tree, node, alpha, beta, verbose=False):
    global counter

    if isinstance(node,int): # if its a leaf , base case , we stop and print the value 
        # if its a leaf, base case, we stop and print the value 
    
        if verbose:
            # print("Evaluating node", node)
            counter +=1
        return node

    else:

        best_value = PLUS_INFINITE
        for child in tree[node]:

            child_value = minimax_max(tree, child, alpha, beta, True)

            best_value = min(best_value, child_value)

            beta = min(beta, best_value)

            if beta <= alpha:
                break

        return best_value

def minimax_max(tree, node, alpha, beta,verbose=False):
    global counter
    if isinstance(node,int): # if its a leaf , base case , we stop and print the value 
        # print("evaluating node", node)
        counter +=1

        return node
    else:
        best_value = MINUS_INFINITE

        for child in tree[node]:
            child_value = minimax_min(tree, child, alpha, beta, True)

            best_value = max(best_value, child_value)

            alpha = max(alpha, best_value)

            if beta <= alpha:
                break
        return best_value


if __name__ == '__main__':

    # Adversarial search: Minimax tre with Alpha-beta pruning (slide 101). It shows the leaves evaluated during the search

    game = {'A': ['B', 'C'], 'B': [8, 6], 'C': [9, 2, 1]}
    
    print ("\nMinimax showing the leaves evaluated during the search \n")

    print (game, "\n")
    
    counter = 0
    print("The optimal value for a Max player is", minimax_max(game, 'A', MINUS_INFINITE, PLUS_INFINITE, True), "after exploring", counter, "nodes \n")

    counter = 0  
    print("The optimal value for a Min player is", minimax_min(game, 'A', MINUS_INFINITE, PLUS_INFINITE, True), "after exploring", counter, "nodes \n")

    # Adversarial search: Minimax tre with Alpha-beta pruning (slide 119). It shows the leaves evaluated during the search
            
    game = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [2, 3], 'E': [5, 9], 'F': [1, 2], 'G': [4, 6]}
    
    print ("\nMinimax showing the leaves evaluated during the search \n")

    print (game, "\n")

    counter= 0
    #calling game starting at node A (starting at the top of the tree)
    print("The optimal value for a Max player is", minimax_max(game, 'A', MINUS_INFINITE, PLUS_INFINITE, True), "after exploring", counter, "nodes \n")
    counter= 0
    print("The optimal value for a Min player is", minimax_min(game, 'A', MINUS_INFINITE, PLUS_INFINITE, True), "after exploring", counter, "nodes \n")




