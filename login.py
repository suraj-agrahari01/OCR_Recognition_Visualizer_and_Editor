from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout,
                             QFileDialog, QHBoxLayout, QMessageBox, QLineEdit, QMenuBar, QAction, QInputDialog, QShortcut, QDialog, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QPixmap, QImage, QTransform, QKeySequence
from PyQt5.QtCore import Qt


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Easy OCR Login')
        self.setGeometry(100, 100, 900, 500)

        layout = QVBoxLayout()

        # Logo
        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(
            QPixmap('main_logo.png').scaled(200, 200, Qt.KeepAspectRatio))
        self.logo_label.setAlignment(Qt.AlignCenter)

        # Company Introduction
        # self.intro_label = QLabel("Crimson Tech is a Nepal-originated multinational tech company that specializes in computer vision, AI, and ML. Our mission is to transform ideas into reality by designing & building reliable, efficient enterprise and industrial software that solves complex and competitive real-world problems, adhering to state-of-the-art AI methods for automation and quality inspection of fast-moving consumer products.", self)
        self.intro_label = QLabel(
            "Weclome to Easy OCR recoginition System \n"
            "Designed and devloped by Crimson Tech\n",
            self
        )
        self.intro_label.setAlignment(Qt.AlignCenter)
        self.intro_label.setWordWrap(True)
        self.intro_label.setStyleSheet("font-size: 30px;")

        # Instructions
        self.instructions_label = QLabel(
            "Please enter your username and password to log in.\n\nIf you have forgotten your password, please contact Crimson Tech at 98xxxxxxx or email crimson@io for assistance.", self)
        self.instructions_label.setAlignment(Qt.AlignCenter)
        self.instructions_label.setWordWrap(True)
        self.instructions_label.setStyleSheet("font-size: 20px;")

        # Form layout for username and password
        form_layout = QFormLayout()
        form_layout.setContentsMargins(250, 0, 300, 0)
        self.username_input = QLineEdit(self)
        self.username_input.setFixedHeight(25)
        self.password_input = QLineEdit(self)
        self.password_input.setFixedHeight(25)
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow('Username:', self.username_input)
        form_layout.addRow('Password:', self.password_input)

        # Login button
        self.login_button = QPushButton('Login', self)
        self.login_button.setFixedSize(100, 30)  # Smaller size
        self.login_button.clicked.connect(self.check_credentials)

        # Add widgets to layout
        layout.addWidget(self.logo_label)
        layout.addWidget(self.intro_label)
        layout.addWidget(self.instructions_label)
        layout.addLayout(form_layout)
        # layout.addWidget(self.login_button)
        # Centering the button below form layout
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        # Add a spacer to push the elements to the top
        layout.addItem(QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == 'admin' and password == 'password':
            QMessageBox.information(
                self, 'Login Successful', f'Welcome, {username}!')
            self.accept()

        elif username == '' and password == '':
            QMessageBox.warning(
                self, 'Error', 'Please enter username and password')

        elif username == 'admin' and password != 'password':
            QMessageBox.warning(self, 'Error', 'Invalid password')

        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password')
