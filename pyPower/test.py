import networkx as nx

circuit=nx.Graph()
circuit.add_nodes_from([1,13])

circuit.add_edge(1,2)
circuit.add_edge(2,3)
circuit.add_edge(2,4)
circuit.add_edge(3,5)
circuit.add_edge(4,6)
circuit.add_edge(3,13)
circuit.add_edge(5,7)
circuit.add_edge(6,8)
circuit.add_edge(6,9)
circuit.add_edge(7,8)
circuit.add_edge(7,10)
circuit.add_edge(9,11)
circuit.add_edge(10,11)
circuit.add_edge(11,12)
circuit.add_edge(12,13)
circuit.add_edge(13,1)

path=nx.all_simple_paths(circuit,1,3)

for i in path:
    print(i)