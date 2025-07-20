from tkinter import *
from Employee import page2
import time
import os
import sqlite3
from Category import Categorie
from Sales import Sales
from suplyre import SupplyreClass
from product import product
from PIL import Image, ImageTk
from Main_billsection import Billing_area

class page1:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.state('zoomed')
        self.page_window = None
        self.page1_window = None
        self.page2_window = None
        self.page3_window = None
        self.page4_window = None
        self.page5_window = None
        self.page6_window = None
        self.root.configure(background="white")
        
        # Variable Initialization
        self.open_windows = []  # Track open windows
        
        # Top Bar
        top_frame = Frame(self.root, bg="#010c48")
        top_frame.pack(side=TOP, fill=X)
        
        Label(top_frame, text="Inventory Management System", font=("times new roman", 40, "bold"), bg="#010c48", fg="white").pack(side=LEFT, padx=20)
        Button(top_frame, text="Logout", bg="skyblue", font=("times new roman", 20, "bold"), cursor="hand2").pack(side=RIGHT, padx=10)
        Button(top_frame, text="Close", fg="black", bg="#FFA07A", font=("times new roman", 20, "bold"), cursor="hand2", command=self.Close).pack(side=RIGHT, padx=10)

        self.tittlt2 = Label(self.root, text="Welcome to Inventory Management System", font=("times new roman", 20, "bold"), bg="black", fg="white")
        self.tittlt2.pack(fill=X)
        
        # Side Frame
        side_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        side_frame.pack(side=LEFT, fill=Y)
        
        # Adding images
        self.bill_photo = Image.open("pics/p1.jpg").resize((185, 185), Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        Label(side_frame, image=self.bill_photo).pack(pady=10)
        
        # Buttons on the side
        Button(side_frame, text="Add Employee", command=self.employee2, bg="lightgrey", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        Button(side_frame, text="Billing Section", command=self.Bill_Area, bg="lightpink", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        Button(side_frame, text="Sales Section", command=self.Sales, bg="lightblue", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        Button(side_frame, text="Product Category", command=self.category, bg="#FFA07A", font=("times new roman", 17, "bold"), cursor="hand2").pack(fill=X, pady=5)
        Button(side_frame, text="Add Supplier", command=self.Suplier, bg="#E6E6FA", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        Button(side_frame, text="Add Product", command=self.product, bg="#ffffe0", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        
        # Main Display Grid
        main_frame = Frame(self.root, bg="white")
        main_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        self.Total_Emp_lbl = Label(main_frame, text="Total Employee\n[ ]", font=("times new roman", 20, "bold"), bg="lightgreen", padx=20)
        self.Total_Emp_lbl.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        
        self.Total_sales_lbl = Label(main_frame, text="Total Sales\n[ ]", font=("times new roman", 20, "bold"), bg="lightgrey", padx=20)
        self.Total_sales_lbl.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
        self.Totoal_ptoduct = Label(main_frame, text="Total Products\n[ ]", font=("times new roman", 20, "bold"), bg="lightblue", padx=20)
        self.Totoal_ptoduct.grid(row=0, column=2, padx=20, pady=20, sticky='nsew')
        
        self.Total_suplier = Label(main_frame, text="Total suppliers\n[ ]", font=("times new roman", 20, "bold"), bg="lightpink", padx=20)
        self.Total_suplier.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        
        self.Total_Categories = Label(main_frame, text="Total Categories\n[ ]", font=("times new roman", 20, "bold"), bg="skyblue", padx=20)
        self.Total_Categories.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')
      
        for i in range(3):
            main_frame.columnconfigure(i, weight=1)
        for i in range(2):
            main_frame.rowconfigure(i, weight=1)

        self.update_time()

    def Close(self):
        if self.page_window is not None:
            self.page_window.destroy()

    def update_time(self):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        self.current_time = time.strftime('%H:%M:%S') 
        self.tittlt2.config(text=f"Welcome to Inventory Management System \t\t\t   Date {str(time.strftime('%d/%m/%y'))}  \t\t\t  Time {str(self.current_time)}")
        total_sales = len(os.listdir('Bills'))
        self.Total_sales_lbl.config(text=f"Total Sales\n[{total_sales}]")
        cur.execute("select * from Employee")
        rows = cur.fetchall()
        self.Total_Emp_lbl.config(text=f"Total Employee\n[{str(len(rows))}]")
        cur.execute("select * from product")
        total_product = cur.fetchall()
        self.Totoal_ptoduct.config(text=f"Total Products\n[{str(len(total_product))}]")
        cur.execute("select * from Suplier")
        total_suplier = cur.fetchall()        
        self.Total_suplier.config(text=f"Total supliers\n[{str(len(total_suplier))}]")
        cur.execute("select * from category")
        Total_Category = cur.fetchall()
        self.Total_Categories.config(text=f"Total Categories\n[{str(len(Total_Category))}]")
        self.tittlt2.after(1000,self.update_time)


    def close_all_windows(self, current_window):
        for window in [self.page1_window,self.page2_window,self.page3_window,self.page4_window,self.page5_window,self.page6_window]:
            if window and window != current_window:
                window.destroy()
    def employee2(self):
        if self.page1_window is not None:
            self.page1_window.destroy()
            time.sleep(1) 
        self.close_all_windows(self.page1_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = page2(self.newwindow)
        self.page1_window = self.newwindow
        self.page_window = self.newwindow
        
    def category(self):
        if self.page2_window is not None:
            self.page2_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page2_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Categorie(self.newwindow)
        self.page2_window = self.newwindow
        self.page_window = self.newwindow
        
    def Sales(self):
        if self.page3_window is not None:
            self.page3_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page3_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Sales(self.newwindow)
        self.page3_window = self.newwindow
        self.page_window = self.newwindow
        
    def Suplier(self):
        if self.page4_window is not None:
            self.page4_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page4_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = SupplyreClass(self.newwindow)
        self.page4_window = self.newwindow
        self.page_window = self.newwindow
        
    def product(self):
        if self.page5_window is not None:
            self.page5_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page5_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = product(self.newwindow)
        self.page5_window = self.newwindow
        self.page_window = self.newwindow
    def Bill_Area(self):
        if self.page6_window is not None:
            self.page6_window.destroy()
            time.sleep(1)
        self.close_all_windows(self.page6_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Billing_area(self.newwindow)
        self.page6_window = self.newwindow
        self.page_window = self.newwindow
        
if __name__=="__main__":
    root=Tk()
    obj = page1(root)
    root.mainloop()




