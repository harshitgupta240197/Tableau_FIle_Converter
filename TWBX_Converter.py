import tkinter as tk
from tkinter import filedialog, ttk
import os
import zipfile

class TWBXConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TWBX File Converter")

        self.file_paths = []
        self.destination_folder = ""

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Select Files Button
        ttk.Label(frame, text="Select TWBX Files:").grid(row=0, column=0, sticky=tk.W)
        self.select_files_btn = ttk.Button(frame, text="Browse", command=self.select_files)
        self.select_files_btn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Select Destination Button
        ttk.Label(frame, text="Select Destination Folder:").grid(row=1, column=0, sticky=tk.W)
        self.select_dest_btn = ttk.Button(frame, text="Browse", command=self.select_destination_folder)
        self.select_dest_btn.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Convert Button
        self.convert_btn = ttk.Button(frame, text="Convert", command=self.convert)
        self.convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select TWBX Files",
            filetypes=[("TWBX files", "*.twbx")]
        )
        if file_paths:
            self.file_paths = file_paths
            print("Selected TWBX Files:", self.file_paths)

    def select_destination_folder(self):
        folder_path = filedialog.askdirectory(title="Select Destination Folder")
        if folder_path:
            self.destination_folder = folder_path
            print("Destination Folder:", self.destination_folder)

    def unpack_twbx(self, file_path, destination_folder):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
        # Renaming the extracted folder to TWB format
        base_filename = os.path.basename(file_path)
        extracted_folder = os.path.join(destination_folder, os.path.splitext(base_filename)[0] + "_extracted")
        # Ensure the extracted folder exists before renaming
        if os.path.exists(extracted_folder):
            os.rename(extracted_folder, os.path.join(destination_folder, os.path.splitext(base_filename)[0] + "_extracted"))
        else:
            print(f"Extracted folder not found for {file_path}")

    def process_files(self):
        if self.file_paths and self.destination_folder:
            for file_path in self.file_paths:
                self.unpack_twbx(file_path, self.destination_folder)
            print("Files unpackaged successfully!")
        else:
            print("Please select TWBX files and destination folder.")

    def convert(self):
        self.process_files()

def main():
    root = tk.Tk()
    app = TWBXConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
