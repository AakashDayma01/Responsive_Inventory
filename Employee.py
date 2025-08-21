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
        self.root.configure(bg="#f0f0f0")
        self.root.state('zoomed')
        self.root.minsize(1000, 600)
        self.root.overrideredirect(True)
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
        btn_config = [
            ("Home", self.root.destroy),
            ("Product Category", self.category),
            ("Suplier",self.suplyre),
            ("Product", self.product),
            ("Billing", self.Bill_Area),
            ("Sales", self.Sales),
        ]
        for name, cmd in btn_config:
            Button(navbar, text=name, bg="#333", fg="white", font=("Arial", 12, "bold"),
                   bd=0, cursor="hand2", activebackground="#555", activeforeground="white",
                   command=cmd).pack(side=LEFT, padx=15, pady=8)

    def create_search_frame(self):
        self.frame = LabelFrame(self.root, text="Search Employee", font=("times new roman", 20, "bold"), bd=3, bg="#e6e6e6")
        self.frame.place(relx=0.05, rely=0.06, relwidth=0.9, relheight=0.13)

        self.searchby = ttk.Combobox(self.frame, values=("Select", "Email", "name", "contact"), state="readonly", justify=CENTER, font=("arial", 15, "bold"))
        self.searchby.place(relx=0.07, rely=0.25, relwidth=0.2)
        self.searchby.current(0)
        
        self.search1 = ttk.Entry(self.frame, font=("arial", 15, "bold"))
        self.search1.place(relx=0.35, rely=0.25, relwidth=0.4)
        
        btn_Search = Button(self.frame, text="Search", command=self.Search_data, bg="#4caf50", fg="white", font=("times new roman", 20, "bold"), cursor="hand2", relief=RAISED)
        btn_Search.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.8)

    
    def create_employee_details_frame(self):
        self.frame2 = Label(self.root, text="Employee Details", font=("times new roman", 20, "bold"), bg="#333", fg="white")
        self.frame2.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.05)
    
    def create_employee_form(self):
        labels = ["Emp No.", "Name", "Email", "Gender", "Contact No.", "D.O.B.", "D.O.J.", "Password", "User Type", "Address", "Salary"]
        positions = [
            (0.0001, 0.26), (0.0001, 0.38), (0.0001, 0.49),
            (0.33, 0.26), (0.66, 0.26),
            (0.33, 0.38), (0.66, 0.38),
            (0.332, 0.49), (0.66, 0.49),
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

    def suplyre(self):
        from suplyre import SupplyreClass
        new_root = Tk()
        self.new_obj = SupplyreClass(new_root)
        self.root.destroy()
 
    def category(self):
        from Category import Categorie
        new_root = Tk()
        self.new_obj = Categorie(new_root)
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