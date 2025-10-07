from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
import time 
import os
from PIL import Image, ImageTk
class Sales:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1335x615+200+135")
        self.root.title("Inventory Management System")
        self.tittle = Label(self.root,bg= "black",text="Custumer Bill Reports ",height=10,justify="center",font=("goudy old style",25,"bold"),fg = "white" ).pack(fill="x",padx=(10,10),pady=(10,500), side="top")
        self.Invoice_Entry = Label(self.root , text="Invoice No." , font=("times new roman",20,"bold") ,)
        self.Invoice_Entry.place(x=60,y=135 )
        self.Name_Entry = Entry(self.root,font=("arial",15,"bold"),bd=2,bg="lightyellow")         
        self.Name_Entry.place(x=230,y=130,width=270,height=40)
        btn_add = Button(self.root , text="Search" ,relief="solid",command=self.search,border=1,highlightthickness=1,padx=20,pady=10, bg="light blue",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=535 , y=130 , height=40 , width=100)
        btn_update = Button(self.root , text="Clear",padx=20,pady=10,relief="solid",border=1,highlightthickness=2 ,bg="light pink",font=("times new roman"  , 20 ,"bold" ),cursor="hand2").place(x=650 , y=130 , height=40 , width=100)
        

        self.Listframe = Frame(self.root,relief=RIDGE  , bg="white",bd=3 )
        self.Listframe.place(x=60,y=180,width=300,height=430 )
        self.scrolly = Scrollbar(self.Listframe , orient=VERTICAL)
        self.listbox = Listbox(self.Listframe , bg="white" ,font=("goudy old style",18,"bold"),yscrollcommand=self.scrolly.set)
        self.scrolly.pack(fill=Y,side="right")
        self.scrolly.config(command=self.listbox.yview )
        self.listbox.pack(fill=BOTH,expand=1)
        self.listbox.bind("<ButtonRelease-1>",self.get_data)

        self.Billframe = Label(self.root,bd=2,bg="white")
        self.Billframe.place(x=380,y=181,height=430,width=500)
        self.billlabel = Label(self.Billframe,text="Bill Area",height=-10,bg="darkblue",fg="white",font=("goudy old style",20,"bold"))
        self.billlabel.pack(fill="x",side=TOP)
        self.billscrollbar = Scrollbar(self.Billframe,orient=VERTICAL)
        self.billtextarea = Text(self.Billframe,bg="lightyellow",font=("goudy old style",15,"bold"),state=DISABLED,bd=2,fg="black",yscrollcommand=self.billscrollbar.set)
        self.billscrollbar.pack(fill=Y,side=RIGHT)
        self.billscrollbar.config(command=self.billtextarea.yview)
        self.billtextarea.pack(fill=BOTH,expand=1)

        self.bill_photo = Image.open("pics/p1.jpg")
        self.bill_photo = self.bill_photo.resize((430,430),Image.LANCZOS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        self.lbl = Label(self.root,image=self.bill_photo)
        self.lbl.place(x=890,y=180)
        self.show()

#**********************************Function*****************************************************
    def show(self):
        self.listbox.delete(0,END)
        for i in os.listdir('Bills'):
            if i.split(".")[1] == "txt":
                self.listbox.insert(END,i)


    def search(self):
        for i in os.listdir('Bills'):
            if i.split(".")[0] == self.Name_Entry.get():
                self.listbox.delete(0,END)
                self.listbox.insert(0,i)
                break
            

    def get_data(self,ev):
        self.billtextarea.config(state=NORMAL)
        a = self.listbox.curselection() 
        self.file_name  = self.listbox.get(a)
        self.file_data = open(f'Bills/{self.file_name}','r')
        self.billtextarea.delete("0.1",END)
        self.billdata = self.file_data.read()
        self.billtextarea.insert(END,self.billdata)
        self.billtextarea.config(state=DISABLED)
        self.file_data.close()




if __name__=="__main__":
    root=Tk()
    obj = Sales(root)
    root.mainloop()

# Updated page1.py code 


# FileName: MultipleFiles/Page1.py
# FileContents:
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
        self.root.minsize(1000, 600)
        self.root.resizable(False,False)
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
        Button(top_frame, text="Logout", bg="skyblue", font=("times new roman", 20, "bold"), cursor="hand2", command=self.logout).pack(side=RIGHT, padx=10) # Added logout command
        Button(top_frame, text="Close", fg="black", bg="#FFA07A", font=("times new roman", 20, "bold"), cursor="hand2", command=self.Close).pack(side=RIGHT, padx=10)

        top_frame2 = Frame(self.root, bg="black")
        top_frame2.pack(fill=X,pady=5)
        Label(top_frame2, text="Welcome to Inventory Management System", font=("times new roman", 20, "bold"), bg="black", fg="white").pack(side=LEFT,fill=X)
        self.month= Label(top_frame2,text=f"Date {str(time.strftime('%d/%m/%y'))}\t",font=("times new roman", 20, "bold"), bg="black", fg="white")
        self.month.pack(side=RIGHT,padx=10)
        self.time=Label(top_frame2,text=f"Time ",font=("times new roman", 20, "bold"), bg="black", fg="white")
        self.time.pack(side=RIGHT,padx=10)
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
        # Destroy all child windows first
        for window in [self.page1_window, self.page2_window, self.page3_window, self.page4_window, self.page5_window, self.page6_window]:
            if window and window.winfo_exists():
                window.destroy()
        self.root.destroy() # Destroy the main root window

    def logout(self):
        import os
        if os.path.exists("session.txt"):
            os.remove("session.txt")
        self.root.destroy()
        from login import LoginPage
        new_root = Tk()
        LoginPage(new_root)
        new_root.mainloop()


    def update_time(self):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        self.current_time = time.strftime('%H:%M:%S') 
        self.month.config(text=f"Date {str(time.strftime('%d/%m/%y'))}\t")
        self.time.config(text=f"Time {str(self.current_time)}\t")
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
        self.time.after(1000,self.update_time)


    def close_all_windows(self, current_window):
        for window in [self.page1_window,self.page2_window,self.page3_window,self.page4_window,self.page5_window,self.page6_window]:
            if window and window != current_window and window.winfo_exists():
                window.destroy()
    def employee2(self):
        if self.page1_window is not None and self.page1_window.winfo_exists():
            self.page1_window.destroy()
        self.close_all_windows(self.page1_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = page2(self.newwindow)
        self.page1_window = self.newwindow
        self.page_window = self.newwindow
        
    def category(self):
        if self.page2_window is not None and self.page2_window.winfo_exists():
            self.page2_window.destroy()
        self.close_all_windows(self.page2_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Categorie(self.newwindow)
        self.page2_window = self.newwindow
        self.page_window = self.newwindow
        
    def Sales(self):
        if self.page3_window is not None and self.page3_window.winfo_exists():
            self.page3_window.destroy()
        self.close_all_windows(self.page3_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Sales(self.newwindow)
        self.page3_window = self.newwindow
        self.page_window = self.newwindow
        
    def Suplier(self):
        if self.page4_window is not None and self.page4_window.winfo_exists():
            self.page4_window.destroy()
        self.close_all_windows(self.page4_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = SupplyreClass(self.newwindow)
        self.page4_window = self.newwindow
        self.page_window = self.newwindow
        
    def product(self):
        if self.page5_window is not None and self.page5_window.winfo_exists():
            self.page5_window.destroy()
        self.close_all_windows(self.page5_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = product(self.newwindow)
        self.page5_window = self.newwindow
        self.page_window = self.newwindow
    def Bill_Area(self):
        if self.page6_window is not None and self.page6_window.winfo_exists():
            self.page6_window.destroy()
        self.close_all_windows(self.page6_window)
        self.newwindow = Toplevel(self.root)
        self.new_obj = Billing_area(self.newwindow)
        self.page6_window = self.newwindow
        self.page_window = self.newwindow
        
# The __main__ block for Page1.py should be removed or commented out,
# as the application will now start from login.py.
# if __name__=="__main__":
#     root=Tk()
#     obj = page1(root)
#     root.mainloop()



