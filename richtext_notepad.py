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
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.removeHighlights)
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.new_act = QAction(QIcon("images/new_file.png"), "New")
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.triggered.connect(self.clearText)

        self.open_act = QAction(QIcon("images/open_file.png"), "Open")
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.triggered.connect(self.openFile)

        self.save_act = QAction(QIcon("images/save_file.png"), "Save")
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.triggered.connect(self.saveToFile)

        self.quit_act = QAction(QIcon("images/exit.png"), "Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        # Create actions for Edit menu
        self.undo_act = QAction(QIcon("images/undo.png"), "Undo")
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.triggered.connect(self.text_edit.undo)

        self.redo_act = QAction(QIcon("images/redo.png"), "Redo")
        self.redo_act.setShortcut("Ctrl+Shift+Z")
        self.redo_act.triggered.connect(self.text_edit.redo)

        self.cut_act = QAction(QIcon("images/cut.png"), "Cut")
        self.cut_act.setShortcut("Ctrl+X")
        self.cut_act.triggered.connect(self.text_edit.cut)

        self.copy_act = QAction(QIcon("images/copy.png"), "Copy")
        self.copy_act.setShortcut("Ctrl+C")
        self.copy_act.triggered.connect(self.text_edit.copy)

        self.paste_act = QAction(QIcon("images/paste.png"), "Paste")
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.triggered.connect(self.text_edit.paste)

        self.find_act = QAction(QIcon("images/find.png"), "Find All")
        self.find_act.setShortcut("Ctrl+F")
        self.find_act.triggered.connect(self.searchText)

        # Create actions for Tools menu
        self.font_act = QAction(QIcon("images/font.png"), "Font")
        self.font_act.setShortcut("Ctrl+T")
        self.font_act.triggered.connect(self.chooseFont)

        self.color_act = QAction(QIcon("images/color.png"), "Color")
        self.color_act.setShortcut("Ctrl+Shift+C")
        self.color_act.triggered.connect(self.chooseFontColor)

        self.highlight_act = QAction(QIcon("images/highlight.png"), "Highlight")
        self.highlight_act.setShortcut("Ctrl+Shift+H")
        self.highlight_act.triggered.connect(self.chooseFontBackgroundColor)

        # Create actions for Help menu
        self.about_act = QAction("About")
        self.about_act.triggered.connect(self.aboutDialog)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.new_act)
        file_menu.addSeparator()
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_act)

        # Create Edit menu and add actions
        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.undo_act)
        edit_menu.addAction(self.redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_act)
        edit_menu.addAction(self.copy_act)
        edit_menu.addAction(self.paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_act)

        #Create Tools menu and add actions
        tool_menu = self.menuBar().addMenu("Tools")
        tool_menu.addAction(self.font_act)
        tool_menu.addAction(self.color_act)
        tool_menu.addAction(self.highlight_act)

        # Create Help menu and add actions
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction(self.about_act)

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())