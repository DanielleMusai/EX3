
class DiGraph():
    def __init__(self):
        self.nodes = {}
        self.edges = 0
        self.mc = 0

    def __repr__(self):
        return "nodes:" + str(self.v_size()) + " , edges:" + str(self.e_size())

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edges

    def get_all_v(self):
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].Edgein

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].Edgeout

    def get_mc(self) -> int:
        return self.mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(node_id, pos)
        self.mc += 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes[id1] is None or self.nodes[id2] is None:
            return False
        self.nodes[id1].Edgeout[id2] = weight
        self.nodes[id2].Edgein[id1] = weight
        self.mc+=1
        self.edges+=1
        return True


    def remove_node(self, node_id: int) -> bool:
        if self.nodes.__contains__(node_id):
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



class Node():
    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.Edgein = {}
        self.Edgeout = {}
        self.weight = {}


    def __repr__(self):
        return "src:" + str(self.Edgein) + " , dest:" + str(self.Edgeout)+", weight:"+ str(self.weight)

if __name__ == '__main__':
    g = DiGraph()
    # file= '../data/A5.json'
    # # g.load_from_json("A3.json")
    for n in range(4):
     g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)


    # g.add_edge(2, 3, 1.1)
    # g.add_edge(1, 3, 1.9)
    # g.remove_edge(1, 3)
    # g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    # print(g.all_in_edges_of_node(1))
    # print(g.all_out_edges_of_node(1))
