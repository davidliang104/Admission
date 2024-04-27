import unittest
from mat_to_list import mat_to_list
from reachable import reachable

class Tests(unittest.TestCase):
    def test_mat_to_list(self):
        # test on a graph
        adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(mat_to_list(adj_mat), adj_list)

        # test on another graph
        adj_mat =   [[0, 1],
                     [0, 1]]
        adj_list = [[1], [1]]
        self.assertEqual(mat_to_list(adj_mat), adj_list)

        # test on empty graph
        adj_mat =   []
        adj_list = []
        self.assertEqual(mat_to_list(adj_mat), adj_list)

        # test on graph with one node
        adj_mat =   [[0]]
        adj_list = [[]]
        self.assertEqual(mat_to_list(adj_mat), adj_list)

    def test_reachable(self):
        # test on a graph
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        # from node 0
        start_node = 0
        reachable_set = {0, 1, 2, 3, 4}
        self.assertEqual(reachable(adj_list, start_node), reachable_set)
        # from node 3
        start_node = 3
        reachable_set = {3, 4}
        self.assertEqual(reachable(adj_list, start_node), reachable_set)
        # from non-existant node
        start_node = 10
        reachable_set = set()
        self.assertEqual(reachable(adj_list, start_node), reachable_set)

        # test on another graph
        adj_list = [[1], [1]]
        # from node 0
        start_node = 0
        reachable_set = {0, 1}
        self.assertEqual(reachable(adj_list, start_node), reachable_set)
        # from node 1
        start_node = 1
        reachable_set = {1}
        self.assertEqual(reachable(adj_list, start_node), reachable_set)
        # from non-existant node
        start_node = 10
        reachable_set = set()
        self.assertEqual(reachable(adj_list, start_node), reachable_set)

        # test on empty graph
        adj_list = []
        start_node = 0
        reachable_set = set()
        self.assertEqual(reachable(adj_list, start_node), reachable_set)

        # test on graph with 1 node
        adj_list = [[0]]
        start_node = 0
        reachable_set = {0}
        self.assertEqual(reachable(adj_list, start_node), reachable_set)

if __name__ == '__main__':
    unittest.main()