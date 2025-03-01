import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)

        self.pushButton = QPushButton('добавить круг', self)
        self.pushButton.setGeometry(10, 10, 200, 40)
        self.pushButton.clicked.connect(self.add_circle)

        self.scene = QGraphicsScene(self)
        self.graphicsView = QGraphicsView(self.scene, self)
        self.graphicsView.setGeometry(0, 60, 800, 540)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, 700)
        y = random.randint(0, 500)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QBrush(color))
        self.scene.addItem(circle)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CircleWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
