from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("path/to/icon.png"))  # Update with actual icon path
        self.initUI()

    def initUI(self):
        # Initialize the user interface components here
        self.setCentralWidget(None)  # Set a central widget or layout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())