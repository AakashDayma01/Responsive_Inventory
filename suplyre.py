from tkinter import *
from tkinter import ttk
import time
import Functions
class SupplyreClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System - Supplier Management")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f0f0f0")
        self.root.state("zoomed")

        # Functions Instance
        self.f = Functions.function()

        # Navbar Section
        self.create_navbar()

        # Space between navbar and header
        Frame(self.root, bg="#f0f0f0", height=10).pack(fill=X)

        # Header Frame
        header_frame = Frame(self.root, bg="black")
        header_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)

        lbl_title = Label(header_frame, text="Supplier Details", font=("times new roman", 25, "bold"), fg="white", bg="black")
        lbl_title.pack(side=LEFT, padx=20)

        # Search Section
        search_frame = Frame(self.root, bg="#f0f0f0")
        search_frame.place(relx=0.58, rely=0.22, relwidth=0.4, relheight=0.08)

        lbl_search = Label(search_frame, text="Invoice no:", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_search.pack(side=LEFT, padx=10)

        self.Search_Entry = ttk.Entry(search_frame, font=("arial", 15), background="#fffacd")  # Yellowish field
        self.Search_Entry.pack(side=LEFT, fill=X, expand=True, padx=10)

        btn_Search = Button(search_frame, text="Search", command=self.Sup_Search, bg="green", fg="white",
                            font=("times new roman", 15, "bold"), cursor="hand2")
        btn_Search.pack(side=LEFT, padx=10)

        # Left Form Section
        form_frame = Frame(self.root, bg="#f0f0f0", bd=2, relief=SOLID)
        form_frame.place(relx=0.02, rely=0.3, relwidth=0.55, relheight=0.65)

        lbl_invoice = Label(form_frame, text="Invoice No.", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_invoice.place(relx=0.02, rely=0.02, relwidth=0.3, relheight=0.08)

        self.Sup_Entry = ttk.Entry(form_frame, font=("arial", 13), background="#fffacd")
        self.Sup_Entry.place(relx=0.35, rely=0.02, relwidth=0.6, relheight=0.08)

        lbl_name = Label(form_frame, text="Name", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_name.place(relx=0.02, rely=0.14, relwidth=0.3, relheight=0.08)

        self.name_Entry = ttk.Entry(form_frame, font=("arial", 13), background="#fffacd")
        self.name_Entry.place(relx=0.35, rely=0.14, relwidth=0.6, relheight=0.08)

        lbl_contact = Label(form_frame, text="Contact", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_contact.place(relx=0.02, rely=0.26, relwidth=0.3, relheight=0.08)

        self.Contact_Entry = ttk.Entry(form_frame, font=("arial", 13), background="#fffacd")
        self.Contact_Entry.place(relx=0.35, rely=0.26, relwidth=0.6, relheight=0.08)

        lbl_desc = Label(form_frame, text="Description", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_desc.place(relx=0.02, rely=0.38, relwidth=0.3, relheight=0.15)

        self.DEsc_Entry = Text(form_frame, font=("arial", 13), height=5, width=30, bg="#fffacd")
        self.DEsc_Entry.place(relx=0.35, rely=0.38, relwidth=0.6, relheight=0.2)

        # Button Section
        btn_frame = Frame(form_frame, bg="#f0f0f0")
        btn_frame.place(relx=0.02, rely=0.65, relwidth=0.95, relheight=0.2)

        btn_add = Button(btn_frame, text="Save", command=self.Sup_Add, bg="blue", fg="white", font=("times new roman", 15, "bold"), cursor="hand2")
        btn_add.pack(side=LEFT, padx=10, expand=True)

        btn_update = Button(btn_frame, text="Update", command=self.Sup_Update, bg="green", fg="white", font=("times new roman", 15, "bold"), cursor="hand2")
        btn_update.pack(side=LEFT, padx=10, expand=True)

        btn_delete = Button(btn_frame, text="Delete", command=self.Sup_Delete, bg="red", fg="white", font=("times new roman", 15, "bold"), cursor="hand2")
        btn_delete.pack(side=LEFT, padx=10, expand=True)

        btn_clear = Button(btn_frame, text="Clear", command=self.Sup_Clear, bg="pink", fg="black", font=("times new roman", 15, "bold"), cursor="hand2")
        btn_clear.pack(side=LEFT, padx=10, expand=True)

        # Table Section
        table_frame = Frame(self.root, bg="#f0f0f0", bd=2, relief=SOLID)
        table_frame.place(relx=0.58, rely=0.3, relwidth=0.4, relheight=0.55)

        self.scrolly = Scrollbar(table_frame, orient=VERTICAL)
        self.scrollx = Scrollbar(table_frame, orient=HORIZONTAL)

        self.Supplier_Table = ttk.Treeview(table_frame, columns=("Invoice", "name", "contact", "description"),
                                           yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)

        self.scrollx.config(command=self.Supplier_Table.xview)
        self.scrolly.config(command=self.Supplier_Table.yview)

        self.Supplier_Table.heading("Invoice", text="Invoice No.")
        self.Supplier_Table.heading("name", text="Name")
        self.Supplier_Table.heading("contact", text="Contact")
        self.Supplier_Table.heading("description", text="Description")
        self.Supplier_Table["show"] = "headings"

        self.Supplier_Table.column("Invoice", width=100)
        self.Supplier_Table.column("name", width=150)
        self.Supplier_Table.column("contact", width=150)
        self.Supplier_Table.column("description", width=200)
        self.Supplier_Table.pack(fill=BOTH, expand=True)

        self.Supplier_Table.bind("<ButtonRelease-1>", self.Sup_Get_data)

        # Display Initial Data
        self.Sup_show(self.Supplier_Table)
        self.Sup_generateInvoice()

    def create_navbar(self):
        navbar = Frame(self.root, bg="#222", height=60)
        navbar.pack(fill=X)

        btn_config = [
            ("Home", self.Back),
            ("Employee", self.employee2),
            ("Categories", self.category),
            ("Billing", self.Bill_Area),
            ("Product", self.product),
            ("Sales", self.Sales),
            ("Back", self.root.destroy)
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=10)

    # CRUD Operations
    def Sup_Add(self):
        mytuple = (self.root, self.Sup_Entry, self.name_Entry, self.Contact_Entry, self.DEsc_Entry, self.Supplier_Table, self.Search_Entry)
        self.f.Suplier_add(mytuple)

    def Sup_show(self, Supplier_Table):
        mytuple = (self.root,)
        self.f.Suplier_show(self.Supplier_Table, mytuple[0])

    def Sup_Get_data(self, event=None):
        mytuple = (self.root, self.Sup_Entry, self.name_Entry, self.Contact_Entry, self.DEsc_Entry, self.Supplier_Table, self.Search_Entry)
        self.f.Suplier_get_data(mytuple)

    def Sup_Update(self):
        mytuple = (self.root, self.Sup_Entry, self.name_Entry, self.Contact_Entry, self.DEsc_Entry, self.Supplier_Table, self.Search_Entry)
        self.f.Suplier_Update(mytuple)

    def Sup_Clear(self):
        mytuple = (self.root, self.Sup_Entry, self.name_Entry, self.Contact_Entry, self.DEsc_Entry, self.Supplier_Table, self.Search_Entry)
        self.f.Suplier_Clears(mytuple)

    def Sup_Delete(self):
        mytuple = (self.root, self.Sup_Entry, self.name_Entry, self.Contact_Entry, self.DEsc_Entry, self.Supplier_Table, self.Search_Entry)
        self.f.Suplier_Delete(mytuple)

    def Sup_generateInvoice(self):
        self.f.Suplir_generateInvoice(self.Sup_Entry)

    def Sup_Search(self):
        mytuple = (self.root, self.Supplier_Table, self.Search_Entry)
        self.f.suplier_search(mytuple)

    def employee2(self):
        self.root.destroy()
        from Employee import page2
        new_root = Tk()
        self.new_obj = page2(new_root)

    
    def category(self):
        self.root.destroy()
        from Category import Categorie
        new_root = Tk()
        self.new_obj = Categorie(new_root)
        
    def Sales(self):
        self.root.destroy()
        from Sales import Sales
        new_root = Tk()
        self.new_obj = Sales(new_root)
        
    def product(self):
        self.root.destroy()
        from product import product
        new_root = Tk()
        self.new_obj = product(new_root)

    def Bill_Area(self):
        self.root.destroy()
        new_root = Tk()
        from Main_billsection import Billing_area
        self.new_obj = Billing_area(new_root)
    
    def Back(self):
        self.root.destroy()
        


if __name__ == "__main__":
    root = Tk()
    obj = SupplyreClass(root)
    root.mainloop()

