from tkinter import *
from tkinter import ttk
import Functions

class Categorie:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#F4F6F7")
        self.root.state("zoomed")
        self.root.state('zoomed')
        self.root.minsize(1000, 600)
        self.root.overrideredirect(True)
        self.f = Functions.function()

        # Variables
        self.Cat_var = StringVar()
        self.name_var = StringVar()

        # Grid Config
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)

        # ================= Navbar (Top) =================
        navbar = Frame(self.root, bg="#222", height=55)
        navbar.grid(row=0, column=0, columnspan=3, sticky="ew")
        navbar.grid_propagate(False)

        btn_config = [
            ("Home", self.root.destroy),
            ("Employee", self.employee2),
            ("Suplier",self.suplyre),
            ("Product", self.product),
            ("Billing", self.Bill_Area),
            ("Sales", self.Sales),
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"), bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=8)

        # ================= Main Heading (Below Navbar) =================
        self.title_frame = Label(self.root, text="📦 Manage Product Categories",font=("Segoe UI", 26, "bold"), bg="#1ABC9C", fg="white",pady=10)
        self.title_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=0, pady=(0, 10))

        # ================= Entry & Buttons Frame =================
        entry_frame = Frame(self.root, bg="#F4F6F7")
        entry_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        entry_frame.columnconfigure(1, weight=1)

        Label(entry_frame, text="Enter Category Name", font=("Segoe UI", 14, "bold"), bg="#F4F6F7").grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.Name_Entry = Entry(entry_frame, textvariable=self.name_var, font=("Segoe UI", 13), bg="white", relief=GROOVE, bd=2)
        self.Name_Entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5, ipady=3)

        btn_frame = Frame(entry_frame, bg="#F4F6F7")
        btn_frame.grid(row=0, column=2, padx=10)

        Button(btn_frame, text="💾 Save", command=self.Cat_add,bg="#27AE60", fg="white", font=("Segoe UI", 12, "bold"),cursor="hand2", relief=FLAT).grid(row=0, column=0, padx=5, pady=2, ipadx=10)

        Button(btn_frame, text="🗑 Delete", command=self.Cat_delete, bg="#E74C3C", fg="white", font=("Segoe UI", 12, "bold"), cursor="hand2", relief=FLAT).grid(row=0, column=1, padx=5, pady=2, ipadx=10)

        # ================= Category Table Frame =================
        self.cat_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        self.cat_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

        self.scrolly = Scrollbar(self.cat_frame, orient=VERTICAL)
        self.scrollx = Scrollbar(self.cat_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview( self.cat_frame, columns=("Cid", "name"), yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrollx.config(command=self.category_table.xview)
        self.scrolly.config(command=self.category_table.yview)

        self.category_table.heading("Cid", text="Category ID")
        self.category_table.heading("name", text="Name")
        self.category_table["show"] = "headings"
        self.category_table.column("Cid", width=100, anchor="center")
        self.category_table.column("name", width=200, anchor="center")
        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease-1>", self.Cat_Get_data)

        self.cat_show()

        # ================= Images Section =================
        self.load_images()

    def load_images(self):
        from PIL import Image, ImageTk
        img1 = Image.open("pics/p2.jpg").resize((630, 330), Image.LANCZOS)
        self.bill_photo1 = ImageTk.PhotoImage(img1, master=self.root)   # 👈 attach to root
        img2 = Image.open("pics/p3.webp").resize((630, 330), Image.LANCZOS)
        self.bill_photo2 = ImageTk.PhotoImage(img2, master=self.root)

        img_frame = Frame(self.root, bg="#F4F6F7")
        img_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        lbl1 = Label(img_frame, image=self.bill_photo1, bg="white", bd=1, relief=SOLID)
        lbl1.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

        lbl2 = Label(img_frame, image=self.bill_photo2, bg="white", bd=1, relief=SOLID)
        lbl2.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    def Cat_add(self):
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.Categories_add(Cattuple)

    def cat_show(self):
        Cattuple = (self.root,)
        self.f.Categories_show(self.category_table, Cattuple[0])

    def Cat_Get_data(self, event=None):
        region = self.category_table.identify_region(event.x, event.y)
        row_id = self.category_table.identify_row(event.y)
        if region != "cell" or not row_id:
            return
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.Categories_get_data(Cattuple)

    def Cat_delete(self):
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.category_delete(Cattuple)
    
    def employee2(self):
        from Employee import page2
        new_root = Tk()
        self.new_obj = page2(new_root)
        self.root.destroy()

    def suplyre(self):
        from suplyre import SupplyreClass
        new_root = Tk()
        self.new_obj = SupplyreClass(new_root)
        self.root.destroy()
        
    def Sales(self):
        from Sales import Sales
        new_root = Tk()
        self.new_obj = Sales(new_root)
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
    obj = Categorie(root)
    root.mainloop()
