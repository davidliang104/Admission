def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    
    adj_list = []
    for neighbors in adj_mat:
        neigh_list = []
        for i, neighbor in enumerate(neighbors):
            if neighbor == 1:
                neigh_list.append(i)
        adj_list.append(neigh_list)

    return adj_list