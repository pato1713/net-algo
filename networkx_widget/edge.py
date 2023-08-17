from typing import Optional
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsItem, QStyleOptionGraphicsItem, QWidget
from PySide6.QtCore import QRectF


class Edge(QGraphicsItem):
    def __init__(self, parent: QGraphicsItem | None = ...) -> None:
        super().__init__(parent)

    def boundingRect(self) -> QRectF:
        return super().boundingRect()

    def paint(
        self,
        painter: QPainter,
        option: QStyleOptionGraphicsItem,
        widget: QWidget | None = ...,
    ) -> None:
        return super().paint(painter, option, widget)
