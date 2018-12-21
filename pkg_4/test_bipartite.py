from TdP_collections.graphs.graph import Graph
from pkg_4.bipartite import bipartite

g = Graph()
v = []
for i in range(1, 9):
    v.append(g.insert_vertex(i))
g.insert_edge(v[0],v[1])
g.insert_edge(v[0],v[3])
g.insert_edge(v[2],v[1])
g.insert_edge(v[2],v[3])
g.insert_edge(v[2],v[5])
g.insert_edge(v[4],v[3])
g.insert_edge(v[4],v[5])
g.insert_edge(v[4],v[7])
g.insert_edge(v[6],v[5])
g.insert_edge(v[6],v[7])

#altra componente bipartibile non connessa alla prima
v1 = g.insert_vertex(9)
v2 = g.insert_vertex(10)
g.insert_edge(v1,v2)

# g.insert_edge(v[6],v[6])

X,Y = bipartite(g)
print("X partition")
for elem in X:
    print(elem)

print("Y partition")
for elem in Y:
    print(elem)