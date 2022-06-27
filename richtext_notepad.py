# import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
        QTextEdit, QFileDialog, QInputDialog, QFontDialog, QColorDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QTextCursor, QColor, QAction

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(400, 500)
        self.setWindowTitle("5.1 - Rich Text Notepad GUI")

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
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
    window = MainWindow()
    sys.exit(app.exec())