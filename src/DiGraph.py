from src.GraphInterface import GraphInterface

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].Edgeout

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].Edgeout

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes[id1] is None or self.nodes[id2] is None:
            return False
        self.nodes[id1].Edgeout[id2] = weight
        self.nodes[id2].Edgein[id1] = weight
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
        self.mc += 1
        return True


    def remove_node(self, node_id: int) -> bool:
        if self.nodes._contains_(node_id):
              self.nodes.pop(node_id)
              self.mc+=1
              return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.nodes[node_id2].Edgein and node_id2 in self.nodes[node_id1].Edgeout:
            self.nodes[node_id1].Edgeout.pop(node_id2)
            self.nodes[node_id2].Edgein.pop(node_id1)
            self.mc += 1
            return True
        return False

    def __repr__(self):
        return f'{self.nodes} 'f'{self.edges}'


class Node():
    def __init__(self, id: int,weight:float, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.Edgein = {}
        self.Edgeout = {}
        self.weight = weight


    def __repr__(self):
        return f'key = {self.id},' f'pos = {self.pos}'


if __name__ == '__main__':
    g = DiGraph()
    # file= '../data/A5.json'
    # # g.load_from_json("A3.json")
    for n in range(3):
     g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    # g.add_edge(2, 3, 1.1)
    # g.add_edge(1, 3, 1.9)
    g.remove_edge(1,0)
    # g.add_edge(1, 3, 10)
    # g.remove_node(1)

    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
