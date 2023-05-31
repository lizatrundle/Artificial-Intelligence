


def preorder(tree, node):
    # game input as a dictionary, key is the node and value is a list of children 
    if isinstance(node,int):# if its a leaf , base case , we stop and print the value 
        print(node, end =" ")# we dont print until we find a leaf 
    else: # we are not at a leaf and we need to recurse 
        print(node, end = " ")
        for child in tree[node]:
            preorder(tree,child)

    
def postorder(tree,node):

    # game input as a dictionary, key is the node and value is a list of children 

    if isinstance(node,int):# if its a leaf , base case , we stop and print the value 
        print(node, end =" ")# we dont print until we find a leaf 
    else: # we are not at a leaf and we need to recurse 
        for child in tree[node]:
            preorder(tree,child)
        print(node, end = " ")
    




if __name__ == '__main__':

    # Adversarial search: Minimax tree (slide 101)

    game = {'A': ['B', 'C'], 'B': [8, 6], 'C': [9, 2, 1]}

    print ("\nGame ", game, "\n")

    print("preorder")
    preorder(game, 'A')
    print("\n----------")
    print("postorder")
    postorder(game, 'A')   
    print("\n----------")

    # Adversarial search: Minimax tree (slide 119)

    game = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [2, 3], 'E': [5, 9], 'F': [1, 2], 'G': [4, 6]}

    print ("\nGame ", game, "\n")

    preorder(game, 'A')
    postorder(game, 'A')   
    
    