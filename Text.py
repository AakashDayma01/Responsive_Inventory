from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk

class Sales:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.resizable(True, True)
        self.root.focus_force()

        # Title
        self.tittle = Label(self.root, bg="black", text="Customer Bill Reports", height=2, justify="center",
                            font=("goudy old style", 25, "bold"), fg="white")
        self.tittle.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Invoice Entry
        self.Invoice_Entry = Label(self.root, text="Invoice No.", font=("times new roman", 20, "bold"))
        self.Invoice_Entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.Name_Entry = Entry(self.root, font=("arial", 15, "bold"), bd=2, bg="lightyellow")
        self.Name_Entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        btn_add = Button(self.root, text="Search", relief="solid", command=self.search, border=1, highlightthickness=1,
                         padx=20, pady=10, bg="light blue", font=("times new roman", 20, "bold"), cursor="hand2")
        btn_add.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        btn_update = Button(self.root, text="Clear", padx=20, pady=10, relief="solid", border=1, highlightthickness=2,
                            bg="light pink", font=("times new roman", 20, "bold"), cursor="hand2")
        btn_update.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        # Listbox Frame
        self.Listframe = Frame(self.root, relief=RIDGE, bg="white", bd=3)
        self.Listframe.grid(row=2, column=0, rowspan=2, padx=10, pady=10, sticky="ns")

        self.scrolly = Scrollbar(self.Listframe, orient=VERTICAL)
        self.listbox = Listbox(self.Listframe, bg="white", font=("goudy old style", 18, "bold"),
                               yscrollcommand=self.scrolly.set)
        self.scrolly.config(command=self.listbox.yview)
        self.scrolly.pack(fill=Y, side=RIGHT)
        self.listbox.pack(fill=BOTH, expand=1)
        self.listbox.bind("<ButtonRelease-1>", self.get_data)

        # Bill Frame
        self.Billframe = Frame(self.root, bd=2, bg="white")
        self.Billframe.grid(row=2, column=1, rowspan=2, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.billlabel = Label(self.Billframe, text="Bill Area", bg="darkblue", fg="white",
                               font=("goudy old style", 20, "bold"))
        self.billlabel.pack(fill="x", side=TOP)

        self.billscrollbar = Scrollbar(self.Billframe, orient=VERTICAL)
        self.billtextarea = Text(self.Billframe, bg="lightyellow", font=("goudy old style", 15, "bold"),
                                 state=DISABLED, bd=2, fg="black", yscrollcommand=self.billscrollbar.set)
        self.billscrollbar.config(command=self.billtextarea.yview)
        self.billscrollbar.pack(fill=Y, side=RIGHT)
        self.billtextarea.pack(fill=BOTH, expand=1)

        # Image
        self.bill_photo = Image.open("pics/p1.jpg")
        self.bill_photo = self.bill_photo.resize((430, 430), Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        self.lbl = Label(self.root, image=self.bill_photo)
        self.lbl.grid(row=2, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Configure grid weights
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.show()

    # Function Definitions
    def show(self):
        self.listbox.delete(0, END)
        for i in os.listdir('Bills'):
            if i.split(".")[1] == "txt":
                self.listbox.insert(END, i)

    def search(self):
        for i in os.listdir('Bills'):
            if i.split(".")[0] == self.Name_Entry.get():
                self.listbox.delete(0, END)
                self.listbox.insert(0, i)
                break

    def get_data(self, ev):
        self.billtextarea.config(state=NORMAL)
        a = self.listbox.curselection()
        self.file_name = self.listbox.get(a)
        self.file_data = open(f'Bills/{self.file_name}', 'r')
        self.billtextarea.delete("0.1", END)
        self.billdata = self.file_data.read()
        self.billtextarea.insert(END, self.billdata)
        self.billtextarea.config(state=DISABLED)
        self.file_data.close()

if __name__ == "__main__":
    root = Tk()
    obj = Sales(root)
    root.mainloop()










# Page1.py file code  


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
        self.page_window = None
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
        Button(side_frame, text="Add Product", command=self.category, bg="#ffffe0", font=("times new roman", 20, "bold"), cursor="hand2").pack(fill=X, pady=5)
        
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








# Employee.py file code   


from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime
import Functions


class page2:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1335x615+200+135")
        self.root.title("Inventory Management System")
        self.root.resizable(False, False)
        self.f = Functions.function()

        self.lbl = None
        self.lbl1 = None

        root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.focus_force()

        # --- Search Frame ---
        self.frame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 20, "bold"), bd=3, height=90, width=800)
        self.frame.place(x=100, y=10)

        self.searchby = ttk.Combobox(self.frame, values=("Select", "Email", "Name", "Contact"),
                                     state="readonly", justify=CENTER, height=10, width=20,
                                     font=("arial", 15, "bold"))
        self.searchby.place(x=20, y=5)
        self.searchby.current(0)

        self.search1 = ttk.Entry(self.frame, font=("arial", 15, "bold"))
        self.search1.place(x=300, y=5)

        btn_Search = Button(self.frame, text="Search", command=self.Search_data, relief="solid",
                            border=1, padx=20, pady=10, bg="dark grey",
                            font=("times new roman", 20, "bold"), cursor="hand2")
        btn_Search.place(x=570, y=-6, height=50, width=190)

        # --- Employee Details Header ---
        self.frame2 = Label(self.root, text="Employee Details", font=("times new roman", 20, "bold"),
                            bg="black", fg="white")
        self.frame2.place(x=30, y=110, width=1275, height=40)

        # --- Form Fields ---
        self.Emp_no = Label(self.root, text="Emp No.", font=("times new roman", 20, "bold"))
        self.Emp_no.place(x=32, y=170, width=125, height=50)
        self.Emp_Entry = ttk.Entry(self.root, state="readonly", font=("arial", 15, "bold"))
        self.Emp_Entry.place(x=180, y=175)

        self.name = Label(self.root, text="Name", font=("times new roman", 20, "bold"))
        self.name.place(x=15, y=220, width=125, height=50)
        self.name_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"))
        self.name_Entry.place(x=180, y=230)

        self.email = Label(self.root, text="Email", font=("times new roman", 20, "bold"))
        self.email.place(x=15, y=275, width=125, height=50)
        self.email_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"))
        self.email_Entry.place(x=180, y=285)

        self.gender = Label(self.root, text="Gender", font=("times new roman", 20, "bold"))
        self.gender.place(x=425, y=165, width=125, height=60)
        self.gender_entry = ttk.Combobox(self.root, values=("Select", "Male", "Female"),
                                         state="readonly", justify=CENTER, font=("arial", 15, "bold"))
        self.gender_entry.place(x=590, y=170)
        self.gender_entry.current(0)

        self.dob = Label(self.root, text="D.O.B.", font=("times new roman", 20, "bold"))
        self.dob.place(x=425, y=220, width=125, height=50)
        self.dob_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"), state="readonly")
        self.dob_Entry.place(x=590, y=230, width=245)
        self.dob_Entry.bind("<Button-1>", self.Show_caleder_dob)

        self.password = Label(self.root, text="Password", font=("times new roman", 20, "bold"))
        self.password.place(x=440, y=275, width=125, height=50)
        self.password_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"))
        self.password_Entry.place(x=590, y=285, width=245)

        self.contact = Label(self.root, text="Contact No.", font=("times new roman", 20, "bold"))
        self.contact.place(x=870, y=155, width=140, height=50)
        self.contact_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"))
        self.contact_Entry.place(x=1050, y=160, width=240)

        self.doj = Label(self.root, text="D.O.J.", font=("times new roman", 20, "bold"))
        self.doj.place(x=850, y=220, width=125, height=50)
        self.doj_Entry = ttk.Entry(self.root, state="readonly", font=("arial", 15, "bold"))
        self.doj_Entry.place(x=1050, y=220, width=240)
        self.doj_Entry.bind("<Button-1>", self.Show_caleder_doj)

        self.usert_type = Label(self.root, text="User Type", font=("times new roman", 20, "bold"))
        self.usert_type.place(x=870, y=265, width=125, height=60)
        self.usert_type_cmb = ttk.Combobox(self.root, values=("Admin", "Employee"),
                                           justify=CENTER, state="readonly", font=("arial", 15, "bold"))
        self.usert_type_cmb.place(x=1050, y=280)
        self.usert_type_cmb.current(0)

        self.Address = Label(self.root, text="Address", font=("times new roman", 20, "bold"))
        self.Address.place(x=26, y=330, width=125, height=50)
        self.Address_Entry = Text(self.root, font=("arial", 15, "bold"))
        self.Address_Entry.place(x=180, y=340, width=300, height=70)

        self.Salary = Label(self.root, text="Salary", font=("times new roman", 20, "bold"))
        self.Salary.place(x=480, y=320, width=125, height=50)
        self.Salary_Entry = ttk.Entry(self.root, font=("arial", 15, "bold"))
        self.Salary_Entry.place(x=630, y=330, width=245)

        # --- Buttons ---
        Button(self.root, text="Save", command=self.ad_data, bg="light blue",
               font=("times new roman", 20, "bold"), cursor="hand2").place(x=490, y=370, height=40, width=170)

        Button(self.root, text="Update", command=self.Update_data, bg="light green",
               font=("times new roman", 20, "bold"), cursor="hand2").place(x=710, y=370, height=40, width=170)

        Button(self.root, text="Delete", command=self.Delete, bg="light grey",
               font=("times new roman", 20, "bold"), cursor="hand2").place(x=930, y=370, height=40, width=170)

        Button(self.root, text="Clear", command=self.clear_data, bg="pink",
               font=("times new roman", 20, "bold"), cursor="hand2").place(x=1150, y=370, height=40, width=170)

        # --- Treeview ---
        self.frame3 = LabelFrame(self.root, bd=3)
        self.frame3.place(x=20, y=420, width=1285, height=140)

        self.frameTreaview = ttk.Treeview(self.frame3, columns=("eid", "name", "email", "gender",
                                                                "contact", "dob", "doj", "pass", "utype", "address", "salary"))
        self.frameTreaview.pack(fill=BOTH, expand=1)

        self.show_data(self.frameTreaview)

    def ad_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.add(mytuple)
    def clear_data(self):
        mytuple=(self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry, self.Salary_Entry )
        self.f.clear(mytuple)
    def show_data(self,frameTreaview):
        self.f.show(self.frameTreaview,self.root)
    def generateeId(self):
        Eid_tuple = (self.Emp_Entry,)
        self.f.generateeid(Eid_tuple)                                         
    def Get_Data(self,event = None):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.get_data(mytuple)
    def Update_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.update(mytuple)
    def Delete(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.delete(mytuple)
    def Search_data(self):
        mytuple = (self.root,self.search1,self.searchby,self.frameTreaview)
        self.f.search(mytuple)
    def Show_caleder_dob(self,event = None):
        MyTuple = (self.dob_Entry,self.root)
        self.f.show_calendar(MyTuple,self.lbl)
    def Show_caleder_doj(self,event = None):
        MyTuple = (self.doj_Entry,self.root)
        self.f.show_calendar_doj(MyTuple,self.lbl1)
if __name__=="__main__":
    root=Tk()
    obj = page2(root)
    root.mainloop()




# employee.py  fully responsive 



from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar
import string
from datetime import datetime
import Functions

class page2:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f0f0f0")
        self.f = Functions.function()
        
        self.lbl = None
        self.lbl1 = None
        
        self.root.wm_attributes("-topmost", True)
        self.root.focus_force()

        # Search Frame
        self.create_search_frame()
        
        # Employee Details Frame
        self.create_employee_details_frame()
        
        # Employee Form Fields
        self.create_employee_form()
        
        # Buttons
        self.create_buttons()
        
        # Table
        self.create_table()
        
        self.generateeId()
        self.show_data(self.frameTreaview)

    def create_search_frame(self):
        self.frame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 20, "bold"), bd=3, bg="#e6e6e6")
        self.frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.12)
        
        self.searchby = ttk.Combobox(self.frame, values=("Select", "Email", "name", "contact"), state="readonly", justify=CENTER, font=("arial", 15, "bold"))
        self.searchby.place(relx=0.02, rely=0.25, relwidth=0.2)
        self.searchby.current(0)
        
        self.search1 = ttk.Entry(self.frame, font=("arial", 15, "bold"))
        self.search1.place(relx=0.3, rely=0.25, relwidth=0.4)
        
        btn_Search = Button(self.frame, text="Search", command=self.Search_data, bg="#4caf50", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Search.place(relx=0.75, rely=0.1, relwidth=0.2, relheight=0.8)
    
    def create_employee_details_frame(self):
        self.frame2 = Label(self.root, text="Employee Details", font=("times new roman", 20, "bold"), bg="#333", fg="white")
        self.frame2.place(relx=0.03, rely=0.16, relwidth=0.94, relheight=0.05)
    
    def create_employee_form(self):
        labels = ["Emp No.", "Name", "Email", "Gender", "Contact No.", "D.O.B.", "D.O.J.", "Password", "User Type", "Address", "Salary"]
        positions = [
            (0.03, 0.23), (0.03, 0.33), (0.03, 0.43),
            (0.33, 0.23), (0.63, 0.23),
            (0.33, 0.33), (0.63, 0.33),
            (0.33, 0.43), (0.63, 0.43),
            (0.03, 0.53), (0.33, 0.53)
        ]
        
        self.entries = {}
        for i, label in enumerate(labels):
            lbl = Label(self.root, text=label, font=("times new roman", 15, "bold"), bg="#f0f0f0")
            lbl.place(relx=positions[i][0], rely=positions[i][1], relwidth=0.1, relheight=0.05)
            
            if label in ["Gender", "User Type"]:
                values = ("Select", "Male", "Female") if label == "Gender" else ("Admin", "Employee")
                entry = ttk.Combobox(self.root, values=values, state="readonly", justify=CENTER, font=("arial", 12, "bold"))
                entry.current(0)
            elif label in ["D.O.B.", "D.O.J."]:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"), state="readonly")
                entry.bind("<Button-1>", self.Show_caleder_dob if label == "D.O.B." else self.Show_caleder_doj)
            elif label == "Address":
                entry = Text(self.root, font=("arial", 12, "bold"))
            else:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"))
            
            entry.place(relx=positions[i][0] + 0.12, rely=positions[i][1], relwidth=0.2, relheight=0.05)
            self.entries[label] = entry
    
    def create_buttons(self):
        colors = ["#2196F3", "#4CAF50", "#f44336", "#FFC107"]
        texts = ["Save", "Update", "Delete", "Clear"]
        commands = [self.ad_data, self.Update_data, self.Delete, self.clear_data]
        
        for i in range(4):
            btn = Button(self.root, text=texts[i], command=commands[i], bg=colors[i], fg="white", font=("times new roman", 15, "bold"), cursor="hand2", relief=RAISED)
            btn.place(relx=0.48 + i*0.13, rely=0.62, relwidth=0.12, relheight=0.05)
    
    def create_table(self):
        self.frame3 = Frame(self.root, bg="white")
        self.frame3.place(relx=0.03, rely=0.7, relwidth=0.94, relheight=0.28)
        
        self.scrolly = Scrollbar(self.frame3, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3, orient=HORIZONTAL)
        
        self.frameTreaview = ttk.Treeview(
            self.frame3,
            columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
            yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set
        )
        
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrollx.config(command=self.frameTreaview.xview)
        self.scrolly.config(command=self.frameTreaview.yview)
        
        for col in self.frameTreaview["columns"]:
            self.frameTreaview.heading(col, text=col.upper())
            self.frameTreaview.column(col, width=120)
        
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.pack(fill=BOTH, expand=1)
        self.frameTreaview.bind("<ButtonRelease-1>", self.Get_Data)

    def ad_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.add(mytuple)
    def clear_data(self):
        mytuple=(self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry, self.Salary_Entry )
        self.f.clear(mytuple)
    def show_data(self,frameTreaview):
        self.f.show(self.frameTreaview,self.root)
    def generateeId(self):
        Eid_tuple = (self.Emp_Entry,)
        self.f.generateeid(Eid_tuple)                                         
    def Get_Data(self,event = None):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.get_data(mytuple)
    def Update_data(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.update(mytuple)
    def Delete(self):
        mytuple = (self.root,self.Emp_Entry,self.name_Entry,self.email_Entry,self.gender_entry,self.contact_Entry,self.dob_Entry,self.doj_Entry,self.password_Entry,self.usert_type_cmb,self.Address_Entry,self.Salary_Entry ,self.frameTreaview)
        self.f.delete(mytuple)
    def Search_data(self):
        mytuple = (self.root,self.search1,self.searchby,self.frameTreaview)
        self.f.search(mytuple)
    def Show_caleder_dob(self,event = None):
        MyTuple = (self.dob_Entry,self.root)
        self.f.show_calendar(MyTuple,self.lbl)
    def Show_caleder_doj(self,event = None):
        MyTuple = (self.doj_Entry,self.root)
        self.f.show_calendar_doj(MyTuple,self.lbl1)

if __name__ == "__main__":
    root = Tk()
    obj = page2(root)
    root.mainloop()








# total responsive Supplier Class

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Functions


class SupplyreClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f0f0f0")

        # Functions Instance
        self.f = Functions.function()

        # Header Frame
        header_frame = Frame(self.root, bg="black")
        header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        lbl_title = Label(header_frame, text="Supplier Details", font=("times new roman", 25, "bold"), fg="white", bg="black")
        lbl_title.pack(side=LEFT, padx=20)

        # Search Section
        search_frame = Frame(self.root, bg="#f0f0f0")
        search_frame.place(relx=0.58, rely=0.12, relwidth=0.4, relheight=0.08)

        lbl_search = Label(search_frame, text="Invoice no:", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_search.pack(side=LEFT, padx=10)

        self.Search_Entry = ttk.Entry(search_frame, font=("arial", 15))
        self.Search_Entry.pack(side=LEFT, fill=X, expand=True, padx=10)

        btn_Search = Button(search_frame, text="Search", command=self.Sup_Search, bg="green", fg="white",
                            font=("times new roman", 15, "bold"), cursor="hand2")
        btn_Search.pack(side=LEFT, padx=10)

        # Left Form Section
        form_frame = Frame(self.root, bg="#f0f0f0", bd=2, relief=SOLID)
        form_frame.place(relx=0.02, rely=0.12, relwidth=0.55, relheight=0.65)

        lbl_invoice = Label(form_frame, text="Invoice No.", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_invoice.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.Sup_Entry = ttk.Entry(form_frame, font=("arial", 13))
        self.Sup_Entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        lbl_name = Label(form_frame, text="Name", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.name_Entry = ttk.Entry(form_frame, font=("arial", 13))
        self.name_Entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        lbl_contact = Label(form_frame, text="Contact", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_contact.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.Contact_Entry = ttk.Entry(form_frame, font=("arial", 13))
        self.Contact_Entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        lbl_desc = Label(form_frame, text="Description", font=("times new roman", 15, "bold"), bg="#f0f0f0")
        lbl_desc.grid(row=3, column=0, padx=10, pady=10, sticky="nw")

        self.DEsc_Entry = Text(form_frame, font=("arial", 13), height=5, width=30)
        self.DEsc_Entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Button Section
        btn_frame = Frame(form_frame, bg="#f0f0f0")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

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
        table_frame.place(relx=0.58, rely=0.22, relwidth=0.4, relheight=0.55)

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


if __name__ == "__main__":
    root = Tk()
    obj = SupplyreClass(root)
    root.mainloop()






# responsive category page 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Functions

class Categorie:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#E0E0E0")

        self.f = Functions.function()

        # Variables
        self.Cat_var = StringVar()
        self.name_var = StringVar()

        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Header
        self.tittle_frame = Label(self.root, text="Manage Product Categories", 
                                  font=("times new roman", 30, "bold"), bd=3, 
                                  relief=RIDGE, bg="black", fg="white")
        self.tittle_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Entry & Buttons Frame
        entry_frame = Frame(self.root, bg="#E0E0E0")
        entry_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        Label(entry_frame, text="Enter category Name", font=("times new roman", 20, "bold"), bg="#E0E0E0")\
            .grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.Name_Entry = Entry(entry_frame, textvariable=self.name_var, font=("arial", 15, "bold"), bg="lightyellow")
        self.Name_Entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

        btn_frame = Frame(entry_frame, bg="#E0E0E0")
        btn_frame.grid(row=0, column=2, padx=10)

        Button(btn_frame, text="Save", command=self.Cat_add, bg="blue", fg="white", 
               font=("times new roman", 15, "bold"), cursor="hand2").grid(row=0, column=0, sticky="ew", padx=5)
        
        Button(btn_frame, text="Delete", command=self.Cat_delete, bg="red", fg="white", 
               font=("times new roman", 15, "bold"), cursor="hand2").grid(row=0, column=1, sticky="ew", padx=5)

        # Category Table Frame
        self.cat_frame = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        self.cat_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.scrolly = Scrollbar(self.cat_frame, orient=VERTICAL)
        self.scrollx = Scrollbar(self.cat_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview(self.cat_frame, columns=("Cid", "name"),
                                           yscrollcommand=self.scrolly.set, 
                                           xscrollcommand=self.scrollx.set)
        
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

        # Images Section
        self.load_images()

    def load_images(self):
        """ Load and display images only once """
        img1 = Image.open("pics/p2.jpg").resize((630, 330), Image.LANCZOS)
        self.bill_photo1 = ImageTk.PhotoImage(img1)
        
        img2 = Image.open("pics/p3.webp").resize((630, 330), Image.LANCZOS)
        self.bill_photo2 = ImageTk.PhotoImage(img2)

        # Images Frame
        img_frame = Frame(self.root, bg="#E0E0E0")
        img_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        lbl1 = Label(img_frame, image=self.bill_photo1, bg="white")
        lbl1.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

        lbl2 = Label(img_frame, image=self.bill_photo2, bg="white")
        lbl2.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    def Cat_add(self):
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.Categories_add(Cattuple)

    def cat_show(self):
        Cattuple = (self.root,)
        self.f.Categories_show(self.category_table, Cattuple[0])

    def Cat_Get_data(self, event=None):
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.Categories_get_data(Cattuple)

    def Cat_delete(self):
        Cattuple = (self.root, self.Name_Entry, self.category_table, self.Cat_var)
        self.f.category_delete(Cattuple)


if __name__ == "__main__":
    root = Tk()
    obj = Categorie(root)
    root.mainloop()




# Main bill section1 
import tkinter as tk
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1200x600")
root.minsize(1000, 500)

# Make main grid responsive
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# =================== LEFT FRAME (All Products) ===================
left_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
left_frame.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
left_frame.grid_rowconfigure(2, weight=1)  # Make product table expandable
left_frame.grid_columnconfigure(0, weight=1)

# Header
tk.Label(left_frame, text="All products", font=("Helvetica", 24, "bold"),
         fg="white", bg="blue").pack(fill="x")

# Search Frame
search_frame = tk.Frame(left_frame, bd=2, relief=tk.RIDGE)
search_frame.pack(fill="x", pady=2, padx=2)

tk.Label(search_frame, text="Search Product | By Name", font=("Helvetica", 14),
         fg="red").grid(row=0, column=0, sticky="w", padx=2, pady=2, columnspan=4)

tk.Label(search_frame, text="Product Name", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=2)
search_entry = tk.Entry(search_frame, font=("Helvetica", 12))
search_entry.grid(row=1, column=1, padx=2, sticky="ew")

search_button_all = tk.Button(search_frame, text="Search All", bg="lightblue")
search_button_all.grid(row=1, column=2, padx=2, pady=2)

search_button = tk.Button(search_frame, text="Search", bg="lightblue")
search_button.grid(row=1, column=3, padx=2, pady=2)

# Configure search_frame columns for responsiveness
search_frame.columnconfigure(1, weight=1)

# Product table
product_table = ttk.Treeview(left_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
for col in product_table["columns"]:
    product_table.heading(col, text=col.upper())
product_table.pack(fill="both", expand=True, padx=2, pady=2)

# =================== MIDDLE FRAME (Customer + Cart) ===================
middle_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
middle_frame.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
middle_frame.grid_rowconfigure(1, weight=1)  # Expand cart table
middle_frame.grid_columnconfigure(0, weight=1)

# Customer Details Frame
cust_frame = tk.Frame(middle_frame, bg="lightgray")
cust_frame.pack(fill="x", padx=2, pady=2)

tk.Label(cust_frame, text="Customer Detail", font=("Helvetica", 18)).pack(fill="x")

# Customer Name
name_frame = tk.Frame(cust_frame, bg="lightgray")
name_frame.pack(fill="x", pady=2, padx=2)
tk.Label(name_frame, text="Name", font=("Helvetica", 12)).pack(side="left")
name_entry = tk.Entry(name_frame, font=("Helvetica", 12))
name_entry.pack(side="left", fill="x", expand=True, padx=2)

# Customer Contact
contact_frame = tk.Frame(cust_frame, bg="lightgray")
contact_frame.pack(fill="x", pady=2, padx=2)
tk.Label(contact_frame, text="Contact", font=("Helvetica", 12)).pack(side="left")
contact_entry = tk.Entry(contact_frame, font=("Helvetica", 12))
contact_entry.pack(side="left", fill="x", expand=True, padx=2)

# Cart Label
tk.Label(middle_frame, text="Cart", font=("Helvetica", 14)).pack(fill="x", padx=2)

# Cart Treeview
cart_table = ttk.Treeview(middle_frame, columns=("pid", "name", "price", "qty"), show="headings")
for col in cart_table["columns"]:
    cart_table.heading(col, text=col.upper())
cart_table.pack(fill="both", expand=True, padx=2, pady=2)

# Bottom Entry and Buttons for Adding/Updating Cart
bottom_entry = tk.Frame(middle_frame)
bottom_entry.pack(fill="x", pady=5, padx=2)

# Product Name Entry
tk.Label(bottom_entry, text="Product Name", font=("Helvetica", 12)).grid(row=0, column=0, padx=5)
product_name_entry = tk.Entry(bottom_entry, width=15)
product_name_entry.grid(row=0, column=1, padx=5)

# Price per Quantity Entry
tk.Label(bottom_entry, text="Price per Qty", font=("Helvetica", 12)).grid(row=0, column=2, padx=5)
price_entry = tk.Entry(bottom_entry, width=10)
price_entry.grid(row=0, column=3, padx=5)

# Quantity Entry
tk.Label(bottom_entry, text="Quantity", font=("Helvetica", 12)).grid(row=0, column=4, padx=5)
qty_entry = tk.Entry(bottom_entry, width=10)
qty_entry.grid(row=0, column=5, padx=5)

# In Stock Label (can be used for showing stock info)
in_stock_label = tk.Label(bottom_entry, text="In Stock", font=("Helvetica", 12))
in_stock_label.grid(row=1, column=0, padx=5, pady=2)

# Buttons: Clear and Add/Update Cart
clear_button = tk.Button(bottom_entry, text="Clear", bg="lightgray", font=("Helvetica", 12))
clear_button.grid(row=1, column=1, pady=5)

add_update_button = tk.Button(bottom_entry, text="Add|Update Cart", bg="orange", font=("Helvetica", 12))
add_update_button.grid(row=1, column=2, columnspan=2, padx=5)

# Configure bottom_entry columns for responsiveness
bottom_entry.columnconfigure([1, 3, 5], weight=1)

# =================== RIGHT FRAME (Billing Area) ===================
right_frame = tk.Frame(root, bd=2, relief=tk.RIDGE)
right_frame.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
right_frame.grid_rowconfigure(1, weight=1)  # Expand bill text area
right_frame.grid_columnconfigure(0, weight=1)

# Billing Label
tk.Label(right_frame, text="Customer Billing Area", font=("Helvetica", 18), bg="orange").pack(fill="x")

# Bill Text Area with Scrollbar
bill_frame = tk.Frame(right_frame)
bill_frame.pack(fill="both", expand=True, padx=2, pady=2)

bill_scroll = tk.Scrollbar(bill_frame, orient=tk.VERTICAL)
bill_scroll.pack(side="right", fill="y")

bill_area = tk.Text(bill_frame, wrap="word", bg="lightgray", yscrollcommand=bill_scroll.set)
bill_area.pack(fill="both", expand=True)
bill_scroll.config(command=bill_area.yview)

# Billing Info: Amount, Discount, Net Pay
info_frame = tk.Frame(right_frame)
info_frame.pack(fill="x", pady=2, padx=2)

# Create labels with grid inside info_frame
labels_data = [
    ("Bill Amount\n[0]", "blue"),
    ("Discount %\n0", "orange"),
    ("Net Pay\n[0]", "blue")
]

for i, (text, bg_color) in enumerate(labels_data):
    lbl = tk.Label(info_frame, text=text, font=("Helvetica", 12), bg=bg_color, fg="white",
                   width=15, height=2, relief=tk.RIDGE)
    lbl.grid(row=0, column=i, padx=2, sticky="nsew")
    info_frame.columnconfigure(i, weight=1)

# Buttons: Print, Clear All, Save Bill
buttons_frame = tk.Frame(right_frame)
buttons_frame.pack(fill="x", pady=2, padx=2)

# Create buttons with proper assignment
print_btn = tk.Button(buttons_frame, text="Print", font=("Helvetica", 12))
print_btn.pack(side="left", fill="x", expand=True, padx=2)

clear_btn = tk.Button(buttons_frame, text="Clear All", font=("Helvetica", 12), bg="lightblue")
clear_btn.pack(side="left", fill="x", expand=True, padx=2)

save_btn = tk.Button(buttons_frame, text="Generate\nSave Bill", font=("Helvetica", 12), bg="pink")
save_btn.pack(side="left", fill="x", expand=True, padx=2)

# Make the whole grid responsive
root.rowconfigure(0, weight=1)
root.columnconfigure([0, 1, 2], weight=1)

# Run the application
root.mainloop()

#main bill section 2
import tkinter as tk
from tkinter import ttk

class InventoryBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Billing System")
        self.root.geometry("1200x600")
        self.root.minsize(1000, 500)

        # Responsive layout configuration
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.create_left_frame()
        self.create_middle_frame()
        self.create_right_frame()

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.left_frame, text="All products", font=("Helvetica", 20, "bold"), fg="white", bg="#003f8a").pack(fill="x")

        self.create_search_section()
        self.create_product_table()

    def create_search_section(self):
        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=5, pady=5)

        tk.Label(search_frame, text="Search Product | By Name", font=("Helvetica", 13, "bold"), fg="red").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        tk.Button(search_frame, text="Search All", font=("Helvetica", 11, "bold"), bg="lightblue").grid(row=0, column=1, padx=10)

        tk.Label(search_frame, text="Product Name", font=("Helvetica", 11)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(search_frame, font=("Helvetica", 11), width=20).grid(row=1, column=1, padx=5)
        tk.Button(search_frame, text="Search", font=("Helvetica", 11, "bold"), bg="lightblue").grid(row=1, column=2, padx=10)

    def create_product_table(self):
        self.product_table = ttk.Treeview(self.left_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
        self.product_table.pack(fill="both", expand=True, padx=5, pady=5)

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#f2f2f2")
        self.middle_frame.grid(row=0, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(2, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.middle_frame, text="Customer Detail", font=("Helvetica", 18, "bold"), bg="#f2f2f2").pack(fill="x", padx=5, pady=5)
        self.create_customer_detail_section()
        self.create_cart_section()

    def create_customer_detail_section(self):
        top_form = tk.Frame(self.middle_frame, bg="#f2f2f2")
        top_form.pack(fill="x", padx=5)

        tk.Label(top_form, text="Name", font=("Helvetica", 11), bg="#f2f2f2").grid(row=0, column=0, sticky="w", padx=5)
        tk.Entry(top_form, font=("Helvetica", 11), width=20).grid(row=0, column=1, padx=5)
        tk.Label(top_form, text="Contact", font=("Helvetica", 11), bg="#f2f2f2").grid(row=0, column=2, padx=5)
        tk.Entry(top_form, font=("Helvetica", 11), width=20).grid(row=0, column=3, padx=5)

    def create_cart_section(self):
        tk.Label(self.middle_frame, text="Cart", font=("Helvetica", 14, "bold"), bg="#f2f2f2").pack(anchor="w", padx=10, pady=2)

        cart_table = ttk.Treeview(self.middle_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in cart_table["columns"]:
            cart_table.heading(col, text=col.upper())
        cart_table.pack(fill="both", expand=True, padx=5)

        self.create_bottom_entry_section()

    def create_bottom_entry_section(self):
        bottom_entry = tk.Frame(self.middle_frame, bg="#f2f2f2")
        bottom_entry.pack(fill="x", padx=5, pady=5)

        tk.Label(bottom_entry, text="Product Name", font=("Helvetica", 11), bg="#f2f2f2").grid(row=0, column=0, padx=5)
        tk.Entry(bottom_entry, width=15).grid(row=0, column=1, padx=5)

        tk.Label(bottom_entry, text="Price per Qty", font=("Helvetica", 11), bg="#f2f2f2").grid(row=0, column=2, padx=5)
        tk.Entry(bottom_entry, width=10).grid(row=0, column=3, padx=5)

        tk.Label(bottom_entry, text="Quantity", font=("Helvetica", 11), bg="#f2f2f2").grid(row=0, column=4, padx=5)
        tk.Entry(bottom_entry, width=10).grid(row=0, column=5, padx=5)

        tk.Label(bottom_entry, text="In Stock", font=("Helvetica", 11), bg="#f2f2f2").grid(row=1, column=0, padx=5)
        tk.Button(bottom_entry, text="Clear", bg="#cccccc", font=("Helvetica", 11)).grid(row=1, column=1, pady=5)
        tk.Button(bottom_entry, text="Add | Update Cart", bg="orange", font=("Helvetica", 11)).grid(row=1, column=2, columnspan=2, padx=5)

    def create_right_frame(self):
        self.right_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=2, sticky="nsew")
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.right_frame, text="Customer Billing Area", font=("Helvetica", 18, "bold"), bg="orange").pack(fill="x")

        self.create_bill_area()
        self.create_billing_info_section()

    def create_bill_area(self):
        self.bill_area = tk.Text(self.right_frame, wrap="word", bg="#f0f0f0", font=("Helvetica", 11))
        self.bill_area.pack(fill="both", expand=True, padx=5, pady=5)

    def create_billing_info_section(self):
        billing_info = tk.Frame(self.right_frame)
        billing_info.pack(fill="x", padx=5, pady=5)

        tk.Label(billing_info, text="Bill Amount\n[0]", font=("Helvetica", 12), bg="blue", fg="white", width=15).grid(row=0, column=0, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Discount %\n0", font=("Helvetica", 12), bg="orange", fg="black", width=15).grid(row=0, column=1, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Net Pay\n[0]", font=("Helvetica", 12), bg="blue", fg="white", width=15).grid(row=0, column=2, sticky="nsew", padx=2)

        tk.Button(billing_info, text="Print", font=("Helvetica", 11), bg="white").grid(row=1, column=0, sticky="nsew", pady=2, padx=2)
        tk.Button(billing_info, text="Clear All", font=("Helvetica", 11), bg="lightblue").grid(row=1, column=1, sticky="nsew", pady=2, padx=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("Helvetica", 11), bg="pink").grid(row=1, column=2, sticky="nsew", pady=2, padx=2)

        for i in range(3):
            billing_info.grid_columnconfigure(i, weight=1)

# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryBillingSystem(root)
    root.mainloop()


#Update 3 main bill section

import tkinter as tk
from tkinter import ttk

class InventoryBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1200x600")
        self.root.minsize(1000, 500)

        # Make all 3 columns equal in size
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

        tk.Label(self.left_frame, text="All products", font=("times new roman", 22, "bold"), fg="white", bg="#000066").pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=5, pady=5)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 13, "bold"), fg="red").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        tk.Button(search_frame, text="Search All", font=("times new roman", 13, "bold"), bg="#d6eaf8").grid(row=0, column=1, padx=10)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(search_frame, font=("times new roman", 12), width=20, bg="lightyellow").grid(row=1, column=1, padx=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="#aed6f1").grid(row=1, column=2, padx=10)

        # Product table
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
        top_form.pack(fill="x", padx=5, pady=2)

        tk.Label(top_form, text="Name", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=0, padx=5)
        tk.Entry(top_form, width=20, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=1, padx=5)
        tk.Label(top_form, text="Contact", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=2, padx=5)
        tk.Entry(top_form, width=20, font=("times new roman", 12)).grid(row=0, column=3, padx=5)

        # Cart
        tk.Label(self.middle_frame, text="Cart", font=("times new roman", 14, "bold"), bg="#dcdcdc").pack(anchor="w", padx=10, pady=3)
        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)

        # Bottom entry form
        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", pady=5)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=0, padx=5)
        tk.Entry(entry_frame, width=15).grid(row=0, column=1, padx=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=2, padx=5)
        tk.Entry(entry_frame, width=10).grid(row=0, column=3, padx=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=4, padx=5)
        tk.Entry(entry_frame, width=10, bg="lightyellow").grid(row=0, column=5, padx=5)

        tk.Label(entry_frame, text="In Stock", font=("times new roman", 12), bg="#dcdcdc").grid(row=1, column=0, padx=5)
        tk.Button(entry_frame, text="Clear", font=("times new roman", 11), bg="lightgray").grid(row=1, column=1, pady=5)
        tk.Button(entry_frame, text="Add|Update Cart", font=("times new roman", 11, "bold"), bg="orange").grid(row=1, column=2, columnspan=2, padx=5)

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

        tk.Label(billing_info, text="Billl Amount\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15).grid(row=0, column=0, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Discount %\n0", font=("times new roman", 12, "bold"), bg="orange", fg="black", width=15).grid(row=0, column=1, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Net Pay\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15).grid(row=0, column=2, sticky="nsew", padx=2)

        tk.Button(billing_info, text="Print", font=("times new roman", 11), bg="white").grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Clear All", font=("times new roman", 11), bg="lightblue").grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("times new roman", 11), bg="pink").grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

        for i in range(3):
            billing_info.grid_columnconfigure(i, weight=1)

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryBillingSystem(root)
    root.mainloop()



import tkinter as tk
from tkinter import ttk

class InventoryBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1200x600")
        self.root.minsize(1000, 500)

        # Make all 3 columns equal in size
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

        tk.Label(self.left_frame, text="All products", font=("times new roman", 22, "bold"), fg="white", bg="#000066").pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=5, pady=5)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 13, "bold"), fg="red").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        tk.Button(search_frame, text="Search All", font=("times new roman", 13, "bold"), bg="#d6eaf8").grid(row=0, column=1, padx=10)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 12)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(search_frame, font=("times new roman", 12), width=20, bg="lightyellow").grid(row=1, column=1, padx=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 12, "bold"), bg="#aed6f1").grid(row=1, column=2, padx=10)

        # Product table
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

        # Customer Info
        top_form = tk.Frame(self.middle_frame, bg="#dcdcdc")
        top_form.pack(fill="x", padx=10, pady=5)

        tk.Label(top_form, text="Customer Name", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(top_form, width=25, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(top_form, text="Mobile No.", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        tk.Entry(top_form, width=25, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=3, padx=5, pady=5)

        # Cart Title
        tk.Label(self.middle_frame, text="Cart", font=("times new roman", 14, "bold"), bg="#dcdcdc").pack(anchor="w", padx=10, pady=5)

        # Cart Table
        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)

        # Product Entry Section (Updated position)
        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", pady=10)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(entry_frame, width=18, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        tk.Entry(entry_frame, width=10, font=("times new roman", 12)).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        tk.Entry(entry_frame, width=10, font=("times new roman", 12), bg="lightyellow").grid(row=0, column=5, padx=5, pady=5)

        tk.Label(entry_frame, text="In Stock", font=("times new roman", 12), bg="#dcdcdc").grid(row=0, column=6, padx=5, pady=5, sticky="w")
        tk.Label(entry_frame, text="XX", font=("times new roman", 12), bg="#f0f0f0", width=6).grid(row=0, column=7, padx=5, pady=5)

        # Action Buttons
        button_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        button_frame.pack(fill="x", padx=10)

        tk.Button(button_frame, text="Clear", font=("times new roman", 11), bg="lightgray", width=10).pack(side="left", padx=5)
        tk.Button(button_frame, text="Add|Update Cart", font=("times new roman", 11, "bold"), bg="orange", width=20).pack(side="left", padx=5)

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

        tk.Label(billing_info, text="Bill Amount\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15).grid(row=0, column=0, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Discount %\n0", font=("times new roman", 12, "bold"), bg="orange", fg="black", width=15).grid(row=0, column=1, sticky="nsew", padx=2)
        tk.Label(billing_info, text="Net Pay\n[0]", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=15).grid(row=0, column=2, sticky="nsew", padx=2)

        tk.Button(billing_info, text="Print", font=("times new roman", 11), bg="white").grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Clear All", font=("times new roman", 11), bg="lightblue").grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("times new roman", 11), bg="pink").grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

        for i in range(3):
            billing_info.grid_columnconfigure(i, weight=1)

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryBillingSystem(root)
    root.mainloop()















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
        self.root.minsize(800, 600)
        self.f = Functions.function()
        self.root.wm_attributes("-topmost", True)
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
        navbar = tk.Frame(self.root, bg="#333", height=50)
        navbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
        for i in range(5):
            navbar.grid_columnconfigure(i, weight=1)

        nav_buttons = ["Home", "Products", "Cart", "Billing", "Logout"]
        for i, btn in enumerate(nav_buttons):
            tk.Button(navbar, text=btn, bg="#555", fg="white",
                      font=("times new roman", 12, "bold"), bd=0).grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.left_frame, text="All Products", font=("times new roman", 30, "bold"),
                          fg="white", bg="#000066")
        header.pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=3, pady=10)

        for i in range(3):
            search_frame.grid_columnconfigure(i, weight=1)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 18, "bold"), fg="red", width=35, anchor="w", padx=2, pady=5).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        tk.Button(search_frame, text="Search All", font=("times new roman", 15, "bold"), width=17, padx=2, pady=2, bg="#d6eaf8", command=self.Billsecton_search_all).grid(row=0, column=2, sticky="e", padx=5, pady=5)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 17), width=16, anchor="w").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        self.Search_Name_Entry = tk.Entry(search_frame, font=("times new roman", 15), bg="lightyellow")
        self.Search_Name_Entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 15, "bold"), bg="#aed6f1", command=self.Billsection_search).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        product_frame = tk.Frame(self.left_frame)
        product_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
        self.product_table.pack(fill="both", expand=True)
        self.product_table.bind('<ButtonRelease-1>', self.Billsection_get_data)  # Bind the selection event

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#dcdcdc")
        self.middle_frame.grid(row=1, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.middle_frame, text="Customer Detail", font=("times new roman", 27, "bold"), bg="#c0c0c0").pack(fill="x")

        top_form = tk.Frame(self.middle_frame, bg="#dcdcdc")
        top_form.pack(fill="x", padx=10, pady=5)

        for i in range(4):
            top_form.grid_columnconfigure(i, weight=1)

        tk.Label(top_form, text="Name", font=("times new roman", 15), bg="#dcdcdc", width=11).grid(row=0, column=0, sticky="w", padx=1, pady=5)
        self.Custumer_Name_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_Name_E.grid(row=0, column=1, sticky="ew", padx=3, pady=5)

        tk.Label(top_form, text="Contact", font=("times new roman", 15), bg="#dcdcdc", width=12).grid(row=0, column=2, sticky="w", padx=3, pady=5)
        self.Custumer_contact_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_contact_E.grid(row=0, column=3, sticky="ew", padx=3, pady=5)
        
        self.cart = Label(self.middle_frame, text="Cart \tTotal Products\t[0]", font=("times new roman", 14, "bold"), bg="#dcdcdc",fg="black" ,justify="left")
        self.cart.pack(anchor="w", padx=10, pady=3)

        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)
        self.cart_table.bind("<ButtonRelease-1>", self.get_cart_data)

        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", padx=10, pady=10)

        for i in range(6):
            entry_frame.grid_columnconfigure(i, weight=1)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        self.p_name_Entry = ttk.Entry(entry_frame,state="readonly", font=("times new roman", 18))
        self.p_name_Entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=2, sticky="w", padx=5, pady=3)
        self.price_perqty_Entry = ttk.Entry(entry_frame, font=("times new roman", 18),state="readonly")
        self.price_perqty_Entry.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=4, sticky="w", padx=5, pady=3)
        self.Quantity_Entry = tk.Entry(entry_frame, font=("times new roman", 18), bg="lightyellow")
        self.Quantity_Entry.grid(row=1, column=4, sticky="ew", padx=5, pady=5)

        button_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        button_frame.pack(fill="x", padx=10, pady=5)

        self.Instock_label = tk.Label(button_frame, text="In Stock[0]", font=("times new roman", 18), bg="#dcdcdc", anchor="w")
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
        mytuple = (self.root, self.cart_table, self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Instock_label)
        self.f.get_cart_data(mytuple)

