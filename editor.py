import tkinter as tk
from tkinter import scrolledtext, filedialog

"""
Tkinter is a built-in Python library for creating user interfaces. It provides a set of tools
and widgets to design and implement graphical applications, offering simplicity and versatility for desktop applications.
"""

current_file = None       #variable for the file currently opened

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        with open(file_path, "r") as file:
            text = file.read()
            text_editor.delete("1.0", tk.END)
            text_editor.insert("1.0", text)

    """
        open_file(): This function is called when the "Open" button is clicked. It uses the filedialog module to open a file dialog, allowing
        the user to select a text file. If a file is selected, it reads the contents of the file and displays them in the text editor
    """

def save_file():
    global current_file
    if current_file:
        text = text_editor.get("1.0", tk.END)
        with open(current_file, "w") as file:
            file.write(text)
    else:
        save_file_as()

    """
        save_file():This function is called when the "Save" button is clicked. It checks if there is a currently opened file (current_file).
        If there is, it retrieves the text from the text editor and saves it to the current file. If no file is currently open, it calls the save_file_as() function.
    """

def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file = file_path
        save_file()


    """
        save_file_as(): This function is called when the "Save As" button is clicked or if there is no current file. It opens a file dialog for
        the user to choose the location and name of the file to save. It then saves the text from the text editor to the selected file.
    """

def clear_text():
    text_editor.delete("1.0", tk.END)

    """
        clear_text(): This function is called when the "Clear" button is clicked. It clears all the text in the text editor (text_editor) by deleting its contents.
    """

# main window
window = tk.Tk()
window.title("Text Editor")

# toolbar frame
toolbar = tk.Frame(window)
toolbar.pack(side=tk.TOP, fill=tk.X)

# toolbar buttons
open_button = tk.Button(toolbar, text="Open", command=open_file)
save_button = tk.Button(toolbar, text="Save", command=save_file)
save_as_button = tk.Button(toolbar, text="Save As", command=save_file_as)
clear_button = tk.Button(toolbar, text="Clear", command=clear_text)

open_button.pack(side=tk.LEFT)
save_button.pack(side=tk.LEFT)
save_as_button.pack(side=tk.LEFT)
clear_button.pack(side=tk.LEFT)

# editor widget with vertical scrollbars
text_editor = scrolledtext.ScrolledText(window, wrap=tk.WORD)
text_editor.pack(expand=True, fill='both')

# Start the Tkinter event loop
window.mainloop()
