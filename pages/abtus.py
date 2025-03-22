from PyQt5 import QtWidgets, QtGui, QtCore

class AbtusPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        # Add Label
        self.label = QtWidgets.QLabel("About our Hospital Page")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.layout.addWidget(self.label)

        # Add a colored Button
        self.button = QtWidgets.QPushButton("Click Me!")
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.layout.addWidget(self.button)

        # Add another widget (Example: TextEdit)
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setPlaceholderText("Write something about the hospital...")
        self.layout.addWidget(self.text_edit)
