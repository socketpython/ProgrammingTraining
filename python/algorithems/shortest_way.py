import queue


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.distance = 0
        self.previous = None

    def __hash__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __cmp__(self, other):
        return self.value == other.value


class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_neighbour(self, source, dest):
        self.graph[source].append(dest)

    def bfs(self, s):
        q = queue.Queue()

        q.put(s)
        s.previous = s
        s.dist = 0

        while not q.empty():
            temp_vertex = q.get()
            for neighbour in self.graph[temp_vertex]:
                if neighbour.previous is None:
                    q.put(neighbour)
                    neighbour.distance = temp_vertex.distance + 1
                    neighbour.previous = temp_vertex

    def find_shortest_path(self, src, dst):
        self.bfs(src)
        if dst.previous is None:
            print("Not path to destination :(")
            return
        print(f"Path length: {dst.distance}")

        current = dst
        path = ""
        while current != src:
            path = "-> " + str(current) + " " + path
            current = current.previous
        print(str(src) + " " + path)


def main():
    v0 = Vertex(0)
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)
    v5 = Vertex(5)
    v6 = Vertex(6)
    v7 = Vertex(7)

    vertexes = [v0, v1, v2, v3, v4, v5, v6, v7]

    g = Graph()
    for vertex in vertexes:
        g.add_vertex(vertex)

    g.add_neighbour(v0, v1)
    g.add_neighbour(v0, v2)
    g.add_neighbour(v0, v3)
    g.add_neighbour(v2, v4)
    g.add_neighbour(v2, v5)
    g.add_neighbour(v1, v3)
    g.add_neighbour(v3, v5)
    g.add_neighbour(v5, v4)
    g.add_neighbour(v4, v2)
    g.add_neighbour(v2, v3)
    g.add_neighbour(v3, v0)
    g.add_neighbour(v3, v6)
    g.add_neighbour(v6, v7)
    g.add_neighbour(v7, v1)

    g.find_shortest_path(v2, v1)


if __name__ == '__main__':
    main()
