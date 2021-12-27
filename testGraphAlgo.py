import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import os

class testDiGraph(unittest.TestCase):
    def test_Vsize(self):
        graph = GraphAlgo()
        graph.load_from_json("../data/jtest.json")
        self.assertEqual(graph.graph.v_size(), 8)

    def test_esize(self):
        graph=GraphAlgo()
        graph.load_from_json("../data/jtest.json")
        self.assertEqual(graph.graph.e_size(), 10)

    def test_get_all_v(self):
        graph=GraphAlgo()
        graph.load_from_json("../data/jtest.json")
        self.assertTrue(graph.graph.nodes.get(5) is not None)


    def test_all_in_and_out(self):
        graph = DiGraph()
        graph.add_node(1, (1, 7, 0));
        graph.add_node(2, (2, 7, 0));
        graph.add_node(3, (0, 7, 0));
        graph.add_edge(1, 2, 1.5)
        graph.add_edge(2, 1, 3);
        graph.add_edge(1, 3, 6);

        edges_out_1 = graph.all_out_edges_of_node(1)
        edges_in_1 = graph.all_in_edges_of_node(1)
        edges_in_2 = graph.all_in_edges_of_node(2)
        edges_out_3 = graph.all_out_edges_of_node(3)

        self.assertEqual(len(edges_out_1), 2, "didn't get the right dictionary")
        self.assertEqual(edges_out_1[2], 1.5, "not found edge 1_2")

        self.assertEqual(len(edges_in_1), 1, "didn't get the right dictionary")
        self.assertEqual(edges_in_1[2], 3, "not found edge 2_1")

        self.assertEqual(len(edges_in_2), 1, "didn't get the right dictionary")
        self.assertEqual(edges_in_2[1], 1.5, "not found edge 1_2")

        self.assertEqual(len(edges_out_3), 0, "didn't get the right dictionary")

        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(1, 4, 14)
        graph.add_edge(1, 2, 12)
        graph.add_edge(2, 1, 21)
        graph.add_edge(1, 3, 13)
        graph.add_edge(2, 3, 23)
        graph.add_edge(3, 1, 31)
        self.assertEqual(graph.all_out_edges_of_node(1), {4: 14, 2: 12, 3: 13})
        self.assertEqual(graph.all_in_edges_of_node(1), {2: 21, 3: 31})

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(0);
        graph.add_node(1);
        graph.add_node(2);
        self.assertFalse((1, 0) in graph.edges, "opposite direction edge not suppose to be created")
        self.assertTrue(graph.add_edge(0, 1, 0.76), "2")
        self.assertEqual(graph.edges[0, 1], 0.76, "the edge did remain the same")

    def test_add_node(self):
        graph = DiGraph()
        # add 4 new nodes
        self.assertTrue(graph.add_node(0))
        self.assertTrue(graph.add_node(1, (2, 5)))
        self.assertTrue(graph.add_node(2))
        self.assertTrue(graph.add_node(3))
        self.assertFalse(5 in graph.nodes)
        self.assertTrue(1 in graph.nodes)
        self.assertEqual(graph.nodes[2].pos, None, " didn't get the right node")

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(0);
        graph.add_node(1);
        graph.add_node(2);
        self.assertTrue(graph.remove_node(1))
        self.assertFalse(1 in graph.nodes, "didn't delete node 1")

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(0);
        graph.add_node(1);
        graph.add_node(2);
        graph.add_edge(1, 2, 1.5);
        graph.add_edge(2, 1, 3);
        graph.add_edge(1, 3, 6);
        mc = graph.get_mc()
        self.assertTrue(graph.remove_edge(1, 2))
        self.assertTrue((1, 2) in graph.edges, "delete edge ");
        self.assertFalse((0, 1) in graph.edges, "didn't return false for not existing edge.");
        self.assertTrue(mc + 1 <= graph.get_mc(), "didn't update mc correctly");

class testGraphAlgo(TestCase):

    # def test_loadFrom_json(self):
    #     graph = GraphAlgo()
    #     self.assertTrue( graph.load_from_json("../data/A5.json"))
    #     self.assertTrue(graph.save_to_json("test.json"))

    def test_save(self):
        graph= GraphAlgo()
        graph.load_from_json("../data/A2.json")
        self.assertTrue(graph.save_to_json("test.json"))
        os.remove("test.json")

    def test_shortest_path(self):
        graph = GraphAlgo()
        graph.load_from_json("../data/A3.json")
        self.assertEqual(graph.shortest_path(1,8),(2.2807243078636805, [1, 26, 8]))


    def test_TSP(self):
        graph = GraphAlgo()
        graph.load_from_json("../data/A2.json")
        self.assertEqual(graph.TSP([1,2,3,4,5]),([1, 2, 3, 4, 5,1], 10.421136656845679))


    def test_centerPoint(self):
        graph = GraphAlgo()
        graph.load_from_json("../data/A2.json")
        self.assertEqual(graph.centerPoint(), [(0, 7.819910602212574)])

