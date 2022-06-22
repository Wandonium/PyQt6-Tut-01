# import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
    QPushButton, QDateEdit, QLineEdit, QTextEdit, QComboBox,
    QFormLayout, QHBoxLayout)
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QRegularExpressionValidator

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("Appointment Form")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("First")
        self.first_name_edit.textEdited.connect(self.clearText)

        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Last")
        self.last_name_edit.textEdited.connect(self.clearText)

        # Create horizontal layout for names
        name_h_box = QHBoxLayout()
        name_h_box.addWidget(self.first_name_edit)
        name_h_box.addWidget(self.last_name_edit)

        # Create additional widgets to be added in the window
        gender_combo = QComboBox()
        gender_combo.addItems(["Male", "Female"])

        self.phone_edit = QLineEdit()
        self.phone_edit.setInputMask("(999) 999-9999;_")
        self.phone_edit.textEdited.connect(self.clearText)

        self.birthdate_edit = QDateEdit()
        self.birthdate_edit.setDisplayFormat("MM/dd/yyyy")
        self.birthdate_edit.setMaximumDate(QDate.currentDate())
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setDate(QDate.currentDate())

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("<username>@<domain>.com")
        reg_opt = QRegularExpression()
        regex = QRegularExpression(
            "\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            reg_opt.PatternOption.CaseInsensitiveOption
        )
        self.email_edit.setValidator(QRegularExpressionValidator(regex))
        self.email_edit.textEdited.connect(self.clearText)

        extra_info_tedit = QTextEdit()

        self.feedback_label = QLabel()
        submit_button = QPushButton("SUBMIT")
        submit_button.setMaximumWidth(140)
        submit_button.clicked.connect(self.checkFormInformation)

        # Create horizontal layout for last row of widgets
        submit_h_box = QHBoxLayout()
        submit_h_box.addWidget(self.feedback_label)
        submit_h_box.addWidget(submit_button)


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())