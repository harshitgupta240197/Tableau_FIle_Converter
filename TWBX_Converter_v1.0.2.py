import customtkinter as ctk
from customtkinter import filedialog, CTk
import os
import zipfile
from PIL import Image, ImageTk

class CustomTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TWBX File Converter")
        self.root.geometry("700x250")  # Adjusted window size

        # Apply dark theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Load the image
        logo_image = Image.open('C:/Users/HarshitGupta/Downloads/CM Duplicator/healthicity-red-primary.png')  
        logo_image = logo_image.resize((270, 70))
        self.logo_image = ImageTk.PhotoImage(logo_image)

        self.create_widgets()

    def create_widgets(self):
        frame = ctk.CTkFrame(self.root)
        frame.grid(row=0, column=0, sticky=(ctk.W, ctk.E, ctk.N, ctk.S))

        # Logo Label
        logo_label = ctk.CTkLabel(frame, image=self.logo_image, text='')
        logo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=(20, 10), sticky=ctk.W)

        # Select Files Button
        ctk.CTkLabel(frame, text="Select TWBX Files:").grid(row=1, column=0, sticky=ctk.W, pady=(10, 5))
        self.select_files_entry = ctk.CTkEntry(frame, width=50)
        self.select_files_entry.grid(row=1, column=1, padx=(0, 5), pady=(10, 5), sticky=ctk.W)
        self.select_files_btn = ctk.CTkButton(frame, text="Browse", command=self.select_files)
        self.select_files_btn.grid(row=1, column=2, padx=(0, 10), pady=(10, 5), sticky=ctk.W)

        # Select Destination Button
        ctk.CTkLabel(frame, text="Select Destination Folder:").grid(row=2, column=0, sticky=ctk.W, pady=(10, 5))
        self.select_dest_entry = ctk.CTkEntry(frame, width=50)
        self.select_dest_entry.grid(row=2, column=1, padx=(0, 5), pady=(10, 5), sticky=ctk.W)
        self.select_dest_btn = ctk.CTkButton(frame, text="Browse", command=self.select_destination_folder)
        self.select_dest_btn.grid(row=2, column=2, padx=(0, 10), pady=(10, 5), sticky=ctk.W)

        # Convert Button
        self.convert_btn = ctk.CTkButton(frame, text="Convert", command=self.convert)
        self.convert_btn.grid(row=3, column=0, columnspan=3, pady=(10, 20), sticky=ctk.W)

        # Adjust column weights
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)
        frame.columnconfigure(2, weight=1)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select TWBX Files",
            filetypes=[("TWBX files", "*.twbx")]
        )
        if file_paths:
            self.select_files_entry.delete(0, ctk.END)
            self.select_files_entry.insert(0, ', '.join(file_paths))

    def select_destination_folder(self):
        folder_path = filedialog.askdirectory(title="Select Destination Folder")
        if folder_path:
            self.select_dest_entry.delete(0, ctk.END)
            self.select_dest_entry.insert(0, folder_path)

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
        file_paths = self.select_files_entry.get().split(', ')
        destination_folder = self.select_dest_entry.get()
        if file_paths and destination_folder:
            for file_path in file_paths:
                self.unpack_twbx(file_path, destination_folder)
            print("Files unpackaged successfully!")
        else:
            print("Please select TWBX files and destination folder.")

    def convert(self):
        self.process_files()

def main():
    root = ctk.CTk()
    app = CustomTkinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
