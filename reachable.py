def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    
    reachable = set()

    # return empty set if list is empty or start_node is larger than size of adj_list
    if not adj_list or start_node >= len(adj_list):
        return reachable

    visited = set()
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            reachable.add(node)
            visited.add(node)
            neighbors = adj_list[node]
            for neighbor in neighbors:
                stack.append(neighbor)

    return reachable