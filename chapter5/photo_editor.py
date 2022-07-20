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
        self.image = QPixmap()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)

        # Create the status bar
        self.setStatusBar(QStatusBar())

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.open_act = QAction(QIcon("images/open_file.png"), "Open")
        self.open_act.setShortcut(("Ctrl+O"))
        self.open_act.setStatusTip("Open a new image")
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon("images/save_file.png"), "Save")
        self.save_act.setShortcut(("Ctrl+S"))
        self.save_act.setStatusTip("Save image")
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon("images/print.png"), "Print")
        self.print_act.setShortcut(("Ctrl+P"))
        self.print_act.setStatusTip("Print image")
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        self.quit_act = QAction(QIcon("images/exit.png"), "Quit")
        self.quit_act.setShortcut(("Ctrl+Q"))
        self.quit_act.setStatusTip("Quit Program")
        self.quit_act.triggered.connect(self.close)

        # Create actions for Edit menu
        self.rotate90_act = QAction("Rotate 90°")
        self.rotate90_act.setStatusTip("Rotate image 90° clockwise")
        self.rotate90_act.triggered.connect(self.rotateImage90)

        self.rotate180_act = QAction("Rotate 180°")
        self.rotate180_act.setStatusTip("Rotate image 180° clockwise")
        self.rotate180_act.triggered.connect(self.rotateImage180)

        self.flip_hor_act = QAction("Flip Horizontal")
        self.flip_hor_act.setStatusTip("Flip image across horizontal axis")
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_act = QAction("Flip Vertical")
        self.flip_ver_act.setStatusTip("Flip image across vertical axis")
        self.flip_ver_act.triggered.connect(self.flipImageVertical)

        self.resize_act = QAction("Resize Half")
        self.resize_act.setStatusTip("Resize image to half the original size")
        self.resize_act.triggered.connect(self.resizeImageHalf)

        self.clear_act = QAction(QIcon("images/clear.png"), "Clear Image")
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the current image")
        self.clear_act.triggered.connect(self.clearImage)

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