if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()




    import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import string
import sqlite3
import time
import os
import tempfile
import Functions

class Billing_area:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1200x650")
        self.root.minsize(800, 600)
        self.f = Functions.function()
        #root.overrideredirect(True)
        self.root.wm_attributes("-topmost",True)
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
        navbar = tk.Frame(self.root, bg="#333", height=50)
        navbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
        for i in range(5):
            navbar.grid_columnconfigure(i, weight=1)

        nav_buttons = ["Home", "Products", "Cart", "Billing", "Logout"]
        for i, btn in enumerate(nav_buttons):
            tk.Button(navbar, text=btn, bg="#555", fg="white",
                      font=("times new roman", 12, "bold"), bd=0).grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.left_frame, text="All Products", font=("times new roman", 30, "bold"),
                 fg="white", bg="#000066")
        header.pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x",padx=3, pady=10)

        for i in range(3):
            search_frame.grid_columnconfigure(i, weight=1)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 18, "bold"), fg="red",width=35,anchor="w",padx=2,pady=5).grid(row=0, column=0,columnspan=2 ,sticky="w", pady=5)
        tk.Button(search_frame, text="Search All", font=("times new roman", 15, "bold" ),width=17,padx=2,pady=2,  bg="#d6eaf8").grid(row=0, column=2, sticky="e", padx=5, pady=5)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 17),width=16,anchor="w").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        tk.Entry(search_frame, font=("times new roman", 15), bg="lightyellow",).grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 15, "bold"),bg="#aed6f1").grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        product_frame = tk.Frame(self.left_frame)
        product_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
        self.product_table.pack(fill="both", expand=True)

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#dcdcdc")
        self.middle_frame.grid(row=1, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.middle_frame, text="Customer Detail", font=("times new roman", 27, "bold"), bg="#c0c0c0").pack(fill="x")

        top_form = tk.Frame(self.middle_frame, bg="#dcdcdc")
        top_form.pack(fill="x", padx=10, pady=5)

        for i in range(4):
            top_form.grid_columnconfigure(i, weight=1)

        tk.Label(top_form, text="Name", font=("times new roman", 15), bg="#dcdcdc",width=11).grid(row=0, column=0, sticky="w", padx=1, pady=5)
        tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow").grid(row=0, column=1, sticky="ew", padx=3, pady=5)

        tk.Label(top_form, text="Contact", font=("times new roman", 15), bg="#dcdcdc" ,width=12).grid(row=0, column=2, sticky="w", padx=3, pady=5)
        tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow").grid(row=0, column=3, sticky="ew", padx=3, pady=5)

        tk.Label(self.middle_frame, text="Cart", font=("times new roman", 14, "bold"), bg="#dcdcdc").pack(anchor="w", padx=10, pady=3)

        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)

        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", padx=10, pady=10)

        for i in range(6):
            entry_frame.grid_columnconfigure(i, weight=1)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        tk.Entry(entry_frame, font=("times new roman", 18), bg="lightyellow").grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=2, sticky="w", padx=5, pady=3)
        tk.Entry(entry_frame, font=("times new roman", 18)).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=4, sticky="w", padx=5, pady=3)
        tk.Entry(entry_frame, font=("times new roman", 18), bg="lightyellow").grid(row=1, column=4, sticky="ew", padx=5, pady=5)

        button_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        button_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(button_frame, text="In Stock[0]", font=("times new roman", 18), bg="#dcdcdc",anchor="w").pack(side="left", padx=5, pady=5)
        tk.Button(button_frame, text="Clear", font=("times new roman", 16), bg="lightgray",padx=10).pack(side="left", padx=5, pady=5)
        tk.Button(button_frame, text="Add|Update Cart", font=("times new roman", 15, "bold"), padx=5, bg="orange", width=25).pack(side="left", padx=5, pady=5)

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

        tk.Label(billing_info, text="Bill Amount\n[0]", font=("times new roman", 15, "bold"), bg="blue", fg="white").grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        discount_frame = tk.Frame(billing_info, bg="orange")
        discount_frame.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        tk.Label(discount_frame, text="Discount %", font=("times new roman", 15, "bold"), bg="orange",fg="white").pack(anchor="center")
        self.Discount_Entry = tk.Entry(discount_frame, font=("times new roman", 12), width=8)
        self.Discount_Entry.pack(anchor="center", padx=5, pady=2)        
        tk.Label(billing_info, text="Net Pay\n[0]", font=("times new roman", 15, "bold"), bg="blue", fg="white").grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

        tk.Button(billing_info, text="Print", font=("times new roman", 15), bg="white").grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Clear All", font=("times new roman", 15), bg="lightblue").grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        tk.Button(billing_info, text="Generate\nSave Bill", font=("times new roman", 15), bg="pink").grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()





