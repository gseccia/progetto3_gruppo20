from TdP_collections.graphs.graph import Graph
from pkg_4.bipartite import bipartite

def print_partitions(X,Y):
    sol = ""
    for elem in X:
        sol += str(elem)
        sol += ", "
    print("\nprima   partizione composta da : ", sol)
    sol = ""
    for elem in Y:
        sol += str(elem)
        sol += ", "
    print("seconda partizione composta da : ", sol)


print("---------------------------------------- TEST_BIPARTITE ----------------------------------------")
print("******* CASO 1 *******")
print("Grafo composto da due componenti non connesse tra di loro ma entrambe bipartibili\n**********************")
g = Graph()
v = []
for i in range(1, 9):
    v.append(g.insert_vertex(i))
print("Prima componente connessa composta da 1, 2, 3, 4, 5, 6, 7, 8")
g.insert_edge(v[0], v[1])
g.insert_edge(v[0], v[3])
g.insert_edge(v[2], v[1])
g.insert_edge(v[2], v[3])
g.insert_edge(v[2], v[5])
g.insert_edge(v[4], v[3])
g.insert_edge(v[4], v[5])
g.insert_edge(v[4], v[7])
g.insert_edge(v[6], v[5])
g.insert_edge(v[6], v[7])

print("Seconda componente connessa composta da 9,10")
v1 = g.insert_vertex(9)
v2 = g.insert_vertex(10)
g.insert_edge(v1, v2)

partitions = bipartite(g)
if partitions is not None:
    print_partitions(partitions[0], partitions[1])

print("\n\n******* CASO 2 *******")
print("Grafo composto da due componenti non connesse tra di loro ed una delle due non è bipartibile\n**********************")
g = Graph()
v = []
for i in range(1, 9):
    v.append(g.insert_vertex(i))
print("Prima   componente connessa composta da 1, 2, 3, 4, 5, 6, 7, 8, la componente presenta un autociclo 6-6")
g.insert_edge(v[0], v[1])
g.insert_edge(v[0], v[3])
g.insert_edge(v[2], v[1])
g.insert_edge(v[2], v[3])
g.insert_edge(v[2], v[5])
g.insert_edge(v[4], v[3])
g.insert_edge(v[4], v[5])
g.insert_edge(v[4], v[7])
g.insert_edge(v[6], v[5])
g.insert_edge(v[6], v[7])
#aggiungo un autociclo
g.insert_edge(v[6], v[6])

print("Seconda componente connessa composta da 9,10")
v1 = g.insert_vertex(9)
v2 = g.insert_vertex(10)
g.insert_edge(v1, v2)

partitions = bipartite(g)
if partitions is None:
    print("\nIl grafo non è bipartibile")

