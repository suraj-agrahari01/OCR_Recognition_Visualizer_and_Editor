import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFormLayout,
                             QFileDialog, QHBoxLayout, QMessageBox, QLineEdit, QMenuBar, QAction, QInputDialog, QShortcut, QDialog, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QPixmap, QImage, QTransform, QKeySequence
from PyQt5.QtCore import Qt
from PIL import Image
from PyQt5.QtGui import QPixmap, QFont

from login import LoginWindow



class ImageAnnotationViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_files = []
        self.labels = []
        self.index = 0
        self.zoom_scale = 1.0
        self.rotation_angle = 0
        self.main_input_dir = ""
        self.image_dir = ""
        self.label_file = ""
        self.updated_label_file = ""
        self.dark_mode = False

    def initUI(self):
        self.setWindowTitle('Easy Recognition Viewer')
        self.setGeometry(100, 100, 800, 400)

        # Create a menu bar
        menubar = self.menuBar()
        home_menu = menubar.addMenu('Home')
        help_menu = menubar.addMenu('Help')

        # Create actions for the menu
        home_action = QAction('Home', self)
        help_action = QAction('Help', self)
        reset_action = QAction('Reset', self)
        dark_mode_action = QAction('Toggle Dark Mode', self)
        home_action.triggered.connect(self.go_home)
        help_action.triggered.connect(self.display_help)
        reset_action.triggered.connect(self.reset_transformations)
        dark_mode_action.triggered.connect(self.toggle_dark_mode)

        # Add actions to the menu
        home_menu.addAction(home_action)
        help_menu.addAction(help_action)
        menubar.addAction(reset_action)
        menubar.addAction(dark_mode_action)

        # Main Layout
        main_layout = QHBoxLayout()

        # Left side layout for buttons and other controls
        left_layout = QVBoxLayout()

        # Image display area
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Current image indicator
        self.current_image_label = QLabel('Current Image: 0 / 0', self)

        # Text entry for image label
        self.text_entry = QLineEdit(self)

        # Image information display
        self.image_info_label = QLabel('', self)

        # Buttons
        self.select_main_input_dir_button = QPushButton(
            'Select Main Input Directory', self)
        self.next_button = QPushButton('Next', self)
        self.prev_button = QPushButton('Previous', self)
        self.save_image_button = QPushButton('Save Image', self)
        self.save_labels_button = QPushButton('Save Labels', self)
        self.zoom_in_button = QPushButton('Zoom In', self)
        self.zoom_out_button = QPushButton('Zoom Out', self)
        self.rotate_button = QPushButton('Rotate', self)
        self.delete_button = QPushButton('Delete Image', self)
        self.jump_button = QPushButton('Jump to Image', self)
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.setStyleSheet(
            'QPushButton {background-color: red; color: white;}')

        # Connect buttons to their functions
        self.select_main_input_dir_button.clicked.connect(
            self.select_main_input_directory)
        self.next_button.clicked.connect(self.next_image)
        self.prev_button.clicked.connect(self.prev_image)
        self.save_image_button.clicked.connect(self.save_image)
        self.save_labels_button.clicked.connect(self.save_labels)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.rotate_button.clicked.connect(self.rotate)
        self.delete_button.clicked.connect(self.delete_image)
        self.jump_button.clicked.connect(self.jump_to_image)
        self.exit_button.clicked.connect(self.close_application)

        # Add widgets to left layout
        left_layout.addWidget(self.select_main_input_dir_button)
        left_layout.addWidget(self.prev_button)
        left_layout.addWidget(self.next_button)
        left_layout.addWidget(self.save_image_button)
        left_layout.addWidget(self.save_labels_button)
        left_layout.addWidget(self.zoom_in_button)
        left_layout.addWidget(self.zoom_out_button)
        left_layout.addWidget(self.rotate_button)
        left_layout.addWidget(self.delete_button)
        left_layout.addWidget(self.jump_button)
        left_layout.addWidget(self.exit_button)
        left_layout.addStretch(1)  # Add stretch to push buttons to top

        # Right side layout for image and text
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.current_image_label)
        right_layout.addWidget(self.image_label)
        right_layout.addWidget(self.image_info_label)
        right_layout.addWidget(self.text_entry)

        # Add left and right layouts to main layout
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Keyboard shortcuts
        QShortcut(QKeySequence("Right"), self, self.next_image)
        QShortcut(QKeySequence("Left"), self, self.prev_image)

    def select_main_input_directory(self):
        self.main_input_dir = QFileDialog.getExistingDirectory(
            self, "Select Main Input Directory")
        if self.main_input_dir:
            self.image_dir = os.path.join(self.main_input_dir, 'images')
            self.label_file = os.path.join(self.main_input_dir, 'labels.txt')
            self.updated_label_file = os.path.join(
                self.main_input_dir, 'labels_new.txt')
            if not os.path.exists(self.image_dir):
                QMessageBox.warning(
                    self, "Error", "Images subfolder not found.")
            elif not os.path.exists(self.label_file):
                QMessageBox.warning(self, "Error", "Label file not found.")
            else:
                if not os.path.exists(self.updated_label_file):
                    with open(self.label_file, 'r') as src:
                        with open(self.updated_label_file, 'w') as dst:
                            dst.write(src.read())
                self.load_labels()
                self.load_images()
                QMessageBox.information(
                    self, "Directory Selected", f"Main input directory selected: {self.main_input_dir}")

    def load_labels(self):
        if self.label_file:
            try:
                with open(self.label_file, 'r') as file:
                    self.labels = [line.strip().split('\t')
                                   for line in file.readlines()]
            except FileNotFoundError:
                QMessageBox.warning(self, "Error", "Label file not found.")
                self.labels = []

    def save_labels(self):
        if self.updated_label_file:
            try:
                with open(self.updated_label_file, 'w') as file:
                    for label in self.labels:
                        file.write('\t'.join(label) + '\n')
                QMessageBox.information(
                    self, "Success", "Labels saved successfully.")
            except Exception as e:
                QMessageBox.warning(
                    self, "Error", f"Failed to save labels: {e}")

    def load_images(self):
        if self.image_dir:
            self.image_files = [f for f in os.listdir(
                self.image_dir) if f.endswith('.jpg')]
            if not self.image_files:
                QMessageBox.warning(
                    self, "Error", "No images found in the selected directory.")
            else:
                self.index = 0
                self.update_current_image_label()
                self.display_image()
        else:
            QMessageBox.warning(
                self, "Error", "Please select an image directory.")

    def display_image(self):
        if 0 <= self.index < len(self.image_files):
            image_path = os.path.join(
                self.image_dir, self.image_files[self.index])
            image = Image.open(image_path)
            q_image = QImage(image_path)
            pixmap = QPixmap.fromImage(q_image)

            if self.zoom_scale != 1.0:
                pixmap = pixmap.scaled(int(pixmap.width(
                ) * self.zoom_scale), int(pixmap.height() * self.zoom_scale), Qt.KeepAspectRatio)

            if self.rotation_angle != 0:
                transform = QTransform().rotate(self.rotation_angle)
                pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)

            self.image_label.setPixmap(pixmap)
            self.text_entry.setText(self.labels[self.index][1])
            self.update_current_image_label()

            # Display image information
            self.image_info_label.setText(
                f"Dimensions: {image.width}x{image.height}\nSize: {os.path.getsize(image_path)} bytes")

    def next_image(self):
        if self.index < len(self.image_files) - 1:
            self.labels[self.index][1] = self.text_entry.text()
            self.index += 1
            self.display_image()

    def prev_image(self):
        if self.index > 0:
            self.labels[self.index][1] = self.text_entry.text()
            self.index -= 1
            self.display_image()

    def save_image(self):
        if 0 <= self.index < len(self.image_files):
            self.labels[self.index][1] = self.text_entry.text()
            self.save_labels()
            # Save image to 'saved' subfolder
            saved_dir = os.path.join(self.image_dir, 'saved')
            if not os.path.exists(saved_dir):
                os.makedirs(saved_dir)
            current_image_path = os.path.join(
                self.image_dir, self.image_files[self.index])
            saved_image_path = os.path.join(
                saved_dir, self.image_files[self.index])
            image = Image.open(current_image_path)
            image.save(saved_image_path)
            QMessageBox.information(
                self, "Success", f"Image saved to {saved_image_path}")

    def zoom_in(self):
        self.zoom_scale += 0.1
        self.display_image()

    def zoom_out(self):
        if self.zoom_scale > 0.1:
            self.zoom_scale -= 0.1
        self.display_image()

    def rotate(self):
        self.rotation_angle += 90
        self.display_image()

    def reset_transformations(self):
        self.zoom_scale = 1.0
        self.rotation_angle = 0
        self.display_image()

    def delete_image(self):
        if 0 <= self.index < len(self.image_files):
            reply = QMessageBox.question(self, 'Delete Image',
                                         "Are you sure you want to delete this image?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                image_path = os.path.join(
                    self.image_dir, self.image_files[self.index])
                os.remove(image_path)
                del self.image_files[self.index]
                del self.labels[self.index]
                if self.index >= len(self.image_files):
                    self.index = len(self.image_files) - 1
                self.update_current_image_label()
                self.display_image()

    def jump_to_image(self):
        text, ok = QInputDialog.getText(
            self, 'Jump to Image', 'Enter image index or filename:')
        if ok:
            try:
                index = int(text) - 1
                if 0 <= index < len(self.image_files):
                    self.index = index
                    self.display_image()
                else:
                    QMessageBox.warning(
                        self, "Error", "Invalid index.")
            except ValueError:
                if text in self.image_files:
                    self.index = self.image_files.index(text)
                    self.display_image()
                else:
                    QMessageBox.warning(
                        self, "Error", "Filename not found in image list.")

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.setStyleSheet(
                "QWidget { background-color: #2e2e2e; color: white; }")
        else:
            self.setStyleSheet("")

    def go_home(self):
        QMessageBox.information(self, "Home", "You are already at Home.")

    def display_help(self):
        help_text = (
            "1. Select Main Input Directory: Choose the main directory containing the images folder and label files.\n"
            "2. Next: Display the next image.\n"
            "3. Previous: Display the previous image.\n"
            "4. Save Image: Save the current image label.\n"
            "5. Save Labels: Save all image labels to the updated label file.\n"
            "6. Zoom In: Increase image size.\n"
            "7. Zoom Out: Decrease image size.\n"
            "8. Rotate: Rotate the image 90 degrees clockwise.\n"
            "9. Reset: Reset zoom and rotation to default values.\n"
            "10. Delete Image: Delete the currently displayed image.\n"
            "11. Jump to Image: Jump to a specific image by index or filename.\n"
            "12. Toggle Dark Mode: Switch between light and dark mode themes.\n"
            "13. Exit: Close the application."
        )
        QMessageBox.information(self, "Help", help_text)

    def update_current_image_label(self):
        self.current_image_label.setText(
            f'Current Image: {self.index + 1} / {len(self.image_files)}')

    def close_application(self):
        reply = QMessageBox.question(self, 'Exit',
                                     "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_image()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Show the login window first
    login_window = LoginWindow()
    if login_window.exec_() == QDialog.Accepted:
        viewer = ImageAnnotationViewer()
        viewer.show()
        sys.exit(app.exec_())
