from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from networkx_widget.node import Node
from networkx import DiGraph, random_layout


class View(QGraphicsView):
    def __init__(self):
        super().__init__()

        self._scene = QGraphicsScene()
        self.setScene(self._scene)

        # Used to add space between nodes
        self._graph_scale = 300

        # Map node name to Node object {str=>Node}
        self._nodes_map = {}

        self._graph = DiGraph()
        self._graph.add_edges_from(
            [
                ("1", "2"),
                ("2", "3"),
                ("3", "4"),
                ("1", "5"),
                ("1", "6"),
                ("1", "7"),
            ]
        )

        self._load_graph()
        self.randomize_position()

    def _load_graph(self):
        self.scene().clear()
        self._nodes_map.clear()

        # Add nodes
        for node in self._graph:
            print(node)
            item = Node(node)
            self.scene().addItem(item)
            self._nodes_map[node] = item

        # Add edges
        # for a, b in self._graph.edges:
        #     source = self._nodes_map[a]
        #     dest = self._nodes_map[b]
        #     self.scene().addItem(Edge(source, dest))

    def randomize_position(self):
        positions = random_layout(self._graph)

        for node, pos in positions.items():
            x, y = pos
            x *= self._graph_scale
            y *= self._graph_scale
            self._nodes_map[node].setPos(x, y)
