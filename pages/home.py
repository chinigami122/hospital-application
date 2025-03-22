from PyQt5 import QtWidgets, QtGui, QtCore

class HomePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Create a stacked layout
        self.stacked_layout = QtWidgets.QStackedLayout()
        self.main_layout.addLayout(self.stacked_layout)

        # --- First Page: Home content ---
        home_widget = QtWidgets.QWidget()
        home_layout = QtWidgets.QVBoxLayout(home_widget)
        home_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Image
        self.image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(r"C:\Users\nmira\OneDrive\Documents\hosîtal2\nurse.png")  # Update path here
        if not pixmap.isNull():
            # Scale image to fit the entire widget size
            pixmap = pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding)
            self.image.setPixmap(pixmap)
        else:
            self.image.setText("Image not found")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        home_layout.addWidget(self.image)

        # Text
        self.label = QtWidgets.QLabel("Welcome to XYZ Hospital\nProviding Quality Healthcare Services")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        home_layout.addWidget(self.label)

        # Login Button
        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.setFixedWidth(120)
        self.login_button.clicked.connect(self.show_welcome_page)
        home_layout.addWidget(self.login_button, alignment=QtCore.Qt.AlignCenter)

        # Add first page to stacked layout
        self.stacked_layout.addWidget(home_widget)

        # --- Second Page: Welcome nurses ---
        welcome_widget = QtWidgets.QWidget()
        welcome_layout = QtWidgets.QVBoxLayout(welcome_widget)
        welcome_label = QtWidgets.QLabel("Welcome dear nurses!")
        welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        welcome_label.setFont(font)
        welcome_layout.addWidget(welcome_label)
        self.stacked_layout.addWidget(welcome_widget)

    def show_welcome_page(self):
        # Switch to second page
        self.stacked_layout.setCurrentIndex(1)
