import tkinter as tk
from tkinter import filedialog
import json

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def load_video(self):
        video_path = filedialog.askopenfilename()
        return video_path

    def save_output(self, output_data):
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        with open(output_file, 'w') as f:
            json.dump(output_data, f)

    def run(self):
        self.root.mainloop()

# Usage example:
gui = GUI()
video_path = gui.load_video()
output_data = {"example": "data"}
gui.save_output(output_data)
gui.run()
