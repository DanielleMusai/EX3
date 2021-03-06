# DirectedwightedGraph- Python 
## EX3
<img width="589" alt="Screenshot 2021-12-27 103258" src="https://user-images.githubusercontent.com/92378800/147452351-c14c4ecd-bb31-41ac-b074-c90ad70d6dad.png">



## *project Explanation*
---
Written by Eden Mor and Danielle Musai.  
In this assignment we had to implement a data structure of a directed weighted directed graph 
In Python, the implementation includes the diGraph class as well as the GraphAlgo class. The center idea is to use the previous implementation of our previous assignment and show it in Python, then we needed to compere our solution performance for our previous implementation in Java.
___
### *the interfaces we needed to implement in the class GraphAlgo:*
* get_graph – returns the directed graph on which the algorithm works on.
* save_to_json – Saves the graph in JSON format to a file
* load_from_json – Loads a graph from a json file.
* shortest_path –  Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
* TSP – Finds the shortest path that visits all the nodes in the list 
* centerPoint - Finds the node that has the shortest distance to it's farthest node.
* plot_graph -  Plots the graph.
---
### *the interfaces we needed to implement in the class diGraph:*
*v_size - Returns the number of vertices in this graph
*e_size - Returns the number of edges in this graph
*get_all_v - return a dictionary of all the nodes in the Graph, each node is represented using a pair
*all_in_edges_of_node- return a dictionary of all the nodes connected to (into) node_id
*all_out_edges_of_node- return a dictionary of all the nodes connected from node_id , each node is represented using a pair
*get_mc - Returns the current version of this graph, on every change in the graph state - the MC should be increased
* add_edge - Adds an edge to the graph.
* add_node -  Adds an node to the graph.
*remove_node-  Removes a node from the graph.
*remove_edge-  Removes an edge from the graph.
---
### *Links*
---
in order to implement the shortestpath algorithem we based on the Dijkstra's algorithm:
more infurmation about Dijkstra's algorithm:  
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
https://www.youtube.com/watch?v=pVfj6mxhdMw
---
## *the graph* ##
*The graph consists of nodes and edges  
the node has id, pos, edges-in and edges-out
---
### *the graph*


![graph](https://user-images.githubusercontent.com/93930203/147415745-2fe4c723-19f4-4b80-8682-93e6b615f062.jpeg)
---
### *MATPLOTLIB*
after the graph was created we create a graphical interface on the screen:

plot graph -  The function takes the  graph that with all the nodes and the edges that connect to the nodes and draw it on the screen:
![image](https://user-images.githubusercontent.com/92378800/147418604-1e0f6b71-fdf8-44bd-8801-17378b9d769f.png)
![WhatsApp Image 2021-12-26 at 20 06 07](https://user-images.githubusercontent.com/93930203/147416749-fabbdbac-9e54-44e5-9402-12d3cfeef92b.jpeg)
___
### *wiki
this is the link for our wiki 
you see ther the compering between the 2 projects
https://github.com/DanielleMusai/EX3/wiki
note: we did the last project separate
___
