import copy
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
import random
import numpy as np
from numpy import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()) -> None:
        self.graph = graph
        self.src = 0
        self.mc = 0
        self.listOfroads = {}
        self.daddys = {}
        self.D = {}
        self.inf = float("inf")

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


    def shortest_path(self, id1: int, id2: int) -> (float, list):
         if id2 not in self.graph.nodes or id1 not in self.graph.nodes:
             list =[]
             list.append(self.inf)
             list.append([])
         if id2 is None and id1 is None:
             return 0
         if id1 == id2:# equal
             return 0, id1
         else:
             self.dijk(id1)
             self.Bpath(id2)
             return (self.D[id2],self.listOfroads[id2])


    def findAway(self, list: list, s: int):
        list1 = []
        list1.append(s)
        list.remove(s)
        count = 0
        index = 0
        n = s
        while list:
            self.dijk(n)
            min = self.D.get(list[0])
            for j in list:
                if self.D.get(j) <= min:
                    min, index= self.D.get(j),j
            count += min
            n = index
            list.remove(n)
            list1.append(n)
        list1.append(s)
        self.dijk(n)
        count += self.D.get(s)
        return [list1, count]

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        min = self.inf
        list1= []
        for i in node_lst:
            flag = self.findAway(copy.deepcopy(node_lst),i)
            if flag[1] < min:
                min = flag[1]
                list1 = flag[0]
        return (list1,min)


    def centerPoint(self) -> (int, float):
        num = (0, self.inf)
        for n in self.graph.nodes:
            self.dijk(n)
            max1 = (n, max(self.D.values()))
            if num[1] > max1[1]:
                num = max1
        list = []
        list.append(num)
        return list

    def __repr__(self) -> str:
        return f'{self.graph}'


    def dijk(self, src: int) -> bool:
        self.src = src
        list = []
        self.initE(self.daddys, list)
        while len(list) != 0:  # check the min
            min_ = self.inf
            minM = -self.inf
            for i in list:
                if min_ > self.D[i]:
                    minM = i
                    min_ = self.D[i]
            if minM != -self.inf:
                list.remove(minM)
            if minM == -self.inf:
                return
            for e in self.graph.all_out_edges_of_node(minM):  # update the weight
                update = self.D[minM] + self.graph.edges[(minM, e)]
                if update < self.D[e]:
                    self.D[e] = update
                    self.daddys[e] = minM
        return True

    def initE(self, parents: dict, list: list): # if there is edge between nodes put a weight or infinity
        for i in self.graph.nodes.keys():
            if i == self.src:
                parents[self.src] = -1
                self.D[self.src] = 0
                self.listOfroads[self.src] = []
                list.append(self.src)
            else:
                self.D[i] = self.inf
                parents[i] = self.inf
                list.append(i)
                self.listOfroads[i] = []



    def Bpath(self, i :int): # add a path between two nodes
        if self.listOfroads[i].__len__() != 0:
            return
        if i == self.src:
            self.listOfroads[i].append(i)
            return
        c = self.daddys[i]
        v = self.listOfroads[i]
        if c == self.inf:
            return
        if self.listOfroads.__contains__(c):
            self.Bpath(c)
        v.extend(self.listOfroads[c])
        v.append(i)


    def plot_graph(self): # the matplotlib part
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
