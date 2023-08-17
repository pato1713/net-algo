import sys
from PySide6.QtWidgets import (
    QComboBox,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QApplication,
    QPushButton,
)
from networkx_widget.view import View


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.view = View()

        v_layout = QHBoxLayout(self)
        v_layout.addWidget(self.view)

        sidebar = QVBoxLayout()
        v_layout.addLayout(sidebar)

        randomize_bttn = QPushButton(
            text="Reload",
        )
        randomize_bttn.clicked.connect(self.view.randomize_position)
        sidebar.addWidget(randomize_bttn)
        sidebar.addWidget(QPushButton(text="test2"))
        sidebar.addWidget(QPushButton(text="test3"))
        sidebar.addWidget(QPushButton(text="test4"))


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    widget.setWindowTitle("NetAlgo")

    sys.exit(app.exec())
