from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("This is a custom widget", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_click(self):
        self.label.setText("Button clicked!")