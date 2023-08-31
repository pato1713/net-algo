from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from networkx_widget.node import Node
from networkx import DiGraph
from networkx_widget.edge import Edge


class View(QGraphicsView):
    def __init__(self, graph: DiGraph):
        super().__init__()

        self._graph = graph
        self._scene = QGraphicsScene()
        self.setScene(self._scene)

        # Used to add space between nodes
        self._graph_scale = 400

        # Map node name to Node object {str=>Node}
        self._nodes_map = {}
        self._edges_map = {}
        self._load_graph()

    def _load_graph(self):
        self.scene().clear()
        self._nodes_map.clear()

        # Add nodes
        for node in self._graph:
            item = Node("Node-" + str(node + 1))
            self.scene().addItem(item)
            self._nodes_map[node] = item

        # Add edges
        for a, b, data in self._graph.edges.data():
            source = self._nodes_map[a]
            dest = self._nodes_map[b]
            edge = Edge(source, dest, data["weight"])
            self._edges_map[str(a) + str(b)] = edge
            self.scene().addItem(edge)
