import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QBrush, QColor


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)

        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, 500)
        y = random.randint(0, 500)

        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QBrush(QColor(255, 255, 0)))
        self.scene.addItem(circle)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CircleWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
