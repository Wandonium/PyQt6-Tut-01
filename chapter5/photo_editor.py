# import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton,
                             QDockWidget, QDialog, QFileDialog, QMessageBox, QToolBar,
                             QStatusBar, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import (QIcon, QAction, QPixmap, QTransform, QPainter)
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setFixedSize(650, 650)
        self.setWindowTitle("5.2 - Photo Editor GUI")

        self.setUpMainWindow()
        self.createToolsDockWidget()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        pass

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        """Create the application's menu bar."""
        # self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, True)
    window = MainWindow()
    sys.exit(app.exec())