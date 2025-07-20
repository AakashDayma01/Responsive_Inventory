from tkinter import *
from tkinter import ttk
import Functions  # Assuming this is still necessary
import time
class product:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1366x768")
        self.root.configure(bg="#f0f0f0")
        self.root.state('zoomed')
        self.root.minsize(1000, 600)
        self.root.overrideredirect(True)
        self.page_window = None
        self.page1_window = None
        self.page2_window = None
        self.page3_window = None
        self.page4_window = None
        self.page5_window = None
        self.page6_window = None

        # Functions Class
        self.f = Functions.function()
        self.page_window = None

        # Layout Components
        self.create_navbar()
        self.create_product_frame()
        self.create_search_frame()
        self.create_table_frame()
        self.fetch_cat_supplier_data()

    def create_navbar(self):
        navbar = Frame(self.root, bg="#222", height=60)
        navbar.pack(fill=X)

        btn_config = [
            ("Home", None),
            ("Employee", self.employee2),
            ("Categories", self.category),
            ("Billing", self.Bill_Area),
            ("Product", self.product),
            ("Sales", self.Sales),
            ("Back", None)
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=10)

    def create_search_frame(self):
        # Adjusting the search frame layout
        frame = LabelFrame(self.root, text="Search", font=("Arial", 14, "bold"), bg="white", fg="black", bd=2, relief=RIDGE)
        frame.place(relx=0.40, rely=0.12, relwidth=0.57, relheight=0.15)

        Label(frame, text="Search By:", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        
        # Creating a responsive combobox for search options
        self.search_cmb = ttk.Combobox(frame, values=["Select", "Supplier", "Category", "Name"], state="readonly", font=("Arial", 12))
        self.search_cmb.current(0)
        self.search_cmb.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Creating an entry field for search input
        self.search_entry = Entry(frame, font=("Arial", 12), bg="lightyellow")
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky="ew")
        
        # Making the search button responsive too
        Button(frame, text="Search", bg="#0078D7", fg="white", font=("Arial", 12, "bold"),
               cursor="hand2", command=self.product_search).grid(row=0, column=3, padx=10, pady=5, sticky="ew")

        # Configuring the search frame columns to adjust to widget sizes
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=2)  # Make the search entry wider

    def create_product_frame(self):
        frame = LabelFrame(self.root, text="Product Details", font=("Arial", 14, "bold"), bg="white", fg="black", bd=2, relief=RIDGE)
        frame.place(relx=0.02, rely=0.12, relwidth=0.35, relheight=0.85)

        self.category_entry = ttk.Combobox(frame, values=["Select"], state="readonly", font=("Arial", 12))
        self.supplier_entry = ttk.Combobox(frame, state="readonly", values=['Select'], font=("Arial", 12))
        self.supplier_entry.current(0)
        self.category_entry.current(0)

        self.name_entry = Entry(frame, font=("Arial", 12), bg="lightyellow")
        self.price_entry = Entry(frame, font=("Arial", 12), bg="lightyellow")
        self.quantity_entry = Entry(frame, font=("Arial", 12), bg="lightyellow")

        # Status Combobox with predefined values
        self.status_entry = ttk.Combobox(frame, state="readonly", font=("Arial", 12))
        self.status_entry['values'] = ("Active", "Inactive")
        self.status_entry.current(0)

        fields = [("Category", self.category_entry),
                  ("Supplier", self.supplier_entry),
                  ("Name", self.name_entry),
                  ("Price", self.price_entry),
                  ("QTY", self.quantity_entry),
                  ("Status", self.status_entry)]

        for idx, (field, entry) in enumerate(fields):
            Label(frame, text=field, font=("Arial", 12, "bold"), bg="white").grid(row=idx, column=0, padx=10, pady=10, sticky="w")
            entry.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")

        frame.grid_columnconfigure(1, weight=1)

        btn_frame = Frame(frame, bg="white")
        btn_frame.grid(row=6, column=0, columnspan=2, pady=15, sticky="ew")
        btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        button_configurations = [("Save", "#28a745", self.product_add),
                                 ("Update", "#17a2b8", self.product_update),
                                 ("Delete", "#dc3545", self.product_delete),
                                 ("Clear", "#ffc107", self.product_clear)]

        for i, (text, color, command) in enumerate(button_configurations):
            Button(btn_frame, text=text, bg=color, fg="white", font=("Arial", 12, "bold"),
                   cursor="hand2", bd=2, command=command).grid(row=0, column=i, padx=(10, 5), pady=5, sticky="ew")
            
    def create_table_frame(self):
        frame = LabelFrame(self.root, text="Product List", font=("Arial", 14, "bold"), bg="white", fg="black", bd=2, relief=RIDGE)
        frame.place(relx=0.40, rely=0.30, relwidth=0.57, relheight=0.67)

        self.product_table = ttk.Treeview(frame, columns=("pid", "supplier", "category", "name", "price", "qty", "status"), show="headings")
        self.product_table.bind("<ButtonRelease-1>", self.product_get_data)
        self.Product_show()

        headers = ["Product ID", "Supplier", "Category", "Name", "Price", "Quantity", "Status"]
        for col, header in zip(self.product_table['columns'], headers):
            self.product_table.heading(col, text=header)
            self.product_table.column(col, anchor=CENTER)

        scrolly = Scrollbar(frame, orient=VERTICAL, command=self.product_table.yview)
        scrollx = Scrollbar(frame, orient=HORIZONTAL, command=self.product_table.xview)
        self.product_table.configure(yscroll=scrolly.set, xscroll=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.product_table.pack(fill=BOTH, expand=True)

    def product_add(self):
        self.f.product_add((self.root, self.name_entry, self.category_entry, self.supplier_entry, self.price_entry, self.quantity_entry, self.status_entry, self.product_table))

    def Product_show(self):
        self.f.Product_show(self.product_table)
    
    def Close(self):
        if self.page_window is not None:
            self.page_window.destroy()

    def product_get_data(self, event=None):
        self.f.Product_get_data((self.root, self.name_entry, self.category_entry, self.supplier_entry, self.price_entry, self.quantity_entry, self.status_entry, self.product_table))

    def product_clear(self):
        self.f.product_clear((self.root, self.name_entry, self.category_entry, self.supplier_entry, self.price_entry, self.quantity_entry, self.status_entry, self.product_table))

    def product_update(self):
        self.f.product_update((self.root, self.name_entry, self.category_entry, self.supplier_entry, self.price_entry, self.quantity_entry, self.status_entry, self.product_table))

    def product_delete(self):
        self.f.product_delete((self.root, self.name_entry, self.category_entry, self.supplier_entry, self.price_entry, self.quantity_entry, self.status_entry, self.product_table))

    def fetch_cat_supplier_data(self, event=None):
        self.f.fetch_cat_supplier_data((self.root, self.supplier_entry, self.category_entry))

    def product_search(self):
        self.f.product_search((self.root, self.search_entry, self.search_cmb, self.product_table))

    def navigate_back(self):
        self.root.destroy() 

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

if __name__ == "__main__":
    root = Tk()
    app = product(root)
    root.mainloop()