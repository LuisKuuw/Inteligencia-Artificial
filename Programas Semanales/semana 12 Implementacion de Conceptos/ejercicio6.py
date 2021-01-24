def MONTE_CARLO_TREE_SEARCH(state):
    tree = node.children(state)
    while TIME-REMAINING():
        leaf = select(tree)
        child = expand(leaf )
        result = simulate(child )
        back_propagate(result, child )

return state