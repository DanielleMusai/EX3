from GraphInterface import GraphInterface


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
        return self.nodes[id1].Edgein

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].Edgeout

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 is not self.nodes or id2 is not self.nodes:
            return False
        self.edges[(id1, id2)] = weight
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
        if self.nodes.__contains__(node_id):
            self.nodes.pop(node_id)
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


class Node:
    def __init__(self, key: int, pos: tuple) -> None:
        self.key = key
        self.pos = pos
        self.Edgein = {}
        self.Edgeout = {}
        self.weight ={}


    def __repr__(self):
        return f'key = {self.key},' f'pos = {self.pos}'

