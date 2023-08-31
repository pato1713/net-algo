import sys, random
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QApplication,
)
from networkx_widget.view import View
from actions_sidebar.sidebar import ActionsSidebar
from networkx import binomial_graph, spring_layout
from alghoritms.dijkstra import Dijkstra


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self._generate_random_graph()

        self.dijkstra = Dijkstra()
        self.dijkstra.set_edges(
            [
                (edge[0], edge[1], edge[2]["weight"])
                for edge in self.graph.edges(data=True)
            ]
        )

        self.view = View(self.graph)
        self.sidebar = ActionsSidebar()

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.view)
        main_layout.addLayout(self.sidebar)

        self.sidebar.randomize_bttn.clicked.connect(self.reload_graph)
        self.sidebar.calculate_path_bttn.clicked.connect(self.calculate_path_fnc)

    def _generate_random_graph(self):
        self.graph = binomial_graph(10, 0.15, directed=True)
        for u, v, w in self.graph.edges(data=True):
            w["weight"] = round(random.random(), 2)

    def calculate_path_fnc(self):
        first_node = list(self.graph)[0]

        last_node = list(self.graph)[9]
        path = self.dijkstra.calculate_shortest_path(first_node, last_node)

        for index, node in enumerate(path):
            self.view._nodes_map[node].mark_as_chosen()
            print(path)
            if index < len(path) - 1:
                self.view._edges_map[str(node) + str(path[index + 1])].mark_as_chosen()

    def reload_graph(self):
        self._generate_random_graph()
        self.view._load_graph()
        positions = spring_layout(
            self.graph, weight="weight", scale=self.view._graph_scale
        )

        for node, pos in positions.items():
            x, y = pos
            self.view._nodes_map[node].setPos(x, y)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWidget()
    widget.resize(800, 600)
    widget.show()
    widget.setWindowTitle("NetAlgo")

    sys.exit(app.exec())
