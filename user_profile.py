# import necessary modules
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(50, 50, 250, 450)
        self.setWindowTitle("User Profile GUI")

        self.setUpMainWindow()
        self.show()

    def craeteImageLabels(self):
        """Open image files and create image labels."""
        images = ["images/skyblue.png", "images/profile_image.png"]
        for img in images:
            try:
                with open(img):
                    label = QLabel(self)
                    pixmap = QPixmap(img)
                    label.setPixmap(pixmap)
                    if img == "images/profile_image.png":
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        """Create the labels to be displayed in the window."""
        self.craeteImageLabels()

        user_label = QLabel(self)
        user_label.setText("John Doe")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText("Biography")
        bio_label.setFont(QFont('Arial', 17))
        bio_label.move(15, 175)

        about_label = QLabel(self)
        about_label.setText("I'm a Software Engineer with 10\nyears experience in creating\nawesome code.")
        about_label.setWordWrap(True)
        about_label.move(15, 200)

        skills_label = QLabel(self)
        skills_label.setText("Skills")
        skills_label.setFont(QFont('Arial', 17))
        skills_label.move(15, 260)

        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 285)

        experience_label = QLabel(self)
        experience_label.setText("Experience")
        experience_label.setFont(QFont('Arial', 17))
        experience_label.move(15, 310)

        developer_label = QLabel(self)
        developer_label.setText('Python Developer')
        developer_label.setFont(QFont("Arial", 13))
        developer_label.move(15, 335)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Mar 2011 - Present")
        dev_dates_label.setFont(QFont('Arial', 10))
        dev_dates_label.move(15, 355)

        driver_label = QLabel(self)
        driver_label.setText('Pizza Delivery Driver')
        driver_label.setFont(QFont('Arial', 13))
        driver_label.move(15, 375)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Aug 2015 - Dec 2017")
        driver_dates_label.setFont(QFont('Arial', 10))
        driver_dates_label.move(15, 395)


# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())