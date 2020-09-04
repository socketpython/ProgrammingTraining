import math
import heapq


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.distance = math.inf
        self.previous = None

    def __hash__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __cmp__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.distance > other.distance


class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_neighbour(self, src, dst, weight):
        self.graph[src].append((dst, weight))

    def dijxtra(self, src):
        src.distance = 0
        unvisited = []
        for k in self.graph.keys():
            unvisited.append(k)

        heapq.heapify(unvisited)

        while len(unvisited) > 0:
            v = heapq.heappop(unvisited)
            print("Now at Vertex", v)
            for neighbour in self.graph[v]:

                neighbour_vertex, neighbour_distance = neighbour
                print("\tNeighbour:", neighbour_vertex)
                distance = v.distance + neighbour_distance
                print(f"\tCurrent distance: {neighbour_vertex.distance}, New distance {distance}")
                if distance < neighbour_vertex.distance:
                    print("\t\tChanging!")
                    neighbour_vertex.distance = distance
                    neighbour_vertex.previous = v
                    heapq.heapify(unvisited)
                    print(f"\t\t Post: distance={neighbour_vertex.distance}, previous {neighbour_vertex.previous}")


def main():
    v0 = Vertex(0)
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)

    g = Graph()
    g.add_vertex(v0)
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_vertex(v3)
    g.add_vertex(v4)
    g.add_vertex(v5)
    g.add_vertex(v6)

    g.add_neighbour(v0, v1, 3)
    g.add_neighbour(v0, v2, 2)
    g.add_neighbour(v0, v3, 10)
    g.add_neighbour(v1, v6, 2)
    g.add_neighbour(v6, v3, 1)
    g.add_neighbour(v2, v4, 12)
    g.add_neighbour(v2, v5, 4)
    g.add_neighbour(v5, v3, 8)
    g.add_neighbour(v5, v4, 4)

    g.dijxtra(v0)
    print("Distance to v3:", v3.distance)
    print("Distance to v4:", v4.distance)
    print(v4.previous, v4.previous.previous, v4.previous.previous.previous)


if __name__ == "__main__":
    main()
