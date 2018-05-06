import random
import collections


def min_cut(vertices, edges):
    if len(vertices) == 2:
        return len(edges)
    edge = random.choice(edges)
    edges.remove(edge)
    left_vertex = edge[0]
    right_vertex = edge[1]

    for l, r in list(edges):
        if l == right_vertex:
            edges.remove((l, r))
            edges.append((left_vertex, r))
        if r == right_vertex:
            edges.remove((l, r))
            edges.append((l, left_vertex))
    for l, r in list(edges):
        if l == r:
            edges.remove((l, r))

    vertices.remove(right_vertex)
    return min_cut(vertices, edges)

def run(times):
    vertices = set([])
    edges = []
    with open('./graph.txt') as f:
        for l in f:
            arr = [int(x) for x in l.split()]
            vertex = arr.pop(0)
            vertices.add(vertex)
            for adjacent in arr:
                edge = (vertex, adjacent)
                if (vertex, adjacent) not in edges and (adjacent, vertex) not in edges:
                    edges.append(edge)

    result = min_cut(set(vertices), list(edges))
    for _ in range(0, times):
        attempt = min_cut(set(vertices), list(edges))
        if attempt < result:
            result = attempt
    print(result)

#         # lookup table with value of superseded node
        # delete link(s?) to both nodes in both lists
        # add superseded node as lookup to new added node