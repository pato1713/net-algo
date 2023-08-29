from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from networkx_widget.node import Node
from networkx import DiGraph, spring_layout
from networkx_widget.edge import Edge


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
        self._graph.add_weighted_edges_from(
            [
                ("1", "2", 0.2),
                ("2", "3", 0.9),
                ("3", "4", 0.1),
                ("1", "5", 0.15),
                ("1", "6", 0.3),
                ("1", "7", 0.4),
            ]
        )

        self._load_graph()
        self.randomize_position()

    def _load_graph(self):
        self.scene().clear()
        self._nodes_map.clear()

        # Add nodes
        for node in self._graph:
            item = Node(node)
            self.scene().addItem(item)
            self._nodes_map[node] = item

        # Add edges
        for a, b, data in self._graph.edges.data():
            source = self._nodes_map[a]
            dest = self._nodes_map[b]
            self.scene().addItem(Edge(source, dest, data["weight"]))

    def randomize_position(self):
        positions = spring_layout(self._graph)

        for node, pos in positions.items():
            x, y = pos
            x *= self._graph_scale
            y *= self._graph_scale
            self._nodes_map[node].setPos(x, y)
