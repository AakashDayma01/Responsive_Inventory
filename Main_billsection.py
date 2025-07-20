import tkinter as tk
from tkinter import ttk

class Billing_area:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1200x600")
        self.root.minsize(1000, 500)

        # Make 3 columns equally stretchable
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1, uniform='equal')
        self.root.grid_rowconfigure(0, weight=1)

        self.create_left_frame()
        self.create_middle_frame()
        self.create_right_frame()

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.left_frame, text="All products", font=("times new roman", 35, "bold"),fg="white", bg="#000066").pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=5, pady=5)

        search_frame.grid_columnconfigure(0, weight=1)
        search_frame.grid_columnconfigure(1, weight=1)
        search_frame.grid_columnconfigure(2, weight=1)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 18, "bold"),width=24 ,fg="red").grid(row=0, column=0, sticky="w", padx=0, pady=2)
        tk.Button(search_frame, text="Search All", font=("times new roman", 15, "bold"), bg="#d6eaf8").grid(row=0, column=1, columnspan=2, sticky="e", padx=5)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 17),width=10).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(search_frame, font=("times new roman", 15), bg="lightyellow").grid(row=1, column=1, sticky="ew", padx=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="#aed6f1").grid(row=1, column=2, sticky="e", padx=5)

        product_frame = tk.Frame(self.left_frame)
        product_frame.pack(fill="both", expand=True)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
        self.product_table.pack(fill="both", expand=True)

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#dcdcdc")
        self.middle_frame.grid(row=0, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.middle_frame, text="Customer Detail", font=("times new roman", 20, "bold"), bg="#c0c0c0").pack(fill="x")

        top_form = tk.Frame(self.middle_frame, bg="#dcdcdc")
        top_form.pack(fill="x", pady=5)

        for i in range(4):
            top_form.grid_columnconfigure(i, weight=1)

        tk.Label(top_form, text="Name", font=("times new roman", 15), bg="#dcdcdc",width=10).grid(row=0, column=0, pady=5, sticky="w")
        tk.Entry(top_form, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(top_form, text="Mobile No.", font=("times new roman", 15), bg="#dcdcdc",width=13).grid(row=0, column=2, padx=5, pady=5, sticky="w")
        tk.Entry(top_form, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        tk.Label(self.middle_frame, text="Cart", font=("times new roman", 14, "bold"), bg="#dcdcdc").pack(anchor="w", padx=10, pady=5)

        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)

        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", pady=10)

        for i in range(8):
            entry_frame.grid_columnconfigure(i, weight=1)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, padx=5, pady=5,column=0, sticky="w")
        tk.Entry(entry_frame, font=("times new roman", 15), bg="lightyellow").grid(row=1, column=0, padx=0, pady=5, sticky="ew")

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        tk.Entry(entry_frame, font=("times new roman", 15)).grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=3, padx=5, pady=5, sticky="w")
        tk.Entry(entry_frame, font=("times new roman", 15), bg="lightyellow").grid(row=1, column=3, padx=5, pady=5, sticky="ew")


        button_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        button_frame.pack(fill="x", padx=10)

        tk.Label(button_frame, text="In Stock[0]", font=("times new roman", 12), bg="#dcdcdc").pack(side="left", padx=5,pady=5)


        tk.Button(button_frame, text="Clear", font=("times new roman", 11), bg="lightgray", width=10).pack(side="left", padx=5,pady=5)
        tk.Button(button_frame, text="Add|Update Cart", font=("times new roman", 11, "bold"), bg="orange", width=20).pack(side="left", padx=5,pady=5)

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.right_frame, text="Customer Billing Area", font=("times new roman", 20, "bold"), bg="orange").pack(fill="x")

        self.bill_area = tk.Text(self.right_frame, wrap="word", bg="#d3d3d3", font=("times new roman", 11))
        self.bill_area.pack(fill="both", expand=True)

        billing_info = tk.Frame(self.right_frame)
        billing_info.pack(fill="x")

        for i in range(3):
            billing_info.grid_columnconfigure(i, weight=1)

        tk.Label(billing_info, text="Bill Amount\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=0, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Discount %\n0", font=("times new roman", 12, "bold"), bg="orange", fg="black").grid(row=0, column=1, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Net Pay\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=2, sticky="nsew", padx=2)

        tk.Button(billing_info, text="Print", font=("times new roman", 11), bg="white").grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Clear All", font=("times new roman", 11), bg="lightblue").grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("times new roman", 11), bg="pink").grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()
