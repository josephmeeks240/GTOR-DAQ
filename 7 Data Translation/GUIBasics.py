import tkinter as tk
from tkinter import filedialog
import os

os.cd("../")
from DataDownloader import DataDownloader

# Create the main window
root = tk.Tk()
root.title("Main Page")
root.geometry("400x200")


# Function to go to the second page
def open_second_page():
    # Create a new window for the second page
    second_page = tk.Toplevel(root)
    second_page.title("Second Page")
    second_page.geometry("400x200")

    # Function to handle file upload
    def upload_file():
        # Open file dialog and get the file path
        file_path = filedialog.askopenfilename()
        # Display the file path in the label
        file_upload_label.config(text=f"Selected file: {file_path}")

    # Function to run when each button on the second page is clicked
    def on_second_button_click(number):
        print(f"Second Page Button {number} clicked!")

    # File upload section
    file_upload_button = tk.Button(second_page, text="Upload File", command=upload_file)
    file_upload_button.pack(pady=10)

    file_upload_label = tk.Label(second_page, text="No file selected")
    file_upload_label.pack(pady=5)

    # Create a frame for the buttons on the second page
    second_frame = tk.Frame(second_page)
    second_frame.pack(pady=20)

    # Create and place the buttons in a single row on the second page
    button4 = tk.Button(second_frame, text="Button 4", command=lambda: on_second_button_click(4))
    button5 = tk.Button(second_frame, text="Button 5", command=lambda: on_second_button_click(5))
    button6 = tk.Button(second_frame, text="Button 6", command=lambda: on_second_button_click(6))

    button4.grid(row=0, column=0, padx=20)
    button5.grid(row=0, column=1, padx=20)
    button6.grid(row=0, column=2, padx=20)


# Function to run when each button on the main page is clicked
def on_main_button_click(number):
    print(f"Main Page Button {number} clicked!")
    open_second_page()


# Create labels and buttons on the main page in a single row
frame = tk.Frame(root)
frame.pack(pady=20)

# Create label and button for Button 1
label1 = tk.Label(frame, text="Label 1")
label1.grid(row=0, column=0, padx=20)
button1 = tk.Button(frame, text="Button 1", command=lambda: on_main_button_click(1))
button1.grid(row=1, column=0, padx=20)

# Create label and button for Button 2
label2 = tk.Label(frame, text="Label 2")
label2.grid(row=0, column=1, padx=20)
button2 = tk.Button(frame, text="Button 2", command=lambda: on_main_button_click(2))
button2.grid(row=1, column=1, padx=20)

# Create label and button for Button 3
label3 = tk.Label(frame, text="Label 3")
label3.grid(row=0, column=2, padx=20)
button3 = tk.Button(frame, text="Button 3", command=lambda: on_main_button_click(3))
button3.grid(row=1, column=2, padx=20)

# Run the application
root.mainloop()
