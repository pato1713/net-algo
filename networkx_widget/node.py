from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget
from PySide6.QtCore import QRectF, Qt
from config.config import NODE_Z_VALUE


class Node(QGraphicsItem):
    def __init__(self, name: str, parent: QGraphicsItem | None = None) -> None:
        super().__init__(parent)
        self._name = name
        self._color = "#5AD469"
        self._radius = 30
        self._rect = QRectF(0, 0, self._radius * 2, self._radius * 2)
        self._edges = []
        self.setZValue(NODE_Z_VALUE)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

    def boundingRect(self) -> QRectF:
        return self._rect

    def mark_as_chosen(self):
        self._color = "#eb4034"
        self.setZValue(NODE_Z_VALUE + 1)
        self.update()

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionGraphicsItem,
        widget: QWidget | None = None,
    ) -> None:
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(
            QPen(
                QColor(self._color).darker(),
                2,
                Qt.SolidLine,
                Qt.RoundCap,
                Qt.RoundJoin,
            )
        )
        painter.setBrush(QBrush(QColor(self._color)))
        painter.drawEllipse(self.boundingRect())
        painter.setPen(QPen(QColor("white")))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self._name)

    def add_edge(self, edge):
        self._edges.append(edge)

    def itemChange(self, change: QGraphicsItem.GraphicsItemChange, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for edge in self._edges:
                edge.changePos()

        return super().itemChange(change, value)
