from typing import List
from src import GraphInterface
import json
class GraphAlgoInterface(GraphInterface):
    def _int_(self,G :int=None ,node:int=None ,edge:int=None,weight:int=None):
        GraphInterface._init_(self)
        self.graph = G
        self.node=node
        self.edge=edge
        self.weight=weight


    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as f:
                new_g={}
                my_d=json.load(f)
                self.node=my_d["Nodes"]
                Edges_d=my_d["Edges"]
                for k,v in Edges_d.items():
                    g = GraphInterface(src=v["src"],w=v["w"],dest=v["dest"])
                    new_g[g.w]=g
                self.graph=new_g
                return True
        except IOError as e:
            print(e)
            return False


    def save_to_json(self, file_name: str) -> bool:
       try:
           with open(file_name, "w") as f:
               json.dump(self, indent=4, fp=f,defult=lambda a:a._dict_)
       except IOError as false:
        return false


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

    # def iterator(self, )->:
    # 
    # def Dijkstras(self,)->:
        

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

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
