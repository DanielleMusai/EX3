import json
import string

class DiGraph():
    def _init_(self):
        self.graph = {}
        self.mc = 0
        self.G = 0

        def v_size(self) -> int:
            return self.Node._len_()

        def e_size(self) -> int:
            return self.Edge._len()

        def get_all_v(self) -> dict:
            return self.graph

        def all_in_edges_of_node(self, id1: int) -> dict:
            return self.graph.get(id1).Edgein

        def all_out_edges_of_node(self, id1: int) -> dict:
            return self.graph.get(id1).Edgeout

        def get_mc(self) -> int:
            return self.mc

        def add_edge(self, id1: int, id2: int, weight: float) -> bool:
            s = self.graph.get(id1).Edgeout.get(id2)
            s1 = self.graph.get(id1).Edgein.get(id1)
            if s is None and s1 is None:
                self.graph.get(id1).Edgeout[id2] = weight
                self.graph.get(id2).Edgein[id1] = weight
                return True
            else:
               return False

        def add_node(self, node_id: int, pos: tuple = None) -> bool:
            # if self.graph.nodes[node_id] is Node(node_id,pos):
            #     return True
            # else:
                return False

        def remove_node(self, node_id: int) -> bool:
            if self.graph._contains_(node_id):
                self.graph.pop(node_id)
                return True
            return False

        def remove_edge(self, node_id1: int, node_id2: int) -> bool:
            if self.graph.get(node_id1).Edgeout.graph.get(node_id2).Edgein and self.graph.get(node_id2).Edgein.graph.get(node_id1).Edgeout:
             del (self.graph.get(node_id1).Edgeout)[node_id2]
             del (self.graph.get(node_id2).Edgein)[node_id1]
             return True
        return False


if __name__ == '__main__':
    g = DiGraph()
    # g.load_from_json("A3.json")
  
    print(g.add_edge(1, 2, 3.4))
