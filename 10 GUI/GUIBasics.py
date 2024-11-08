import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Main Page")
root.geometry("300x200")


# Function to go to the second page
def open_second_page():
    # Create a new window for the second page
    second_page = tk.Toplevel(root)
    second_page.title("Second Page")
    second_page.geometry("300x200")

    # Function to run when each button on the second page is clicked
    def on_second_button_click(number):
        print(f"Second Page Button {number} clicked!")

    # Create three buttons on the second page
    button4 = tk.Button(second_page, text="Button 4", command=lambda: on_second_button_click(4))
    button5 = tk.Button(second_page, text="Button 5", command=lambda: on_second_button_click(5))
    button6 = tk.Button(second_page, text="Button 6", command=lambda: on_second_button_click(6))

    # Place the buttons on the second page
    button4.pack(pady=10)
    button5.pack(pady=10)
    button6.pack(pady=10)


# Function to run when each button on the main page is clicked
def on_main_button_click(number):
    print(f"Main Page Button {number} clicked!")
    open_second_page()


# Create three buttons on the main page
button1 = tk.Button(root, text="Button 1", command=lambda: on_main_button_click(1))
button2 = tk.Button(root, text="Button 2", command=lambda: on_main_button_click(2))
button3 = tk.Button(root, text="Button 3", command=lambda: on_main_button_click(3))

# Place the buttons on the main page
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Run the application
root.mainloop()
