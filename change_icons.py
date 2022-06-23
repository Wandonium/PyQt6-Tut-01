# import necessary modules
import sys, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Changing Icons Example")
        self.setWindowIcon(QIcon("images/pyqt_logo.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        info_label = QLabel("Click on the button and select a fruit.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images = [
            "images/1_apple.png",
            "images/2_pineapple.png",
            "images/3_watermelon.png",
            "images/4_banana.png"
        ]
        self.icon_button = QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

    def changeButtonIcon(self):
        """When the button is clicked, change the icon to a different
        random icon from the image list."""
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())