#updated correct responsive 
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
        self.root.minsize(800, 600)
        self.f = Functions.function()
        self.root.wm_attributes("-topmost", True)
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
        navbar = tk.Frame(self.root, bg="#333", height=50)
        navbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
        for i in range(5):
            navbar.grid_columnconfigure(i, weight=1)

        nav_buttons = ["Home", "Products", "Cart", "Billing", "Logout"]
        for i, btn in enumerate(nav_buttons):
            tk.Button(navbar, text=btn, bg="#555", fg="white",
                      font=("times new roman", 12, "bold"), bd=0).grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

    def create_left_frame(self):
        self.left_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.left_frame.grid(row=1, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.left_frame, text="All Products", font=("times new roman", 30, "bold"),
                          fg="white", bg="#000066")
        header.pack(fill="x")

        search_frame = tk.Frame(self.left_frame, bd=2, relief=tk.RIDGE)
        search_frame.pack(fill="x", padx=3, pady=10)

        for i in range(3):
            search_frame.grid_columnconfigure(i, weight=1)

        tk.Label(search_frame, text="Search Product | By Name", font=("times new roman", 18, "bold"), fg="red", width=35, anchor="w", padx=2, pady=5).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        tk.Button(search_frame, text="Search All", font=("times new roman", 15, "bold"), width=17, padx=2, pady=2, bg="#d6eaf8", command=self.Billsecton_search_all).grid(row=0, column=2, sticky="e", padx=5, pady=5)

        tk.Label(search_frame, text="Product Name", font=("times new roman", 17), width=16, anchor="w").grid(row=1, column=0, sticky="w", padx=2, pady=5)
        self.Search_Name_Entry = tk.Entry(search_frame, font=("times new roman", 15), bg="lightyellow")
        self.Search_Name_Entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        tk.Button(search_frame, text="Search", font=("times new roman", 15, "bold"), bg="#aed6f1", command=self.Billsection_search).grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        product_frame = tk.Frame(self.left_frame)
        product_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.product_table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"), show="headings")
        for col in self.product_table["columns"]:
            self.product_table.heading(col, text=col.upper())
        self.product_table.pack(fill="both", expand=True)
        self.product_table.bind('<ButtonRelease-1>', self.Billsection_get_data)  # Bind the selection event

    def create_middle_frame(self):
        self.middle_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE, bg="#dcdcdc")
        self.middle_frame.grid(row=1, column=1, sticky="nsew")
        self.middle_frame.grid_rowconfigure(1, weight=1)
        self.middle_frame.grid_columnconfigure(0, weight=1)

        tk.Label(self.middle_frame, text="Customer Detail", font=("times new roman", 27, "bold"), bg="#c0c0c0").pack(fill="x")

        top_form = tk.Frame(self.middle_frame, bg="#dcdcdc")
        top_form.pack(fill="x", padx=10, pady=5)

        for i in range(4):
            top_form.grid_columnconfigure(i, weight=1)

        tk.Label(top_form, text="Name", font=("times new roman", 15), bg="#dcdcdc", width=11).grid(row=0, column=0, sticky="w", padx=1, pady=5)
        self.Custumer_Name_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_Name_E.grid(row=0, column=1, sticky="ew", padx=3, pady=5)

        tk.Label(top_form, text="Contact", font=("times new roman", 15), bg="#dcdcdc", width=12).grid(row=0, column=2, sticky="w", padx=3, pady=5)
        self.Custumer_contact_E = tk.Entry(top_form, font=("times new roman", 15), bg="lightyellow")
        self.Custumer_contact_E.grid(row=0, column=3, sticky="ew", padx=3, pady=5)
        
        self.cart = Label(self.middle_frame, text="Cart \tTotal Products\t[0]", font=("times new roman", 14, "bold"), bg="#dcdcdc",fg="black" ,justify="left")
        self.cart.pack(anchor="w", padx=10, pady=3)

        cart_frame = tk.Frame(self.middle_frame)
        cart_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), show="headings")
        for col in self.cart_table["columns"]:
            self.cart_table.heading(col, text=col.upper())
        self.cart_table.pack(fill="both", expand=True)
        self.cart_table.bind("<ButtonRelease-1>", self.get_cart_data)

        entry_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        entry_frame.pack(fill="x", padx=10, pady=10)

        for i in range(6):
            entry_frame.grid_columnconfigure(i, weight=1)

        tk.Label(entry_frame, text="Product Name", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        self.p_name_Entry = ttk.Entry(entry_frame,state="readonly", font=("times new roman", 18))
        self.p_name_Entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Price per Qty", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=2, sticky="w", padx=5, pady=3)
        self.price_perqty_Entry = ttk.Entry(entry_frame, font=("times new roman", 18),state="readonly")
        self.price_perqty_Entry.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        tk.Label(entry_frame, text="Quantity", font=("times new roman", 15), bg="#dcdcdc").grid(row=0, column=4, sticky="w", padx=5, pady=3)
        self.Quantity_Entry = tk.Entry(entry_frame, font=("times new roman", 18), bg="lightyellow")
        self.Quantity_Entry.grid(row=1, column=4, sticky="ew", padx=5, pady=5)

        button_frame = tk.Frame(self.middle_frame, bg="#dcdcdc")
        button_frame.pack(fill="x", padx=10, pady=5)

        self.Instock_label = tk.Label(button_frame, text="In Stock[0]", font=("times new roman", 18), bg="#dcdcdc", anchor="w")
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
        mytuple = (self.root, self.cart_table, self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Instock_label)
        self.f.get_cart_data(mytuple)

if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()

    #update2
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
        self.root.minsize(800, 600)
        self.f = Functions.function()
        self.root.wm_attributes("-topmost", True)
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
        navbar = tk.Frame(self.root, bg="#333", height=50)
        navbar.grid(row=0, column=0, columnspan=3, sticky="nsew")
        for i in range(5):
            navbar.grid_columnconfigure(i, weight=1)

        nav_buttons = ["Home", "Products", "Cart", "Billing", "Logout"]
        for i, btn in enumerate(nav_buttons):
            tk.Button(navbar, text=btn, bg="#555", fg="white",
                      font=("times new roman", 12, "bold"), bd=0).grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

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

        y_scroll = ttk.Scrollbar(self.cart_table, orient="vertical", command=self.product_table.yview)
        x_scroll = ttk.Scrollbar(self.cart_table, orient="horizontal", command=self.product_table.xview)
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
        mytuple = (self.root, self.cart_table, self.price_perqty_Entry, self.p_name_Entry, self.pid, self.Instock_label)
        self.f.get_cart_data(mytuple)

if __name__ == "__main__":
    root = tk.Tk()
    app = Billing_area(root)
    root.mainloop()





from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar
import string
from datetime import datetime
import Functions
from suplyre import SupplyreClass

class page2:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f0f0f0")
        self.f = Functions.function()
        
        self.lbl = None
        self.lbl1 = None
        
        self.root.wm_attributes("-topmost", True)
        self.root.focus_force()

        # Search Frame
        self.create_search_frame()
        
        # Employee Details Frame
        self.create_employee_details_frame()
        
        # Employee Form Fields
        self.create_employee_form()
        
        # Buttons
        self.create_buttons()
        
        # Table
        self.create_table()
        
        self.generateeId()
        self.show_data(self.frameTreaview)

    def create_search_frame(self):
        self.frame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 20, "bold"), bd=3, bg="#e6e6e6")
        self.frame.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.12)
        
        self.searchby = ttk.Combobox(self.frame, values=("Select", "Email", "name", "contact"), state="readonly", justify=CENTER, font=("arial", 15, "bold"))
        self.searchby.place(relx=0.02, rely=0.25, relwidth=0.2)
        self.searchby.current(0)
        
        self.search1 = ttk.Entry(self.frame, font=("arial", 15, "bold"))
        self.search1.place(relx=0.3, rely=0.25, relwidth=0.4)
        
        btn_Search = Button(self.frame, text="Search", command=self.Search_data, bg="#4caf50", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Search.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.8)

        btn_Back = Button(self.frame, text="Back", command=self.root.destroy, bg="#609d8b", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Back.place(relx=0.86, rely=0.1, relwidth=0.1, relheight=0.8)

    
    def create_employee_details_frame(self):
        self.frame2 = Label(self.root, text="Employee Details", font=("times new roman", 20, "bold"), bg="#333", fg="white")
        self.frame2.place(relx=0.03, rely=0.16, relwidth=0.94, relheight=0.05)
    
    def create_employee_form(self):
        labels = ["Emp No.", "Name", "Email", "Gender", "Contact No.", "D.O.B.", "D.O.J.", "Password", "User Type", "Address", "Salary"]
        positions = [
            (0.0001, 0.23), (0.0001, 0.35), (0.0001, 0.47),
            (0.33, 0.23), (0.66, 0.23),
            (0.33, 0.35), (0.66, 0.35),
            (0.332, 0.47), (0.66, 0.47),
            (0.0001, 0.59), (0.33, 0.59)
        ]
        
        self.entries = {}
        for i, label in enumerate(labels):
            lbl = Label(self.root, text=label, font=("times new roman", 14, "bold"), bg="#f0f0f0")
            lbl.place(relx=positions[i][0], rely=positions[i][1], relwidth=0.12, relheight=0.04)
            
            if label in ["Gender", "User Type"]:
                values = ("Select", "Male", "Female") if label == "Gender" else ("Admin", "Employee")
                entry = ttk.Combobox(self.root, values=values, state="readonly", justify=CENTER, font=("arial", 12, "bold"))
                entry.current(0)
            elif label in ["D.O.B.", "D.O.J."]:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"), state="readonly")
                entry.bind("<Button-1>", self.Show_caleder_dob if label == "D.O.B." else self.Show_caleder_doj)
            elif label == "Address":
                entry = Text(self.root, font=("arial", 12, "bold"))
            else:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"))
            
            entry.place(relx=positions[i][0] + 0.15, rely=positions[i][1], relwidth=0.18, relheight=0.04)
            self.entries[label] = entry
    
    def create_buttons(self):
        colors = ["#2196F3", "#4CAF50", "#f44336", "#FFC107"]
        texts = ["Save", "Update", "Delete", "Clear"]
        commands = [self.ad_data, self.Update_data, self.Delete, self.clear_data]
        
        for i in range(4):
            btn = Button(self.root, text=texts[i], command=commands[i], bg=colors[i], fg="white", font=("times new roman", 12, "bold"), cursor="hand2", relief=RAISED)
            btn.place(relx=0.42 + i*0.14, rely=0.64, relwidth=0.13, relheight=0.05)
    
    def create_table(self):
        self.frame3 = Frame(self.root, bg="white")
        self.frame3.place(relx=0.03, rely=0.7, relwidth=0.94, relheight=0.25)
        
        self.scrolly = Scrollbar(self.frame3, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3, orient=HORIZONTAL)
        
        self.frameTreaview = ttk.Treeview(self.frame3,columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrollx.config(command=self.frameTreaview.xview)
        self.scrolly.config(command=self.frameTreaview.yview)
        
        for col in self.frameTreaview["columns"]:
            self.frameTreaview.heading(col, text=col.upper())
            self.frameTreaview.column(col, width=120)
        
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.pack(fill=BOTH, expand=1)
        self.frameTreaview.bind("<ButtonRelease-1>", self.Get_Data)
        self.data_tuple =  (self.root, self.entries["Emp No."], self.entries["Name"], self.entries["Email"], self.entries["Gender"], self.entries["Contact No."],self.entries["D.O.B."], self.entries["D.O.J."], 
            self.entries["Password"], self.entries["User Type"], self.entries["Address"], self.entries["Salary"], self.frameTreaview)

    def ad_data(self):self.f.add(self.data_tuple)
    def clear_data(self): self.f.clear(self.data_tuple)
    def show_data(self, frameTreaview): self.f.show(frameTreaview, self.root)
    def generateeId(self): self.f.generateeid((self.entries["Emp No."],))
    def Get_Data(self, event=None):
        region = self.frameTreaview.identify_region(event.x, event.y)
        row_id = self.frameTreaview.identify_row(event.y)
        if region != "cell" or not row_id:
            return
        self.f.get_data(self.data_tuple)
    def Update_data(self): self.f.update(self.data_tuple)
    def Delete(self): self.f.delete(self.data_tuple)
    def Search_data(self): self.f.search((self.root, self.search1, self.searchby, self.frameTreaview))

    def Show_caleder_dob(self, event=None): 
        if not self.lbl or not self.lbl.winfo_exists():
            self.lbl = Label(self.root,bg="white")
        x = self.entries['D.O.B.'].winfo_x()
        y = self.entries['D.O.B.'].winfo_y() + self.entries["D.O.B."].winfo_height() + 5
        self.lbl.place(x=x, y=y, width=200, height=300)
        self.f.show_calendar((self.entries["D.O.B."], self.root), self.lbl)

    def Show_caleder_doj(self, event=None):
        if not self.lbl1 or not self.lbl1.winfo_exists():
            self.lbl1 = Label(self.root, bg="white")
        x = self.entries["D.O.J."].winfo_x()
        y = self.entries["D.O.J."].winfo_y() + self.entries["D.O.J."].winfo_height() + 5
        self.lbl1.place(x=x, y=y, width=260, height=300)
        self.f.show_calendar_doj((self.entries["D.O.J."], self.root), self.lbl1)
    

if __name__ == "__main__":
    root = Tk()
    obj = page2(root)
    root.mainloop()

# Employee update
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar
import string
from datetime import datetime
import Functions
from suplyre import SupplyreClass

class page2:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1335x615+200+135")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f0f0f0")
        self.f = Functions.function()
        
        self.lbl = None
        self.lbl1 = None
        
        self.root.wm_attributes("-topmost", True)
        self.root.focus_force()

        # Search Frame
        self.create_search_frame()
        
        # Employee Details Frame
        self.create_employee_details_frame()
        
        # Employee Form Fields
        self.create_employee_form()
        
        # Buttons
        self.create_buttons()
        
        # Table
        self.create_table()
        
        self.generateeId()
        self.create_navbar()
        self.show_data(self.frameTreaview)

    def create_navbar(self):
        navbar = Frame(self.root, bg="#222", height=55)
        navbar.pack(fill=X)

        title = Label(navbar, bg="#222", fg="white",
                      font=("Helvetica", 18, "bold"))
        title.pack(side=LEFT, padx=20)

        btn_config = [
            ("Home", None),
            ("Employee", None),
            ("Categories", None),
            ("Billing", None),
            ("Product", None),
            ("Sales", None),
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=8)

    def create_search_frame(self):
        self.frame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 20, "bold"), bd=3, bg="#e6e6e6")
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.11)

        
        self.searchby = ttk.Combobox(self.frame, values=("Select", "Email", "name", "contact"), state="readonly", justify=CENTER, font=("arial", 15, "bold"))
        self.searchby.place(relx=0.02, rely=0.20, relwidth=0.2)
        self.searchby.current(0)
        
        self.search1 = ttk.Entry(self.frame, font=("arial", 15, "bold"))
        self.search1.place(relx=0.3, rely=0.25, relwidth=0.4)
        
        btn_Search = Button(self.frame, text="Search", command=self.Search_data, bg="#4caf50", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Search.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.8)

        btn_Back = Button(self.frame, text="Back", command=self.root.destroy, bg="#609d8b", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Back.place(relx=0.86, rely=0.1, relwidth=0.1, relheight=0.8)

    
    def create_employee_details_frame(self):
        self.frame2 = Label(self.root, text="Employee Details", font=("times new roman", 20, "bold"), bg="#333", fg="white")
        self.frame2.place(relx=0.03, rely=0.17, relwidth=0.94, relheight=0.05)
    
    def create_employee_form(self):
        labels = ["Emp No.", "Name", "Email", "Gender", "Contact No.", "D.O.B.", "D.O.J.", "Password", "User Type", "Address", "Salary"]
        positions = [
            (0.0001, 0.23), (0.0001, 0.35), (0.0001, 0.47),
            (0.33, 0.23), (0.66, 0.23),
            (0.33, 0.35), (0.66, 0.35),
            (0.332, 0.47), (0.66, 0.47),
            (0.0001, 0.59), (0.33, 0.59)
        ]
        
        self.entries = {}
        for i, label in enumerate(labels):
            lbl = Label(self.root, text=label, font=("times new roman", 14, "bold"), bg="#f0f0f0")
            lbl.place(relx=positions[i][0], rely=positions[i][1], relwidth=0.12, relheight=0.04)
            
            if label in ["Gender", "User Type"]:
                values = ("Select", "Male", "Female") if label == "Gender" else ("Admin", "Employee")
                entry = ttk.Combobox(self.root, values=values, state="readonly", justify=CENTER, font=("arial", 12, "bold"))
                entry.current(0)
            elif label in ["D.O.B.", "D.O.J."]:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"), state="readonly")
                entry.bind("<Button-1>", self.Show_caleder_dob if label == "D.O.B." else self.Show_caleder_doj)
            elif label == "Address":
                entry = Text(self.root, font=("arial", 12, "bold"))
            else:
                entry = ttk.Entry(self.root, font=("arial", 12, "bold"))
            
            entry.place(relx=positions[i][0] + 0.15, rely=positions[i][1], relwidth=0.18, relheight=0.04)
            self.entries[label] = entry
    
    def create_buttons(self):
        colors = ["#2196F3", "#4CAF50", "#f44336", "#FFC107"]
        texts = ["Save", "Update", "Delete", "Clear"]
        commands = [self.ad_data, self.Update_data, self.Delete, self.clear_data]
        
        for i in range(4):
            btn = Button(self.root, text=texts[i], command=commands[i], bg=colors[i], fg="white", font=("times new roman", 12, "bold"), cursor="hand2", relief=RAISED)
            btn.place(relx=0.42 + i*0.14, rely=0.64, relwidth=0.13, relheight=0.05)
    
    def create_table(self):
        self.frame3 = Frame(self.root, bg="white")
        self.frame3.place(relx=0.03, rely=0.7, relwidth=0.94, relheight=0.25)
        
        self.scrolly = Scrollbar(self.frame3, orient=VERTICAL)
        self.scrollx = Scrollbar(self.frame3, orient=HORIZONTAL)
        
        self.frameTreaview = ttk.Treeview(
            self.frame3,
            columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"),
            yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set
        )
        
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.scrollx.pack(side=BOTTOM, fill=X)
        self.scrollx.config(command=self.frameTreaview.xview)
        self.scrolly.config(command=self.frameTreaview.yview)
        
        for col in self.frameTreaview["columns"]:
            self.frameTreaview.heading(col, text=col.upper())
            self.frameTreaview.column(col, width=120)
        
        self.frameTreaview["show"] = "headings"
        self.frameTreaview.pack(fill=BOTH, expand=1)
        self.frameTreaview.bind("<ButtonRelease-1>", self.Get_Data)
        self.data_tuple =  (
            self.root,
            self.entries["Emp No."],
            self.entries["Name"],
            self.entries["Email"],
            self.entries["Gender"],
            self.entries["Contact No."],
            self.entries["D.O.B."],
            self.entries["D.O.J."],
            self.entries["Password"],
            self.entries["User Type"],
            self.entries["Address"],
            self.entries["Salary"],
            self.frameTreaview
        )

    def ad_data(self):self.f.add(self.data_tuple)
    def clear_data(self): self.f.clear(self.data_tuple)
    def show_data(self, frameTreaview): self.f.show(frameTreaview, self.root)
    def generateeId(self): self.f.generateeid((self.entries["Emp No."],))
    def Get_Data(self, event=None):self.f.get_data(self.data_tuple)
    def Update_data(self): self.f.update(self.data_tuple)
    def Delete(self): self.f.delete(self.data_tuple)
    def Search_data(self): self.f.search((self.root, self.search1, self.searchby, self.frameTreaview))

    def Show_caleder_dob(self, event=None): 
        if not self.lbl or not self.lbl.winfo_exists():
            self.lbl = Label(self.root,bg="white")
        x = self.entries['D.O.B.'].winfo_x()
        y = self.entries['D.O.B.'].winfo_y() + self.entries["D.O.B."].winfo_height() + 5
        self.lbl.place(x=x, y=y, width=200, height=300)
        self.f.show_calendar((self.entries["D.O.B."], self.root), self.lbl)

    def Show_caleder_doj(self, event=None):
        if not self.lbl1 or not self.lbl1.winfo_exists():
            self.lbl1 = Label(self.root, bg="white")
        x = self.entries["D.O.J."].winfo_x()
        y = self.entries["D.O.J."].winfo_y() + self.entries["D.O.J."].winfo_height() + 5
        self.lbl1.place(x=x, y=y, width=260, height=300)
        self.f.show_calendar_doj((self.entries["D.O.J."], self.root), self.lbl1)
    

if __name__ == "__main__":
    root = Tk()
    obj = page2(root)
    root.mainloop()