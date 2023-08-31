from sys import maxsize


class Dijkstra:
    def __init__(self) -> None:
        self.edges = []  # tuples (node, node, weight)
        self.nodes = set()

    def add_node(self, node):
        self.nodes.append(node)

    def set_nodes(self, nodes):
        self.nodes = nodes

    def add_edge(self, edge):
        self.edges.append(edge)

    def set_edges(self, edges):
        self.edges = edges

        nodes = []
        for edge in self.edges:
            nodes.append(edge[0])
            nodes.append(edge[1])

        self.set_nodes(list(set(nodes)))

    def calculate_shortest_path(self, source, destination):
        # initialize values
        path_cost = {}
        previous_node = {}
        not_visited_nodes = []

        for node in self.nodes:
            path_cost[node] = maxsize  # pseudo infinity
            not_visited_nodes.append(node)

        path_cost[source] = 0

        # analize the neighbours
        while destination in not_visited_nodes:
            current_node = sorted(not_visited_nodes)[0]

            for edge in self.edges:
                dest = None

                if edge[0] == current_node:
                    dest = edge[1]

                if edge[1] == current_node:
                    dest = edge[0]

                if dest is None or dest not in not_visited_nodes:
                    continue

                new_cost = path_cost[current_node] + edge[2]

                if path_cost[dest] > new_cost:
                    path_cost[dest] = new_cost
                    previous_node[dest] = current_node

            not_visited_nodes.remove(current_node)

        # calculate the path
        path = []
        path.append(destination)
        next_node = previous_node[destination]
        while next_node != None:
            path.append(next_node)
            next_node = previous_node.get(next_node)

        path.reverse()
        return path
