from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
import sys
import json
import matplotlib.pyplot as plt
import random
import numpy as np


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph


    def get_graph(self) -> GraphInterface:
        return self.graph



    def load_from_json(self, file_name: str) -> bool:
        try:
            di_graph = self.graph
            with open(file_name) as json_file:
                graph_json = json.load(json_file)
                json_file.close()
                # load nodes
                for node in graph_json['Nodes']:
                    di_graph.add_node(node['id'])
                    if 'pos' in node:
                        pos = node['pos'].split(',')
                        di_graph.nodes[node['id']].pos = [float(x) for x in pos]
                # load edges
                for edge in graph_json['Edges']:
                    di_graph.add_edge(edge['src'], edge['dest'], edge['w'])
                self.graph=di_graph
                return True

        except FileNotFoundError:
            print("not found " + file_name)
            return False



    def save_to_json(self, file_name: str) -> bool:
        Edges=[]
        Nodes=[]
        dict = {}
        for node in self.graph.nodes.values():
            if node.pos is not None:
                Nodes.append({"id": node.key,"pos":f'{node.pos[0]},{node.pos[1]},{node.pos[2]}'})
            else:
                Nodes.append({"id": node.key,"pos": None})
        for edge in self.graph.edges:
             Edges.append({"src": edge[0],"dest": edge[1],"w": self.graph.edges[edge]})
        dict["Nodes"] = Nodes
        dict["Edges"] = Edges
        try:
            file = open(file_name, 'w')
        except IOError:
            return False
        file.write(json.dumps(dict))
        file.close()
        return True

    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self):
        g = self.graph
        nodes = g.nodes
        plt.xlabel(" X-Axis ")
        plt.ylabel(" Y-Axis ")
        plt.title("The Graph")
        for node in nodes.values():
            x = float(node.pos[0])
            y = float(node.pos[1])
            plt.annotate("{:}".format(node.key),  # this is the text
                         xy=(x, y),  # this is the point to label
                         xytext=(0, 7), ha='center',
                         textcoords='offset points',  #position of the text
                         color='purple')
            plt.plot(x, y, markersize=5, marker="o", color="lightblue")
            for edge in self.graph.all_out_edges_of_node(node.key):
                index_src = float(self.graph.nodes[edge].pos[0])
                index_dest= float(self.graph.nodes[edge].pos[1])
                plt.annotate('', xy=(x, y), xycoords='data',
                             xytext=(index_src, index_dest), textcoords='data',
                             arrowprops=dict(facecolor='black', arrowstyle='<| -'))

        plt.show()




if __name__ == '__main__':
    g = DiGraph()  # creates an empty directed graph
    # for n in range(4):
    #     g.add_node(n)
    # g.add_edge(0, 1, 1)
    # g.add_edge(1, 0, 1.1)
    # g.add_edge(1, 2, 1.3)
    # g.add_edge(2, 3, 1.1)
    # g.add_edge(1, 3, 1.9)
    # g.remove_edge(1, 3)
    # g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    # print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    # print(g_algo.shortest_path(0, 3))
    # g_algo.plot_graph()
    g_algo.load_from_json('../data/A4.json')
    # print(g_algo)
    g_algo.plot_graph()
