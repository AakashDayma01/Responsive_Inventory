from tkinter import *
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import tkinter.font as tkFont

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.state('zoomed')
        self.root.minsize(1000, 600)
        self.root.overrideredirect(True)        
        self.root.configure(bg="#f5f6fa")

        # ====== GRID CONFIG ======
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # ================= NAVBAR =================
        navbar = Frame(self.root, bg="#222", height=60)
        navbar.grid(row=0, column=0, columnspan=3, sticky="ew")
        navbar.grid_propagate(False)

        btn_config = [
            ("Home", self.root.destroy),
            ("Employee", self.employee2),
            ("Categories", self.category),
            ("Billing", self.Bill_Area),
            ("Product", self.product),
            ("Suplyre", self.suplyre),
        ]

        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=10)

        # ================= HEADING =================
        heading = Label(self.root, text="Customer Bill Reports", fg="#2c3e50", bg="#ecf0f1",
                        font=("Goudy Old Style", 24, "bold"), pady=10)
        heading.grid(row=1, column=0, columnspan=3, sticky="ew")

        # ================= SEARCH =================
        search_frame = Frame(self.root, bg="#dfe6e9", pady=10, padx=15, relief=RIDGE, bd=2)
        search_frame.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

        Label(search_frame, text="Invoice No.:", font=("Times New Roman", 18, "bold"), bg="#dfe6e9").pack(side=LEFT)
        self.Name_Entry = Entry(search_frame, font=("Arial", 15), bd=2, bg="white", relief=SOLID)
        self.Name_Entry.pack(side=LEFT, padx=5, ipadx=50, ipady=5)

        Button(search_frame, text="Search", command=self.search, bg="#3498db", fg="white",
               font=("Times New Roman", 15, "bold"), relief=FLAT, cursor="hand2").pack(side=LEFT, padx=10)
        Button(search_frame, text="Clear", command=self.show, bg="#e67e22", fg="white",
               font=("Times New Roman", 15, "bold"), relief=FLAT, cursor="hand2").pack(side=LEFT)

        # ================= LEFT LIST =================
        self.Listframe = Frame(self.root, bg="#ffffff", bd=3, relief=GROOVE)
        self.Listframe.grid(row=3, column=0, sticky="ns", padx=10, pady=10)

        Label(self.Listframe, text="Available Bills", bg="#1abc9c", fg="white",
              font=("Arial", 16, "bold"), pady=5).pack(fill="x")

        self.scrolly = Scrollbar(self.Listframe, orient=VERTICAL)
        self.listbox = Listbox(self.Listframe, bg="#ecf0f1", font=("Goudy Old Style", 15),
                               yscrollcommand=self.scrolly.set, selectbackground="#16a085", relief=FLAT)
        self.scrolly.pack(fill=Y, side=RIGHT)
        self.scrolly.config(command=self.listbox.yview)
        self.listbox.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.listbox.bind("<ButtonRelease-1>", self.get_data)

        # ================= BILL AREA =================
        self.Billframe = Frame(self.root, bd=2, bg="white")
        self.Billframe.grid(row=3, column=1, sticky="nsew", padx=20, pady=10)

        Label(self.Billframe, text="Bill Area", bg="#34495e", fg="white",
              font=("Goudy Old Style", 18, "bold")).pack(fill="x")

        bill_scrollbar = Scrollbar(self.Billframe, orient=VERTICAL)
        self.bill_font = tkFont.Font(family="Goudy Old Style", size=15, weight="bold")
        self.billtextarea = Text(self.Billframe, bg="lightyellow", font=self.bill_font, wrap="word",
                                 state=DISABLED, bd=2, fg="black", yscrollcommand=bill_scrollbar.set)
        bill_scrollbar.pack(fill=Y, side=RIGHT)
        bill_scrollbar.config(command=self.billtextarea.yview)
        self.billtextarea.pack(fill=BOTH, expand=1)

        self.Billframe.bind("<Configure>", self.adjust_font_size)

        # ================= IMAGE =================
        img_frame = Frame(self.root, bg="white", bd=2)
        img_frame.grid(row=3, column=2, sticky="ns", padx=10, pady=10)

        if os.path.exists("pics/p1.jpg"):
            self.bill_photo = Image.open("pics/p1.jpg").resize((400, 400), Image.LANCZOS)
            self.bill_photo = ImageTk.PhotoImage(self.bill_photo, master=self.root)
            Label(img_frame, image=self.bill_photo, bg="white").pack(fill=BOTH, expand=1)

        self.show()

    # ================= FUNCTIONS =================
    def placeholder_action(self):
        messagebox.showinfo("Info", "This button is not yet connected.")

    def adjust_font_size(self, event):
        new_size = max(10, int(event.height / 30))
        self.bill_font.configure(size=new_size)

    def show(self):
        self.listbox.delete(0, END)
        if os.path.exists('Bills'):
            for i in os.listdir('Bills'):
                if i.endswith(".txt"):
                    self.listbox.insert(END, i)

    def search(self):
        invoice_no = self.Name_Entry.get().strip()
        self.listbox.delete(0, END)
        if os.path.exists('Bills'):
            for i in os.listdir('Bills'):
                if i.startswith(invoice_no) and i.endswith(".txt"):
                    self.listbox.insert(END, i)

    def get_data(self, ev):
        self.billtextarea.config(state=NORMAL)
        try:
            a = self.listbox.curselection()
            file_name = self.listbox.get(a)
            with open(f'Bills/{file_name}', 'r') as f:
                self.billtextarea.delete("1.0", END)
                self.billtextarea.insert(END, f.read())
        except:
            pass
        self.billtextarea.config(state=DISABLED)

    def employee2(self):
        from Employee import page2
        new_root = Tk()
        self.new_obj = page2(new_root)
        self.root.destroy()

    
    def category(self):
        from Category import Categorie
        new_root = Tk()
        self.new_obj = Categorie(new_root)
        self.root.destroy()
        
    def suplyre(self):
        from suplyre import SupplyreClass
        new_root = Tk()
        self.new_obj = SupplyreClass(new_root)
        self.root.destroy()
        
    def product(self):
        from product import product
        new_root = Tk()
        self.new_obj = product(new_root)
        self.root.destroy()

    def Bill_Area(self):
        new_root = Tk()
        from Main_billsection import Billing_area
        self.new_obj = Billing_area(new_root)
        self.root.destroy()
    


if __name__ == "__main__":
    root = Tk()
    Sales(root)
    root.mainloop()
