import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import os

root = tk.Tk()

dir = './test/images/'  # r'D:\projects\Crimson\dabur\datasets\new_dabur_all_data\\'
# r'D:\projects\Crimson\dabur\datasets\new_dabur_all_data\rhimesh_1.txt'
label_file_name = './test/labels.txt'
# r'D:\projects\Crimson\dabur\datasets\new_dabur_all_data\rhimesh_1.txt'
updated_file_name = './test/labels_new.txt'
file = open(label_file_name, 'r')

seperator = ' \t'
lines = file.readlines()
new_lines = []
current_line_index = 0

# text from entry
string_from_detected = tk.StringVar()


def click_save():
    global current_line_index
    global lines
    global string_from_detected
    text_get = string_from_detected.get()
    # 'word_1.jpg,"*MRP Rs. 375/-"\n'
    lines[current_line_index] = lines[current_line_index].split(seperator)[
        0] + seperator + text_get
    with open(updated_file_name, 'w') as file:
        file.writelines(lines)
    return text_get


def next():
    global current_line_index

    click_save()

    current_line_index += 1
    image = ImageTk.PhotoImage(Image.open(
        dir + lines[current_line_index].split(seperator)[0]))
    img.configure(image=image)
    img.image = image  # keep a reference!

    panel2 = tk.Entry(root, fg="black", bg="white", width=40, font=(
        "Arial", 20, "bold"), textvariable=string_from_detected)
    panel2.delete(0, tk.END)
    panel2.insert(0, lines[current_line_index].split(seperator)[1])


def previous():
    global current_line_index

    click_save()

    current_line_index -= 1
    image = ImageTk.PhotoImage(Image.open(
        dir + lines[current_line_index].split(seperator)[0]))
    img.configure(image=image)
    img.image = image  # keep a reference!

    panel2 = tk.Entry(root, fg="black", bg="white", width=40, font=(
        "Arial", 20, "bold"), textvariable=string_from_detected)
    panel2.delete(0, tk.END)
    panel2.insert(0, lines[current_line_index].split(seperator)[1])


# main frame
root.geometry("400x300")

detect_image, detect_string = lines[0].split(seperator)

# for title
title_of_application = tk.Label(
    root, text="GUI for OCR Application", fg="red", activebackground="red")
title_of_application.pack()

# for image
image_load = Image.open(dir + detect_image)
test = ImageTk.PhotoImage(image_load)

img = tk.Label(image=test)
img.image = test
img.pack(pady=20)

# Text Detected
text_label = tk.Label(root, text="Text Detected From Image")
text_label.pack()
text_read = tk.Entry(root, fg="black", bg="white", width=40, font=(
    "Arial", 20, "bold"), textvariable=string_from_detected)
text_read.delete(0, tk.END)
text_read.insert(0, detect_string)
text_read.pack(pady=20)

# buttons
btn1 = tk.Button(root, text="Save", fg="red",
                 activebackground="red", command=click_save)
btn1.place(x=50, y=220)
btn2 = tk.Button(root, text="Next", fg="brown",
                 activebackground="brown", command=next)
btn2.place(x=350, y=220)
prev = tk.Button(root, text="previous", fg="brown",
                 activebackground="brown", command=previous)
prev.place(x=280, y=220)

root.mainloop()
