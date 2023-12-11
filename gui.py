import tkinter as tk
from tkinter import filedialog
import os
from .config import *

__all__ = [
    "file_path"
]

root = tk.Tk()
root.withdraw()  # Hide the main window

file_path = filedialog.askopenfilename(
    title="Select a File",
    filetypes=[("Excel files (.xls)", "*.xls"), ("All files", "*.*")],
)

assert os.path.isfile(file_path), f"File not found: {file_path}"
logging.info("The selected file is %s", file_path)