from typing import Optional
from PySide6.QtGui import QPainter, QColor, QPen, QBrush, QPolygonF, QPainterPath
from PySide6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget
from PySide6.QtCore import QRectF, Qt, QLineF, QPointF
from networkx_widget.node import Node
from config.config import EDGE_Z_VALUE
import math


class Edge(QGraphicsItem):
    def __init__(
        self,
        source: Node,
        dest: Node,
        weight: float,
        parent: QGraphicsItem | None = None,
    ) -> None:
        super().__init__(parent)
        self._weight = weight
        self._color = "#2BB53C"
        self._line = QLineF()
        self._source = source
        self._dest = dest
        self._tickness = 5
        self._source.add_edge(self)
        self._dest.add_edge(self)
        self.setZValue(EDGE_Z_VALUE)
        self.changePos()
        self._arrow_size = 20

    def changePos(self):
        self.prepareGeometryChange()
        self._line = QLineF(
            self._source.pos() + self._source.boundingRect().center(),
            self._dest.pos() + self._dest.boundingRect().center(),
        )

    def boundingRect(self) -> QRectF:
        return (
            QRectF(self._line.p1(), self._line.p2())
            .normalized()
            .adjusted(
                -self._tickness - self._arrow_size,
                -self._tickness - self._arrow_size,
                self._tickness + self._arrow_size,
                self._tickness + self._arrow_size,
            )
        )

    def _draw_arrow(self, painter: QPainter, start: QPointF, end: QPointF):
        painter.pen().setBrush(QBrush(self._color))
        line = QLineF(start, end)
        angle = -math.atan2(-line.dy(), -line.dx())

        arrow_head = QPolygonF()
        arrow_head.clear()
        arrow_head.append(line.p2())
        arrow_head.append(
            line.p2()
            + QPointF(
                math.sin(angle + math.pi / 3) * self._arrow_size,
                math.cos(angle + math.pi / 3) * self._arrow_size,
            )
        )

        arrow_head.append(
            line.p2()
            + QPointF(
                math.sin(angle + math.pi - math.pi / 3) * self._arrow_size,
                math.cos(angle + math.pi - math.pi / 3) * self._arrow_size,
            )
        )

        painter.drawPolygon(arrow_head)

        path = QPainterPath()
        path.addPolygon(arrow_head)
        painter.fillPath(path, QBrush(self._color))

    def _arrow_target(self):
        length = self._line.length() - self._dest._radius
        x_factor = self._line.dx() * length / self._line.length()
        y_factor = self._line.dy() * length / self._line.length()

        return QPointF(self._line.p1().x() + x_factor, self._line.p1().y() + y_factor)

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionGraphicsItem,
        widget: QWidget | None = None,
    ) -> None:
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(
            QPen(
                QColor(self._color),
                self._tickness,
                Qt.SolidLine,
                Qt.RoundCap,
                Qt.RoundJoin,
            )
        )
        painter.drawLine(self._line)

        self._draw_arrow(painter, self._line.p1(), self._arrow_target())
        painter.setPen(
            QPen(
                QColor("#fff"),
                self._tickness,
                Qt.SolidLine,
                Qt.RoundCap,
                Qt.RoundJoin,
            )
        )
        painter.drawText(self.boundingRect(), Qt.AlignCenter, str(self._weight))
