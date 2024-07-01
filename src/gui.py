# Module for the GUI
import tkinter as tk
from tkinter import filedialog

def load_video():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename()
    return video_path

def save_output(output_data):
    root = tk.Tk()
    root.withdraw()
    output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    with open(output_file, 'w') as f:
        json.dump(output_data, f)
