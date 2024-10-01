import customtkinter
from tkinter import messagebox
#test




class PDFMerge:
    def __init__(self, app):
        self.app = app

    def pdfmerge_function(self):
        title = customtkinter.CTkLabel(self.app, text="Insert your PDF files", font=("arial", 20))
        title.pack(padx=20, pady=20)
        entry = customtkinter.CTkEntry(self.app, width=400, placeholder_text="YouTube Link hier einfügen")
        entry.pack(padx=20, pady=20)