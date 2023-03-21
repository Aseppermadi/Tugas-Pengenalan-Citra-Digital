#import libary yang akan digunakan
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter


class MinMaxFilterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Min Max Filter App")
        self.master.geometry("600x400")

        self.image = None
        self.filtered_image = None

        self.create_widgets()

    def create_widgets(self):
        # membuat menu bar.
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Image", command=self.open_image)
        filemenu.add_command(label="Save Filtered Image", command=self.save_filtered_image)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

        # membuat kanvas untuk menampilkan gambar.
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack(side=tk.LEFT)

        # disini membuat tombol untuk filter dan memasukan gambar.
        self.min_button = tk.Button(self.master, text="Min Filter", command=self.min_filter)
        self.min_button.pack(side=tk.TOP, pady=10)

        self.max_button = tk.Button(self.master, text="Max Filter", command=self.max_filter)
        self.max_button.pack(side=tk.TOP, pady=10)
        
        self.open_button = tk.Button(self.master, text="Open Image", command=self.open_image)
        self.open_button.pack(side=tk.TOP, pady=10)

    def open_image(self):
        # membuka file untuk memilih gambar.
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        if file_path:
            # memuat gambar dan di tampilkan.
            self.image = Image.open(file_path)
            self.image = self.image.resize((400, 400), Image.ANTIALIAS)
            self.filtered_image = self.image.copy()
            self.display_image(self.image)

    def save_filtered_image(self):
        # buka untuk memilih di penyimpanan apa dan nama filenya.
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg")])

        if file_path:
            # menyimpan foto yang telah di filter.
            self.filtered_image.save(file_path)

    def display_image(self, image):
        # memunculkan gambar di kanvas.
        self.photo_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

    def min_filter(self):
        if self.image:
            # menerapkan filter min pada gambar.
            self.filtered_image = self.image.filter(ImageFilter.MinFilter())
            self.display_image(self.filtered_image)

    def max_filter(self):
        if self.image:
            # menerapkan filter max pada gambar.
            self.filtered_image = self.image.filter(ImageFilter.MaxFilter())
            self.display_image(self.filtered_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = MinMaxFilterApp(root)
    root.mainloop()
    