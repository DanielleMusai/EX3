import json
import matplotlib.pyplot as plt
import numpy as np


class Node:
    # count=0
    def __init__(self, pos: dict, id) -> None:
        self.pos = pos
        self.id = id

    def __repr__(self) -> str:
        return f"id: pos:{self.pos}{self.id}"

class Graph:
    def __init__(self,nodes={},edges={}) -> None:
        self.nodes = nodes
        self.edges = edges

    def add_node(self, id, pos=(0, 0)):
        self.nodes[id] = Node(id, {'x': pos[0], 'y': pos[1]})
        self.edges[id] = {}
        return self

    def connect(self, src, dest, w=0):
        if src in self.nodes.keys() and dest in self.nodes.keys():
            self.edges[src][dest] = w

    def save_to_json(self, file):
        with open(file, 'w') as f:
            json.dump(self, indent=2, fp=f, default=lambda a: a.__dict__)

    def load_from_json(self, file):
        dict = {}
        with open(file, "r") as f:
            dict = json.load(f)
        for n in dict["nodes"].values():
            self.add_node(n["id"], (n['pos']['x'], n['pos']['y']))
        for src, out in dict["edges"].items():
            for dest, w in out.items():
                print(src, dest, w)
                self.connect(int(src), int(dest), w)

    def __str__(self) -> str:
        return f"nodes: {self.nodes}\nedges: {self.edges}"

import random
def plot(g: Graph):
    for v in g.nodes.values():
        x, y = v.pos['x'], v.pos['y']
        print(x,y)
        plt.plot(x,y,markersize=4,marker='o',color='pink')
        plt.text(x, y, str(v.id), color="grey", fontsize=12)
        for nai,w in g.edges[v.id].items():
            u=g.nodes[nai]
            x_,y_=u.pos['x'], u.pos['y']
            plt.annotate("",xy=(x,y),xytext=(x_,y_), arrowprops=dict(arrowstyle="<-"))

    plt.show()

def load_graph(dict):
    if "id" in dict:
        return Node(**dict)
    if "nodes" in dict:
        nodes={int(id): n for id,n in dict['nodes'].items()}
        edges={int(src):{int(dest): w for dest,w in nai.items()} for src,nai in dict["edges"].items()}
        return Graph(nodes=nodes,edges=edges)
    return dict



# if __name__ == '__main__':
#     g = Graph()
#     for i in range(10):
#         x, y=random.uniform(0,100),random.uniform(0,100)
#         g.add_node(i, pos=(x, y))
#     for i in range(10):
#         for j in range(0,i,2):
#             if i != j:
#                 g.connect(i, j, 0)
#    # g.save_to_json("A1.json")
#     A2 = Graph()
#     print(A2)
#     A2.load_from_json("A2.json")
#     print(A2)
#    # A2.save_to_json("A2.json")
#     plot(A2)
#     with open("A2.json","r") as f:
#         A3=json.load(fp=f,object_hook=load_graph)
#     print(A3)
