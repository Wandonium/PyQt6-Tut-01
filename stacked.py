# import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox,
    QStackedLayout, QFormLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(300, 340)
        self.setWindowTitle("QStackedLayout Example")

        self.setUpMainWindow()
        self.show()

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())