import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import Functions

class Billing_area:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1200x650")
        self.root.configure(bg="#f0f0f0")
        self.root.state('zoomed')
        self.root.minsize(1000, 600)
        self.root.overrideredirect(True)
        self.f = Functions.function()
        self.root.focus_force()
        self.cart_list = []
        self.pid = StringVar()
        self.file_print = 0

        self.root.grid_rowconfigure(1, weight=1)
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1, uniform='equal')

        self.create_navbar()
        self.create_left_frame()
        self.create_middle_frame()
        self.create_right_frame()
            
    def create_navbar(self):
        navbar = Frame(self.root, bg="#222", height=60)
        navbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
        for i in range(5):
            navbar.grid_columnconfigure(i, weight=1)

        btn_config = [
            ("Home", self.root.destroy),
            ("Employee", self.employee2),
            ("Categories", self.category),
            ("Suppleir", self.supliers),
            ("Product", self.product),
            ("Sales", self.Sales),
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=10)

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.left_frame, text="All Products", font=("times new roman", 30, "bold"),
                          fg="white", bg="#000066")
        header.pack(fill="x")

        search_frame = tk.Frame(self.left_frame,bg="white",borderwidth=2, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=3, pady=10)

        for i in range(3):
            search_frame.grid_columnconfigure(i, weight=1)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 18, "bold"), fg="red", width=35, anchor="w",bg="white" ,padx=2, pady=5).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        tk.Button(search_frame, text="Search All", font=("times new roman", 15, "bold"), width=17, padx=2, pady=2, bg="#d6eaf8", command=self.Billsecton_search_all).grid(row=0, column=2, sticky="e", padx=5, pady=5)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 17), width=16,bg="white" ,anchor="w").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        self.Search_Name_Entry = tk.Entry(search_frame, font=("times new roman", 15), bg="lightyellow")
        self.Search_Name_Entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 15, "bold"), bg="#aed6f1", command=self.Billsection_search).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        product_frame = tk.Frame(self.left_frame)
        product_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"),
                                          show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
            self.product_table.column(col, width=100, anchor="center")

        y_scroll = ttk.Scrollbar(product_frame, orient="vertical", command=self.product_table.yview)
        x_scroll = ttk.Scrollbar(product_frame, orient="horizontal", command=self.product_table.xview)
        self.product_table.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        y_scroll.pack(fill="y", side="right")
        x_scroll.pack(fill="x", side="bottom")
        self.product_table.pack(fill="both", expand=True, side="left")

        self.product_table.bind('<ButtonRelease-1>', self.Billsection_get_data)

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2,borderwidth=2, relief=tk.RIDGE, bg="white")
        self.middle_frame.grid(row=1, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)
        self.Customer_detail = tk.Frame(self.middle_frame,bg="white",borderwidth=2, bd=2, relief=tk.RIDGE)
        self.Customer_detail.pack(fill="x", padx=3, pady=5)

        tk.Label(self.Customer_detail, text="Customer Detail", font=("times new roman", 27, "bold"), bg="#c0c0c0").pack(fill="x")

        top_form = tk.Frame(self.Customer_detail, bg="white")
        top_form.pack(fill="x", padx=10, pady=5)

        for i in range(4):
            top_form.grid_columnconfigure(i, weight=1)

        tk.Label(top_form, text="Name", font=("times new roman", 15), bg="white", width=11).grid(row=0, column=0, sticky="w", padx=1, pady=5)
        self.Custumer_Name_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_Name_E.grid(row=0, column=1, sticky="ew", padx=3, pady=5)

        tk.Label(top_form, text="Contact", font=("times new roman", 15), bg="white", width=13).grid(row=0, column=2, sticky="w", padx=3, pady=5)
        self.Custumer_contact_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_contact_E.grid(row=0, column=3, sticky="ew", padx=3, pady=5)

        cart_frame = tk.Frame(self.middle_frame,bd=2,borderwidth=2,bg="white",relief=tk.RIDGE)
        cart_frame.pack(fill="both", expand=True, padx=3, pady=5)

        self.Cart_details = tk.Frame(cart_frame,bg="#c0c0c0", relief=tk.RIDGE)
        self.Cart_details.pack(fill="x", padx=3, pady=3)
        self.Cart_details.grid_columnconfigure(0,weight=1)

        self.cart_label = Label(self.Cart_details, text="Cart ", font=("times new roman", 14, "bold"), bg="#c0c0c0",fg="black" ,justify="left")
        self.cart_label.grid(row=0,column=0,sticky="w")
        self.cart = Label(self.Cart_details, text="Total Products [0]", font=("times new roman", 14, "bold"), bg="#c0c0c0",fg="black" ,justify="left")
        self.cart.grid(row=0,column=1,sticky="w")


        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
            self.cart_table.column(col, width=100, anchor="center")

        y_scroll = ttk.Scrollbar(self.cart_table, orient="vertical", command=self.cart_table.yview)
        x_scroll = ttk.Scrollbar(self.cart_table, orient="horizontal", command=self.cart_table.xview)
        self.cart_table.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        y_scroll.pack(fill="y", side="right")
        x_scroll.pack(fill="x", side="bottom")
        self.cart_table.pack(fill="both", expand=True, side="left")
        self.cart_table.bind("<ButtonRelease-1>", self.get_cart_data)

        self.Product_details = tk.Frame(self.middle_frame,bg="white",borderwidth=2, bd=2, relief=tk.RIDGE)
        self.Product_details.pack(fill="x", padx=3, pady=3)

        entry_frame = tk.Frame(self.Product_details, bg="white",bd=2,borderwidth=2)
        entry_frame.pack(fill="x", padx=3, pady=3)

        for i in range(6):
            entry_frame.grid_columnconfigure(i, weight=1)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 15), bg="white").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        self.p_name_Entry = ttk.Entry(entry_frame,state="readonly", font=("times new roman", 18))
        self.p_name_Entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 15), bg="white").grid(row=0, column=2, sticky="w", padx=5, pady=3)
        self.price_perqty_Entry = ttk.Entry(entry_frame, font=("times new roman", 18),state="readonly")
        self.price_perqty_Entry.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 15), bg="white").grid(row=0, column=4, sticky="w", padx=5, pady=3)
        self.Quantity_Entry = tk.Entry(entry_frame, font=("times new roman", 18), bg="lightyellow")
        self.Quantity_Entry.grid(row=1, column=4, sticky="ew", padx=5, pady=5)

        button_frame = tk.Frame(self.Product_details, bg="white")
        button_frame.pack(fill="x", padx=3, pady=3)

        self.Instock_label = tk.Label(button_frame, text="In Stock[0]", font=("times new roman", 18), bg="white", anchor="w")
        self.Instock_label.pack(side="left", padx=5, pady=5)
        tk.Button(button_frame, text="Clear", font=("times new roman", 16), bg="lightgray", padx=10, command=self.clear_cart).pack(side="left", padx=5, pady=5)
        tk.Button(button_frame, text="Add|Update Cart", font=("times new roman", 15, "bold"), padx=5, bg="orange", width=25, command=self.Add_update_Cart).pack(side="left", padx=5, pady=5)

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.right_frame.grid(row=1, column=2, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.right_frame, text="Customer Billing Area", font=("times new roman", 27, "bold"), bg="orange").pack(fill="x")

        self.bill_area = tk.Text(self.right_frame, wrap="word", bg="#d3d3d3", font=("times new roman", 11))
        self.bill_area.pack(fill="both", expand=True, padx=10, pady=5)

        billing_info = tk.Frame(self.right_frame)
        billing_info.pack(fill="x", padx=10, pady=5)

        for i in range(3):
            billing_info.grid_columnconfigure(i, weight=1)

        self.Bill_amount_label = tk.Label(billing_info, text="Bill Amount\n[0]", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.Bill_amount_label.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        discount_frame = tk.Frame(billing_info, bg="orange")
        discount_frame.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        tk.Label(discount_frame, text="Discount %", font=("times new roman", 15, "bold"), bg="orange", fg="white").pack(anchor="center")
        self.Discount_Entry = tk.Entry(discount_frame, font=("times new roman", 12), width=8)
        self.Discount_Entry.pack(anchor="center", padx=5, pady=2)

        self.Bill_netpay_label = tk.Label(billing_info, text="Net Pay\n[0]", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        self.Bill_netpay_label.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

        tk.Button(billing_info, text="Print", font=("times new roman", 15), bg="white", command=self.Print_File).grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Clear All", font=("times new roman", 15), bg="lightblue", command=self.clear_all).grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("times new roman", 15), bg="pink", command=self.generate_bill).grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

        self.Billsection_show()

    # Function mappings
    def Billsection_show(self):
        self.f.Billsection_show(self.product_table)

    def Billsection_search(self):
        self.f.Billsection_search((self.root, self.Search_Name_Entry, self.product_table))

    def Billsecton_search_all(self):
        self.f.Billsecton_search_all(self.product_table, (self.root,))

    def Billsection_get_data(self, event=None):
        region = self.product_table.identify_region(event.x, event.y)
        row_id = self.product_table.identify_row(event.y)

        if region != "cell" or not row_id:
            return
        self.f.Billsection_get_data((self.root, self.price_perqty_Entry, self.p_name_Entry, self.Instock_label, self.pid, self.product_table))

    def Add_update_Cart(self):
        self.f.Add_updateCart((self.root, self.Quantity_Entry, self.p_name_Entry, self.price_perqty_Entry, self.pid, self.cart_list,
                               self.Discount_Entry, self.cart_table, self.cart, self.Bill_netpay_label, self.Bill_amount_label))

    def generate_bill(self):
        self.f.generate_bill((self.Custumer_Name_E, self.Custumer_contact_E, self.cart_list, self.Discount_Entry,
                              self.Bill_netpay_label, self.Bill_amount_label, self.bill_area, self.product_table, self.root))

    def clear_cart(self):
        self.f.clear_cart((self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Quantity_Entry,
                           self.Instock_label, self.Bill_amount_label, self.Bill_netpay_label, self.Discount_Entry))

    def clear_all(self):
        self.f.clear_all(
            (self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Quantity_Entry,
             self.Instock_label, self.Bill_amount_label, self.Bill_netpay_label, self.Discount_Entry),
            (self.root, self.cart_list, self.cart_table, self.cart, self.bill_area, self.Custumer_Name_E, self.Custumer_contact_E)
        )
        

    def Print_File(self):
        self.f.print_file(self.bill_area)

    def get_cart_data(self, event=None):
        region = self.cart_table.identify_region(event.x, event.y)
        row_id = self.cart_table.identify_row(event.y)

        if region != "cell" or not row_id:
            return
        
        mytuple = (self.root, self.cart_table, self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Instock_label)
        self.f.get_cart_data(mytuple)


    # Navbar functions
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

    def supliers(self):
        self.root.destroy()
        new_root = Tk()
        from suplyre import SupplyreClass
        self.new_obj = SupplyreClass(new_root)

if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()