# Easy OCR Recognition System

This project is an Easy OCR Recognition System designed and developed by Crimson Tech. The system includes a login window for authentication and an image annotation viewer for reviewing and annotating images.

## System OverView

| ![image](https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor/assets/138669672/5f0b91ff-0495-4b3f-a3aa-ddde60dac9d9) |
| :---------------------------------------------------------------------------------------------------------------------------------------: |
|                                                            _Fig : Login Image_                                                            |

| ![image](https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor/assets/138669672/28008aff-5359-4a19-9cfd-2bf2a04c0a51) |
| :---------------------------------------------------------------------------------------------------------------------------------------: |
|                                                             _Fig : Home Page_                                                             |

| ![image](https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor/assets/138669672/b9b9b147-0b29-48db-bc35-9a2a40409c20) |
| :---------------------------------------------------------------------------------------------------------------------------------------: |
|                                                    _Fig : Imort, zoom-out and zoom-in_                                                    |

| ![image](https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor/assets/138669672/9a0c9043-9fd2-4baa-82c8-162d4a920d9d) |
| :---------------------------------------------------------------------------------------------------------------------------------------: |
|                                                _Fig : Rotation and dark mode intergaretd_                                                 |

| ![image](https://github.com/suraj-agrahari01/OCR_Recognition_Visualizer_and_Editor/assets/138669672/9028673e-525a-41f7-8b7d-be213c9861aa) |
| :---------------------------------------------------------------------------------------------------------------------------------------: |
|                                             _Fig : Jump to page number , save iamge and txt _                                             |

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
python login_easy_ocr.py

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
└── test                  #input folder
    └── images
         └── saved
         └── images.jpg
    └── labels_new.txt
    └── labels.txt


```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Developed by Suraj Agrahari.
Special thanks to the contributors and the open-source community.
