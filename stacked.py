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

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        # Create and connect the combo box to switch pages
        page_combo = QComboBox()
        page_combo.addItems(["Image", "Description", "Additional Info"])
        page_combo.activated.connect(self.switchPage)

        # Create the Image page (Page 1)
        profile_image = QLabel()
        pixmap = QPixmap("images/norwegian.jpg")
        profile_image.setPixmap(pixmap)
        profile_image.setScaledContents(True)

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())