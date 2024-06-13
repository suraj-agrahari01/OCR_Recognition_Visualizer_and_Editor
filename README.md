# Easy OCR Recognition System

This project is an Easy OCR Recognition System designed and developed by Crimson Tech. The system includes a login window for authentication and an image annotation viewer for reviewing and annotating images.

## Features

### Login Authentication:

-   Users are required to log in with a username and password.
-   Default credentials: Username: `admin`, Password: `password`.

### Image Annotation Viewer:

-   Load and display images from a specified directory.
-   Annotate images with text labels.
-   Navigate through images using "Next" and "Previous" buttons.
-   Save individual image labels or all labels at once.
-   Zoom in and out of images.
-   Rotate images 90 degrees clockwise.
-   Reset zoom and rotation transformations.
-   Delete images.
-   Jump to a specific image by index or filename.
-   Toggle between light and dark mode themes.

## Installation

### Clone the Repository:

```bash
git https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor.git
cd OCR_Recognition_Visualizer_and_Editor
```

Ensure you have PyQt5 and PIL installed.

### Run the Application:

```bash
python main.py

```

## Usage

### Login:

-   Run the application.
-   Enter the username and password in the login window.
-   Click "Login".

### Image Annotation Viewer:

-   Click "Select Main Input Directory" to choose the main directory containing the images folder and labels.txt file.
-   Navigate through images using "Next" and "Previous" buttons.
-   Annotate images using the text entry field and save labels.
-   Use zoom, rotate, and reset functionalities to adjust image display.
-   Delete images if necessary.
-   Use the "Jump to Image" button to quickly navigate to a specific image.
-   Toggle dark mode using the menu bar option.
-   Save changes before exiting the application.

## Project Structure

```bash
easy-ocr-recognition/
│
├── login_easy_ocr.py     # Main application code GUI
├── easy_recotation.py     #script
├── main_logo.png         # Logo image used in the login window
├── README.md             # This README file
└── main_logo.png         #logo

```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Developed by Suraj Agrahari.
Special thanks to the contributors and the open-source community.
