from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import messagebox
import customtkinter
from Files.pdfmerge import PDFMerge

#git test

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("960x540")
app.title("PDF Tool")

pdfmerge_instance = PDFMerge(app)

def reset_gui():
    for widget in app.winfo_children():
        widget.destroy()
    initialize_gui()

    reset_button = customtkinter.CTkButton(app, text="Hauptmenü", command=reset_gui)
    reset_button.place(x=50, y=50)



def pdfmerge_import():
    pdfmerge_instance.pdfmerge_function()
    button.destroy()

def initialize_gui():
    global button
    button = customtkinter.CTkButton(app, text="PDF Merge ", command=pdfmerge_import(), height=100,
        width=200,)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

if __name__ == '__main__':
    initialize_gui()
app.mainloop()