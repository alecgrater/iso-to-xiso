# powershell commands
#.\extract-xiso.exe -x '.\filename.iso’
#.\extract-xiso.exe -c '.\filename\'
import tkinter as tk
import shutil
from tkinter import filedialog
import os
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("ISO Converter")

        self.label = tk.Label(master, text="Select an ISO file:")
        self.label.pack()

        self.filepath = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.filepath)
        self.entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.filepath.set(filename)
        #set self.filename to filename without path and extension
        self.filename = os.path.splitext(os.path.basename(filename))[0]

    def convert(self):
        iso_path = self.filepath.get()
        if iso_path.endswith(".iso"):
            folder_path = os.path.splitext(iso_path)[0]
            extract_cmd1 = f'.\\extract-xiso.exe -x "{iso_path}"'
            extract_cmd2 = f'.\\extract-xiso.exe -c "{self.filename}xiso"\\'
            try:
                subprocess.run(extract_cmd1, cwd=os.path.dirname(iso_path), shell=True, check=True)
                os.rename(folder_path, folder_path + "xiso")
                subprocess.run(extract_cmd2, cwd=os.path.dirname(iso_path), shell=True, check=True)
                os.remove(iso_path)
                shutil.rmtree(folder_path + "xiso")
                tk.messagebox.showinfo("Success", "Conversion complete!")
            except subprocess.CalledProcessError as e:
                tk.messagebox.showerror("Error", f"Conversion failed: {e}")
        else:
            tk.messagebox.showerror("Error", "Invalid file format, please select an ISO file.")

root = tk.Tk()
app = App(root)
root.mainloop()
