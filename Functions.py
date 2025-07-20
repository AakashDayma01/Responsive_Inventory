from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar
import string
from datetime import datetime
import time
import os
import tempfile
class function:
    def __init__(self):
        self.file_print = 0
        self.lbl_cal =None
        self.lbl_cal1 =None

        # def check_email(self):
    #    import re
     #   pattern =  r'\b[A-Za-z0-9._%=-]+[@]\w+[.]\w{2,3}\b'
      #  if re.search(pattern, mytuple[3].get()):
       #     return True
        #else:
         #       return False    
        
    def check_name(self,name):
       name = name.get()
       if name[0].isalpha()!=True:
           return False
       else :
           for i in name :
               if i == " " or i.isalpha()== True:
                   return True
               else:
                   return False
           


    def checkpassword(self,mytuple):
        for i in mytuple[8].get():
            a = mytuple[8].get()
            if a[0].isalpha()!=True:
                return 12
            else:
                j =  True
                if j:
                    for i in mytuple[8].get() :
                        if i.isnumeric():
                            k = True
                            if k :
                                for i in mytuple[8].get() :
                                    if i in string.punctuation:
                                        return True
            

    def check_email(self,mytuple):
        lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        number = [ "1","2","3","4","5","6","7","8","9","0"]
        Special = ["." ,"-","_"]
        other = ["!","#","$","%","^","&","*","(",")","[","]","{","}","|","/",":",";","'",'"',"?","<",">","=","+","`","~"]
        email = str(mytuple[3].get())
        sb =str(mytuple[3].get())
        if len(email)>=63:
            return False
        if sb.count("@")!=1:
            return False
        s = email.split("@")
        s1 = s[0]
        s2 = s[1]
        if len(s1)<=3:
            return False
        elif s2.count(".")!=1:
            return False
        elif s1.isnumeric():
            return False
        for i in s1:
            if i in other:
                return False
        
        
        
        domain = s2.split(".")
        d1 = domain[0]
        d2 = domain[1]
        for i in d1:
            if i in Special or i in other:
                return False
        for i in d2 :
            if i in Special and i in other:
                return False


        if len(d1)<3:
            return False
        
        elif len(d2)<2:
            return False
        elif ".." in s1 or "__" in s1 or "--" in s1 :
            return False
        elif ".-" in s1 or "._" in s1 or "-_" in s1:
            return False
        elif "-." in s1 or "_." in s1 or "_-" in s1 :
            return False    

        for i in s1:
            if i in lower:
                a= True
                if a:
                    for i in s1:
                        if i in number:
                            b= True
                        else:
                            b = True
                            for i in s1:
                                if i in Special:
                                    return True
                                else:
                                    return True
            else:
                return False    
        else:
            return TRUE         
                                    
    def add(self,mytuple):
        pass_w = mytuple[8].get()
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        dob = str(mytuple[6].get()).split('-')
        doj = str(mytuple[7].get()).split('-')
        try:
                if mytuple[1].get() =="":
                    messagebox.showerror("Error", "Employee ID must be required",parent = mytuple[0])

                elif mytuple[2].get()=="":
                    messagebox.showerror("Error","Name must be required please enter the name",parent = mytuple[0])

                elif self.check_name(mytuple[2])!=True:
                    messagebox.showerror("Error","Plese Don't use integers and special letters in name",parent = mytuple[0])
                elif mytuple[4].get() == "Select":
                    messagebox.showerror("Error","Please select the gender",parent = mytuple[0])
                elif mytuple[5].get()== "":
                    messagebox.showerror("Error","Please enter contact number",parent = mytuple[0])       
                elif mytuple[5].get().isnumeric()!=True:
                    messagebox.showerror("Error","Plese Don't use Strings and Special letters in Contact",parent = mytuple[0])
                elif len(str(mytuple[5].get()))!=10:
                    print(len(str(mytuple[5].get())))
                    messagebox.showerror("Error", "Invalid Contact Number pleaseenter correct Contact number",parent = mytuple[0])
                elif mytuple[3].get() =="":
                    messagebox.showerror("Error","Please enter Email",parent = mytuple[0])
                elif self.check_email(mytuple)!=True:
                    messagebox.showerror("Error","Invalid email please enter valid email",parent = mytuple[0])
                elif mytuple[6].get() =="":
                    messagebox.showerror("Error","please enter date of birth",parent = mytuple[0])
                elif mytuple[7].get() =="":
                    messagebox.showerror("Error","please enter date of Joining",parent = mytuple[0])
                elif mytuple[8].get()=="":
                    messagebox.showerror("Error","Please generate password using mixture of numbers and strings",parent = mytuple[0])    
                elif self.checkpassword(mytuple)==False: 
                    messagebox.showerror("Error","password must be mixture of numbers ,alphabates and special characters please create a strong password",parent = mytuple[0])
                elif len(mytuple[8].get())<6 or len(mytuple[8].get())>11:
                    messagebox.showerror("Error","the size of password must be greater than 6 and shorter than 11",parent = mytuple[0])
                elif self.checkpassword(mytuple)==12: 
                    messagebox.showerror("Error","Eror first letter must be alphabate in password",parent = mytuple[0])
                elif mytuple[11].get()=="":
                    messagebox.showerror("Error","please enter salary",parent = mytuple[0])
                elif mytuple[11].get().isnumeric()!=True:
                    messagebox.showerror("Error","please don't strings and special characters in salary",parent = mytuple[0])
                elif mytuple[10].get("0.1", END).strip()=="":
                    messagebox.showerror("Error","please enter address ",parent = mytuple[0])
                elif(int(doj[2])-int(dob[2])<18):
                    messagebox.showinfo("info","Age of employee must be more than 18 years",parent = mytuple[0])

                else:
                    cur.execute("select * from Employee where eid = ?",(mytuple[1].get(),))
                    row = cur.fetchone()
                    cur.execute("select * from Employee where email = ?",(mytuple[3].get(),))
                    row2 = cur.fetchone()
                    cur.execute("select * from Employee where utype = 'Admin'")
                    row3 = cur.fetchone()
                    if (row!= None):
                        messagebox.showerror("Error" , "This Employee id already exists , try diffrent",parent = mytuple[0])
                    elif (row2!= None):
                        messagebox.showerror("Error" , "This Emain ID already exists , try diffrent",parent = mytuple[0])
                    elif (row3!= None or row3==None):
                        if mytuple[9].get() =="Admin" and row3!=None:
                            messagebox.showerror("Error" , "User Type Admin already exists , try diffrent",parent = mytuple[1])
                        elif mytuple[9].get() == "Employee" or row3==None:
                            cur.execute("insert into Employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                    mytuple[1].get(),
                                    mytuple[2].get(),
                                    mytuple[3].get(),
                                    mytuple[4].get(),
                                    mytuple[5].get(),
                                    mytuple[6].get(),
                                    mytuple[7].get(),
                                    mytuple[8].get(),
                                    mytuple[9].get(),
                                    mytuple[10].get("0.1", END),
                                    mytuple[11].get()                   
                                ))
                            con.commit()
                            messagebox.showinfo("success" , "Employee added sucessfully",parent = mytuple[0])
                            con.close()
                            self.show(mytuple[12],mytuple[0])
                            self.clear(mytuple)
        except Exception as ex:
            messagebox.showerror("Error", f" 10 {str(ex)}",parent = mytuple[1])


    
    def show(self, frameTreaview,root):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
            cur.execute("select * from Employee")
            rows = cur.fetchall()
            frameTreaview.delete(*frameTreaview.get_children())
            for row in rows:
                frameTreaview.insert("", END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"  Error Due to: {str(ex)}",parent=root)

    def clear(self,mytuple,event = None):
        try:
            mytuple[1].config(state=WRITABLE)
            mytuple[6].config(state=WRITABLE)
            mytuple[7].config(state=WRITABLE)
            mytuple[1].delete(0, END)  
            mytuple[2].delete(0, END)  
            mytuple[3].delete(0, END)  
            mytuple[4].set("Select")  
            mytuple[4].insert(0,"Select") 
            mytuple[5].delete(0, END)  
            mytuple[6].delete(0, END)  
            mytuple[7].delete(0, END)  
            mytuple[8].delete(0, END)
            mytuple[9].set("Admin")  
            mytuple[9].insert(0,"Admin") 
            mytuple[10].delete(1.0, END)  
            mytuple[11].delete(0, END) 
            Eid_tuple = (mytuple[1],)
            self.generateeid(Eid_tuple)       
            mytuple[1].config(state="readonly")
            mytuple[6].config(state="readonly")
            mytuple[7].config(state="readonly")
        except Exception as ex:
            messagebox.showerror("Error", f" 6{str(ex)}",parent = mytuple[0])

    def generateeid(self,Eid_tuple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        cur.execute("Select * from Employee")
        row = cur.fetchone()
        if row !=None: 
            Eid_tuple[0].config(state=WRITABLE)
            con = sqlite3.connect(database="Billing_System.db")
            cur = con.cursor()
            cur.execute("SELECT MAX(eid) FROM Employee")
            result = cur.fetchone()
            c = result[0] 
            con.commit()
            c = int(c) + 1
            Eid_tuple[0].delete(0, END)
            billno = c
            Eid_tuple[0].insert(0, billno)
            Eid_tuple[0].config(state="readonly")
        else:
            Eid_tuple[0].config(state=WRITABLE)
            billno = 1001
            Eid_tuple[0].delete(0,END)
            Eid_tuple[0].insert(0, billno)
            Eid_tuple[0].config(state="readonly")

    def get_data(self,mytuple):
        self.clear(mytuple)
        try:       
            f=mytuple[12].focus()
            content = (mytuple[12].item(f))
            row=content['values']
            mytuple[1].config(state=WRITABLE)
            mytuple[6].config(state=WRITABLE)
            mytuple[7].config(state=WRITABLE)
            mytuple[1].delete(0,END)
            mytuple[1].insert(0,row[0]) 
            mytuple[2].insert(0,row[1]) 
            mytuple[3].insert(0,row[2]) 
            mytuple[4].set(row[3]) 
            mytuple[5].insert(0,row[4]) 
            mytuple[6].insert(0,row[5]) 
            mytuple[7].insert(0,row[6]) 
            mytuple[8].insert(0,row[7]) 
            mytuple[9].set(row[8]) 
            mytuple[10].delete("1.0", END) 
            mytuple[10].insert(END ,row[9]) 
            mytuple[11].insert(0,row[10])
            mytuple[1].config(state="readonly")
            mytuple[6].config(state="readonly")
            mytuple[7].config(state="readonly")
        except Exception as ex:
            messagebox.showerror("Error", f" Error due to: {str(ex)}",parent = mytuple[0])

    def update(self,mytuple):
        pass_w = mytuple[8].get()
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        dob = str(mytuple[6].get()).split('-')
        doj = str(mytuple[7].get()).split('-')
        #try:
        if mytuple[1].get() =="":
            messagebox.showerror("Error", "Employee ID must be required" , parent = mytuple[0])
        elif mytuple[2].get() =="":
            messagebox.showerror("Error","Name must be required please enter the name", parent = mytuple[0])
        elif self.check_name(mytuple[2])!=True:
            messagebox.showerror("Error","Plese Don't use integers and special letters in name", parent = mytuple[0])
        elif mytuple[4].get() == "Select":
            messagebox.showerror("Error","Please select the gender", parent = mytuple[0])
        elif mytuple[5].get() == "":
            messagebox.showerror("Error","Please enter contact number", parent = mytuple[0])       
        elif mytuple[5].get().isnumeric()!=True:
            messagebox.showerror("Error","Plese Don't use Strings and Special letters in Contact", parent = mytuple[0])
        elif len(str(mytuple[5].get()))!=10:
            print(len(str(mytuple[5].get())))
            messagebox.showerror("Error", "Invalid Contact Number pleaseenter correct ontact number", parent = mytuple[0])
        elif self.check_email(mytuple)!=True:
            messagebox.showerror("Error","Invalid email please enter valid email", parent = mytuple[0])
        elif mytuple[6].get() =="":
            messagebox.showerror("Error","please enter date of birth", parent = mytuple[0])
        elif mytuple[7].get() =="":
            messagebox.showerror("Error","please enter date of Joining", parent = mytuple[0])
        elif mytuple[8].get()=="":
            messagebox.showerror("Error","Please generate password using mixture of numbers and strings", parent = mytuple[0])    
        elif self.checkpassword(mytuple)==False: 
            messagebox.showerror("Error","password must be mixture of numbers ,alphabates and special characters please create a strong password", parent = mytuple[0])
        elif len(mytuple[8].get())<6 or len(mytuple[8].get())>11:
            messagebox.showerror("Error","the size of password must be greater than 6 and shorter than 11", parent = mytuple[0])
        elif self.checkpassword(mytuple)==12: 
            messagebox.showerror("Error","Eror first letter must be alphabate in password", parent = mytuple[0])
        elif mytuple[11].get()=="":
            messagebox.showerror("Error","please enter salary", parent = mytuple[0])
        elif mytuple[11].get().isnumeric()!=True:
            messagebox.showerror("Error","please don't strings and special characters in salary", parent = mytuple[0])
        elif mytuple[10].get("0.1", END).strip()=="":
            messagebox.showerror("Error","please enter address ", parent = mytuple[0])
        elif(int(doj[2])-int(dob[2])<18):
            messagebox.showinfo("info","Age of employee must be more than 18 years",parent = mytuple[0])

        else:
            cur.execute("select * from Employee where eid = ?",(mytuple[1].get(),))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error" , "Invalid Employee ID", parent = mytuple[0])
            else:
                cur.execute("update Employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                    mytuple[2].get(),
                    mytuple[3].get(),
                    mytuple[4].get(),
                    mytuple[5].get(),
                    mytuple[6].get(),
                    mytuple[7].get(),
                    mytuple[8].get(),
                    mytuple[9].get(),
                    mytuple[10].get("1.0",END),
                    mytuple[11].get() ,   
                    mytuple[1].get()
                ))
                con.commit()
                messagebox.showinfo("success" , "Employee Updated sucessfully",parent = mytuple[0])
                con.close()
                self.show(mytuple[12],mytuple[0])
                self.clear(mytuple)

        #except Exception as ex:
         #   messagebox.showerror("Error", f" 4{str(ex)}",parent = mytuple[0])


    def delete(self, mytuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if mytuple[1].get() =="":
                    messagebox.showerror("Error" , "Employee ID must be required", parent = mytuple[0])
                else:
                    cur.execute("select * from Employee where eid = ?",(mytuple[1].get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error" , "Invalid Employee ID", parent = mytuple[0])
                    else:
                        op= messagebox.askyesno("conform", "Doyou really want to delete the Employee ?",parent = mytuple[0])
                        if op == True:
                            cur.execute("delete from Employee where eid=?" ,(mytuple[1].get(),))
                            con.commit()
                            messagebox.showinfo("Delete" , "Employee deleted successfully",parent=mytuple[0])
                            con.close()
                            self.show(mytuple[12],mytuple[0])
                            self.clear(mytuple)
        except Exception as ex:
            messagebox.showerror("Error", f" 5{str(ex)}",parent = mytuple[0])

    def search(self,mytuple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
            if mytuple[2].get()=="Select":
                messagebox.showerror("Error","Select the Search by option" , parent = mytuple[0])

            elif mytuple[2].get() == "":
                messagebox.showerror("Error","Search input should be required" , parent=mytuple[0])
            elif mytuple[1].get() == "":
                cur.execute("select * from Employee")
                rows = cur.fetchall()
                if len(rows)!=0:
                    mytuple[3].delete(*mytuple[3].get_children())
                    for row in rows:
                        mytuple[3].insert("",END,values=row)
            else:
                cur.execute("select * from Employee where "+ mytuple[2].get()+" like '%"+mytuple[1].get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    mytuple[3].delete(*mytuple[3].get_children())
                    for row in rows:
                        mytuple[3].insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent = mytuple[0])
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f" 7{str(ex)}",parent = mytuple[0])

    cal_label1 = None
    def show_calendar(self, MyTuple,lbl):
        if function.cal_label1 and function.cal_label1.winfo_exists():
            function.cal_label1.destroy()

        # Get the position of the D.O.J. entry field dynamically
        x = MyTuple[0].winfo_x()
        y = MyTuple[0].winfo_y() + MyTuple[0].winfo_height() + 5

        # Create a Label to hold the calendar
        lbl.place(x=x, y=y, width=260, height=300)
        lbl.configure(bg="white")

        cal = Calendar(lbl, selectmode='day', date_pattern='dd-mm-yyyy')
        cal.place(relx=0, rely=0, relwidth=1, relheight=0.85)

        def get_date():
            """Get the selected date and update the entry field."""
            date = cal.get_date()
            MyTuple[0].config(state='normal')
            MyTuple[0].delete(0, 'end')
            MyTuple[0].insert(0, date)
            MyTuple[0].config(state='readonly')
            lbl.destroy()
        btn_date = Button(lbl, text="Select Date", command=get_date, bg="black", fg="white",
                          font=("times new roman", 14, "bold"), padx=10, pady=5, cursor="hand2")
        btn_date.place(relx=0.5, rely=0.9, anchor="center", width=120, height=35)

        # Store the calendar label in the class attribute
        function.cal_label = lbl

    cal_label = None  # Store the calendar label as a class attribute
    def show_calendar_doj(self, MyTuple, lbl1):
        # Destroy the existing calendar label if it exists
        if function.cal_label and function.cal_label.winfo_exists():
            function.cal_label.destroy()

        # Get the position of the D.O.J. entry field dynamically
        x = MyTuple[0].winfo_x()
        y = MyTuple[0].winfo_y() + MyTuple[0].winfo_height() + 5

        # Create a Label to hold the calendar
        lbl1.place(x=x, y=y, width=260, height=300)
        lbl1.configure(bg="white")

        cal = Calendar(lbl1, selectmode='day', date_pattern='dd-mm-yyyy')
        cal.place(relx=0, rely=0, relwidth=1, relheight=0.85)

        def get_date():
            """Get the selected date and update the entry field."""
            date = cal.get_date()
            MyTuple[0].config(state='normal')
            MyTuple[0].delete(0, 'end')
            MyTuple[0].insert(0, date)
            MyTuple[0].config(state='readonly')
            lbl1.destroy()

        # Button to select the date
        btn_date = Button(lbl1, text="Select Date", command=get_date, bg="black", fg="white",
                          font=("times new roman", 14, "bold"), padx=10, pady=5, cursor="hand2")
        btn_date.place(relx=0.5, rely=0.9, anchor="center", width=120, height=35)

        # Store the calendar label in the class attribute
        function.cal_label = lbl1


#***********************************************Suplier Class Fuction ************************************************#
    
    
    
    def Suplier_add(self,mytuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if mytuple[1].get() =="":
                    messagebox.showerror("Error", "Invoice ID must be required" , parent = mytuple[0])
                elif mytuple[2].get() =="":
                    messagebox.showerror("Error","Please enter name ", parent = mytuple[0])
                elif self.check_name(mytuple[2])!=True:
                    messagebox.showerror("Error","Name should contain only Alphabates please don't use special characters and numbers", parent = mytuple[0])
                elif mytuple[3].get() =="":
                    messagebox.showerror("Error","Please enter contact number ", parent = mytuple[0])
                elif mytuple[3].get().isnumeric()!=True:
                    messagebox.showerror("Error","Contact number should be numeric please don't use apecial characters and numbers in contact number", parent = mytuple[0])
                elif len(mytuple[3].get())!=10:
                    messagebox.showerror("Error","Invalid contact number please check", parent = mytuple[0])
                elif mytuple[4].get("0.1",END).strip() =="":
                    messagebox.showerror("Error","Please enter description ", parent = mytuple[0])
                else:
                    cur.execute("select * from Suplier where Invoice = ?",(mytuple[1].get(),))
                    row = cur.fetchone()           
                    if (row!= None):
                        messagebox.showerror("Error" , "This Invoice  id already exists , try diffrent", parent = mytuple[0])
                    else:
                        cur.execute("insert into Suplier(Invoice,name,contact,description) values(?,?,?,?)",(
                            mytuple[1].get(),
                            mytuple[2].get(),
                            mytuple[3].get(),
                            mytuple[4].get("1.0",END),                
                        ))
                        con.commit()
                        messagebox.showinfo("success" , "Supplier added sucessfully",parent = mytuple[0])
                        self.Suplier_show(mytuple[5],mytuple[0])
                        self.Suplier_Clears(mytuple)
                        self.Suplir_generateInvoice(mytuple[1])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = mytuple[0])



    def Suplier_show(self,Supplier_Table,root):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
            cur.execute("select * from Suplier")
            rows = cur.fetchall()
            Supplier_Table.delete(*Supplier_Table.get_children())
            for row in rows:
                Supplier_Table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent = root)


    def Suplier_get_data(self,mytuple ):
        self.Suplier_Clears(mytuple)
        try:
            f=mytuple[5].focus()
            content = (mytuple[5].item(f))
            row=content['values']
            mytuple[1].config(state=WRITABLE)
            mytuple[1].delete(0,END)
            mytuple[1].insert(0,row[0]) 
            mytuple[2].insert(0,row[1]) 
            mytuple[3].insert(0,row[2]) 
            mytuple[4].delete("1.0", END) 
            mytuple[4].insert(END ,row[3]) 
            mytuple[1].config(state="readonly")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = mytuple[0])


    def Suplier_Update(self,mytuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if mytuple[1].get() =="":
                    messagebox.showerror("Error", "Invoice ID must be required" , parent = mytuple[0])
                elif mytuple[2].get() =="":
                    messagebox.showerror("Error","Please enter name ", parent = mytuple[0])
                elif self.check_name(mytuple[2])!=True:
                    messagebox.showerror("Error","Name should contain only Alphabates please don't use special characters and numbers", parent = mytuple[0])
                elif mytuple[3].get() =="":
                    messagebox.showerror("Error","Please enter contact number ", parent = mytuple[0])
                elif mytuple[3].get().isnumeric()!=True:
                    messagebox.showerror("Error","Contact number should be numeric please don't use apecial characters and numbers in contact number", parent = mytuple[0])
                elif len(mytuple[3].get())!=10:
                    messagebox.showerror("Error","Invalid contact number please check", parent = mytuple[0])
                elif mytuple[4].get("0.1",END).strip() =="":
                    messagebox.showerror("Error","Please enter description ", parent = mytuple[0])
                else:
                    cur.execute("select * from Suplier where Invoice = ?",(mytuple[1].get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error" , "Invalid Invoice ID", parent = mytuple[0])
                    else:
                        cur.execute("update Suplier set name=?,contact=?,description=? where Invoice=?",(
                            mytuple[2].get(),
                            mytuple[3].get(),
                            mytuple[4].get("1.0",END),   
                            mytuple[1].get()
                        ))
                        con.commit()
                        messagebox.showinfo("success" , "Suppler Updated sucessfully",parent = mytuple[0])
                        self.Suplier_show(mytuple[5],mytuple[0])
                        self.Suplier_Clears(mytuple)
                        self.Suplir_generateInvoice(mytuple[1])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = mytuple[0])


    def suplier_search(self,MYtuple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
            if MYtuple[2].get() == "":
                messagebox.showerror("Error","Invoice no  should be required" , parent=MYtuple[0])
            elif MYtuple[2].get().isnumeric()!=True:
                messagebox.showerror("Error","Invoice should be numeric please don't enter special characters and alphabates", parent=MYtuple[0])

            
            else:
                cur.execute("select * from Suplier where Invoice=? ",(MYtuple[2].get(),))
                row = cur.fetchone()
                if row!=None:
                    MYtuple[1].delete(*MYtuple[1].get_children())
                    MYtuple[1].insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent = MYtuple[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent = MYtuple[0])


    def Suplier_Clears(self,MYtuple):
        try:
            MYtuple[1].config(state=WRITABLE)
            MYtuple[1].delete(0, END)  
            MYtuple[2].delete(0, END)  
            MYtuple[3].delete(0, END) 
            MYtuple[6].delete(0,END) 
            MYtuple[4].delete(1.0, END)
            Eid_tuple = (MYtuple[1],)
            self.Suplir_generateInvoice(MYtuple[1])
            MYtuple[1].config(state="readonly")
  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = MYtuple[0])



    def Suplier_Delete(self,MYtuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
            if MYtuple[1].get() =="":
                messagebox.showerror("Error", "Invoice ID must be required" , parent = MYtuple[0])
            else:
                cur.execute("select * from Suplier where Invoice = ?",(MYtuple[1].get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error" , "Invalid Invoice ID", parent = MYtuple[0])
                else:
                    op= messagebox.askyesno("conform", "Doyou really want to delete the Supplier ?",parent = MYtuple[0])
                    if op == True:
                        cur.execute("delete from Suplier where Invoice=?" ,(MYtuple[1].get(),))
                        con.commit()
                        messagebox.showinfo("Delete" , "Supplier deleted successfully",parent=MYtuple[0])
                        self.Suplier_show(MYtuple[5],MYtuple[0])
                        self.Suplier_Clears(MYtuple)
                        self.Suplir_generateInvoice(MYtuple[1])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = MYtuple[0])


    def Suplir_generateInvoice(self,MYtuple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        cur.execute("Select * from Suplier")
        row = cur.fetchone()
        if row !=None: 
            MYtuple.config(state=WRITABLE)
            con = sqlite3.connect(database="Billing_System.db")
            cur = con.cursor()
            cur.execute("SELECT MAX(Invoice) FROM Suplier")
            result = cur.fetchone()
            c = result[0]  # Extracting the integer value from the tuple
            con.commit()
            c = int(c) + 1
            MYtuple.delete(0, END)
            billno = c
            MYtuple.insert(0, billno)
            MYtuple.config(state="readonly")

        else:
            MYtuple.config(state=WRITABLE)
            billno = 101
            MYtuple.delete(0,END)
            MYtuple.insert(0, billno)
            MYtuple.config(state="readonly")




#**************************************************Category Functions****************************************************
            
    def Categories_add(self,Cattuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if Cattuple[1].get() =="":
                    messagebox.showerror("Error", "category Nmae should  be required" , parent = Cattuple[0])
                else:
                    cur.execute("select * from category where name = ?",(Cattuple[1].get(),))
                    row = cur.fetchone() 
                    if (row!= None):
                        messagebox.showerror("Error" , "This category already present , try diffrent", parent = Cattuple[0])
                    else:
                        cur.execute("insert into category(name) values(?)",(
                            Cattuple[1].get(),           
                        ))
                        con.commit()
                        messagebox.showinfo("success" , "category added sucessfully",parent = Cattuple[0])
                        self.Categories_show(Cattuple[2],Cattuple[0])
                        self.Categories_clear(Cattuple)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Cattuple[0])


    def Categories_show(self,category_table,root):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            category_table.delete(*category_table.get_children())
            for row in rows:
                category_table.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}",parent = root)


    def Categories_get_data(self,Cattuple,event=None):
      
        try:
            f=Cattuple[2].focus()
            content = (Cattuple[2].item(f))
            row=content['values']
            Cattuple[3].set(row[0])
            Cattuple[1].insert(0,row[1])  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Cattuple[0])

    def Categories_clear(self,Cattuple):
        try:
            Cattuple[1].delete(0, END)  
            Cattuple[3].set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Cattuple[0])


    def category_delete(self,Cattuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if Cattuple[3].get() =="":
                    messagebox.showerror("Error", "Please select category from the list " , parent = Cattuple[0])
                else:
                    cur.execute("select * from category where cid = ?",(Cattuple[3].get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error" , "Please try again", parent = Cattuple[0])
                    else:
                        op= messagebox.askyesno("conform", "Doyou really want to delete the category ?",parent = Cattuple[0])
                        if op == True:
                            cur.execute("delete from category where cid=?" ,(Cattuple[3].get(),))
                            con.commit()
                            messagebox.showinfo("Delete" , "category deleted successfully",parent=Cattuple[0])
                            self.Categories_show(Cattuple[2],Cattuple[0])
                            self.Categories_clear(Cattuple)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Cattuple[0])



#********************************************** PRODUCT FUNCTIONS*********************************************************************
            

    def product_add(self,Pro_tuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if Pro_tuple[1].get() =="":
                    messagebox.showerror("Error", "Name should  be required" , parent = Pro_tuple[0])
                elif self.check_name(Pro_tuple[1])!=True:
                    messagebox.showerror("Error","Don't use Numbers and special characters in product name")
                elif Pro_tuple[2].get() =="Select":
                    messagebox.showerror("Error", "category Name should  be required" , parent = Pro_tuple[0])
                elif Pro_tuple[3].get() =="Select":
                    messagebox.showerror("Error", "supplier Name should  be required" , parent = Pro_tuple[0])
                elif Pro_tuple[4].get() =="":
                    messagebox.showerror("Error","Enter Price of product")
                elif Pro_tuple[4].get().isnumeric()!=True:
                    messagebox.showerror("Error","Price should be numeric Don't use Strings and special characters")
                elif Pro_tuple[5].get()=="":
                    messagebox.showerror("Error","Error Please Enter Quantity")
                elif Pro_tuple[5].get().isnumeric()!=True:
                    messagebox.showerror("Error","Quantity should be numeric Don't use Strings and special characters ")

                else:
                    cur.execute("select * from category where name = ?",(Pro_tuple[1].get(),))
                    row = cur.fetchone()
                   
                    if (row!= None):
                        messagebox.showerror("Error" , "This category already present , try diffrent", parent = Pro_tuple[0])
                    else:
                        cur.execute("insert into product(supplier,category,name,price,qty,status) values(?,?,?,?,?,?)",(
                            Pro_tuple[3].get(),
                            Pro_tuple[2].get(),
                            Pro_tuple[1].get(),  
                            Pro_tuple[4].get(),
                            Pro_tuple[5].get(),
                            Pro_tuple[6].get(),         
                        ))
                        con.commit()
                        messagebox.showinfo("success" , "category added sucessfully",parent = Pro_tuple[0])
                        self.Product_show(Pro_tuple[7])
                        self.product_clear(Pro_tuple)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Pro_tuple[0])

    def Product_show(self,frameTreaview):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            frameTreaview.delete(*frameTreaview.get_children())
            for row in rows:
                frameTreaview.insert("",END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def Product_get_data(self,Pro_tuple):
        self.product_clear(Pro_tuple)
        try:
            f=Pro_tuple[7].focus()
            content = (Pro_tuple[7].item(f))
            row=content['values']
            Pro_tuple[3].config(state=WRITABLE)
            Pro_tuple[2].config(state=WRITABLE)
            Pro_tuple[6].config(state=WRITABLE)
            Pro_tuple[3].delete(0, END)
            Pro_tuple[2].delete(0, END)
            Pro_tuple[6].delete(0,END)
            Pro_tuple[3].insert(0,row[1]) 
            Pro_tuple[2].insert(0,row[2]) 
            Pro_tuple[1].insert(0,row[3]) 
            Pro_tuple[4].insert(0,row[4]) 
            Pro_tuple[5].insert(0,row[5]) 
            Pro_tuple[6].insert(0,row[6]) 
            Pro_tuple[3].config(state="readonly")
            Pro_tuple[2].config(state="readonly")
            Pro_tuple[6].config(state="readonly")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Pro_tuple[0])

    def product_clear(self,Pro_tuple):
        try:
            Pro_tuple[3].config(state=WRITABLE)
            Pro_tuple[2].config(state=WRITABLE)
            Pro_tuple[6].config(state=WRITABLE)
            Pro_tuple[3].delete(0, END)
            Pro_tuple[2].delete(0, END)  
            Pro_tuple[1].delete(0, END) 
            Pro_tuple[4].delete(0,END) 
            Pro_tuple[5].delete(0, END) 
            Pro_tuple[6].delete(0,END) 
            Pro_tuple[3].insert(0,"Select")
            Pro_tuple[2].insert(0,"Select")
            Pro_tuple[6].insert(0,"Active")
            Pro_tuple[3].config(state="readonly")
            Pro_tuple[2].config(state="readonly")
            Pro_tuple[6].config(state="readonly")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Pro_tuple[0])



    def product_update(self,Pro_tuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if Pro_tuple[1].get() =="":
                    messagebox.showerror("Error", "Product Name must be required" , parent = Pro_tuple[0])
                if self.check_name(Pro_tuple[1])!=True:
                    messagebox.showerror("Error","Please don't use specian characters and numbers in name")
                elif Pro_tuple[3].get=="":
                    messagebox.showerror("Error","Please select the supplier")
                elif Pro_tuple[2].get=="":
                    messagebox.showerror("Error","Please select the Category")
                
                else:
                    cur.execute("select * from product where name = ?",(Pro_tuple[1].get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error" , "Invalid Product Name ", parent = Pro_tuple[0])
                    else:
                        cur.execute("update product set supplier=?,category=?,price=?,qty=?, status = ? where name=?",(
                            Pro_tuple[3].get(),
                            Pro_tuple[2].get(),
                            Pro_tuple[4].get(),
                            Pro_tuple[5].get(),
                            Pro_tuple[6].get(),
                            Pro_tuple[1].get(),   
                        ))
                        con.commit()
                        messagebox.showinfo("success" , "Product Updated sucessfully",parent = Pro_tuple[0])
                        self.Product_show(Pro_tuple[7])
                        self.product_clear(Pro_tuple)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Pro_tuple[0])


    def product_delete(self,Pro_tuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
                if Pro_tuple[3].get() =="":
                    messagebox.showerror("Error", "Invoice ID must be required" , parent = Pro_tuple[0])
                else:
                    cur.execute("select * from product where name = ?",(Pro_tuple[1].get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error" , "Invalid Invoice ID", parent = Pro_tuple[0])
                    else:
                        op= messagebox.askyesno("conform", "Doyou really want to delete the Supplier ?",parent = Pro_tuple[0])
                        if op == True:
                            cur.execute("delete from product where name=?" ,(Pro_tuple[1].get(),))
                            con.commit()
                            messagebox.showinfo("Delete" , "product deleted successfully",parent=Pro_tuple[0])
                            self.Product_show(Pro_tuple[7])
                            self.product_clear(Pro_tuple)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Pro_tuple[0])

    
    def product_search(self,Pro_tuple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
            if Pro_tuple[2].get()=="Select":
                messagebox.showerror("Error","Select the Search by option" , parent = Pro_tuple[0])

            elif Pro_tuple[2].get() == "":
                messagebox.showerror("Error","Search input should be required" , parent=Pro_tuple[0])
            else:
                cur.execute("select * from product where "+ Pro_tuple[2].get()+" like '%"+Pro_tuple[1].get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    Pro_tuple[3].delete(*Pro_tuple[3].get_children())
                    for row in rows:
                        Pro_tuple[3].insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent = Pro_tuple[0])
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent = Pro_tuple[0])

    def fetch_cat_supplier_data(self,Pro_tuple):
        try:
            con = sqlite3.connect(database="Billing_System.db")
            cur = con.cursor()
            cur.execute("select name from category")
            data=cur.fetchall()
            self.list = []
            if len(data)>0:
                for i in data:
                    self.list.append(i[0])
                Pro_tuple[2].config(values=self.list)
            else:
                self.list.append("Empty")
                Pro_tuple[2].config(values=self.list)

            cur.execute("select name from Suplier")
            data1=cur.fetchall()
            self.list2 = []
            if len(data1)>0:
                for J in data1:
                    self.list2.append(J[0])
                Pro_tuple[1].config(values=self.list2)
            else:
                self.list2.append("Empty")
                Pro_tuple[1].config(values=self.list2)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent =Pro_tuple[0])


#**********************************************MAin_billsection functions*******************************************************
    def Billsection_show(self,frameTreaview):
        #clear()
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        try:
            cur.execute("select pid ,name, price, qty, status from product where status='Active'")
            rows = cur.fetchall()
            frameTreaview.delete(*frameTreaview.get_children())
            for row in rows:
                frameTreaview.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def Billsection_search(self,Bill_TUple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
            if Bill_TUple[1].get() == "":
                messagebox.showerror("Error","Search input should be required" , parent=Bill_TUple[0])
            else:
                cur.execute("select pid ,name, price, qty, status from product where name like '%"+Bill_TUple[1].get()+"%' and status ='Active'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    Bill_TUple[2].delete(*Bill_TUple[2].get_children())
                    for row in rows:
                        Bill_TUple[2].insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent = Bill_TUple[0])
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent = Bill_TUple[0])


    def Billsecton_search_all(self,frameTreaview,Bill_TUple):
        con = sqlite3.connect(database="Billing_System.db")
        cur = con.cursor()
        try:
                cur.execute("select pid ,name, price, qty, status from product where status = 'Active'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    frameTreaview.delete(*frameTreaview.get_children())
                    for row in rows:
                        frameTreaview.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent = Bill_TUple[0])

    def Billsection_get_data(self,Bill_TUple):
        try:
            f=Bill_TUple[5].focus()
            content = (Bill_TUple[5].item(f))
            row=content['values']
            Bill_TUple[1].config(state=WRITABLE)
            Bill_TUple[2].config(state=WRITABLE)
            Bill_TUple[2].delete(0, END)
            Bill_TUple[1].delete(0, END)
            Bill_TUple[4].set(row[0])
            Bill_TUple[2].insert(0,row[1]) 
            Bill_TUple[1].insert(0,row[2])  
            Bill_TUple[3].config(text=f"In Stock [{row[3]}]")
            self.stock_lbl_frametreaview2 = row[3]
            Bill_TUple[1].config(state="readonly")
            Bill_TUple[2].config(state="readonly")
            return self.stock_lbl_frametreaview2
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Bill_TUple[0])

    
    def checkdiscount(self,Discount):
        for i in Discount.get():
            a = Discount.get()
            if i.isalpha()==True:
                return True
            elif i in string.punctuation:
                return True
        else:
            return False 

    def checkquantity(self,Quantity):
        for i in Quantity.get():
            a = Quantity.get()
            if i.isalpha()==True:
                return True
            elif i in string.punctuation:
                return True
        else:
            return False                                     



    def Add_updateCart(self,Bill_TUple):
        Bill_update = (Bill_TUple[5],Bill_TUple[6],Bill_TUple[9],Bill_TUple[10])

        Bill_TUple2 =(Bill_TUple[0],Bill_TUple[5],Bill_TUple[7],Bill_TUple[8])

        try:
            if Bill_TUple[1].get() == "":
                messagebox.showerror("Error","Please Enter Quantity")
            elif self.checkquantity(Bill_TUple[1])==True:
                    messagebox.showerror("Error", "Quantity should be numeric please dont use special caracters and strings")
            elif Bill_TUple[2].get()=="":
                messagebox.showerror("Error","Please select the product From List")
            elif int(Bill_TUple[1].get())>int(self.stock_lbl_frametreaview2):
                messagebox.showerror("Error","Invalid Quantity ,Quantity must be less than Stock of the product")
            else:
                
                
               # self.price_cal = float(int(Bill_TUple[1].get())*float(Bill_TUple[3].get()))
                self.price_cal = float(Bill_TUple[3].get())
                self.cart_data = [Bill_TUple[4].get(),Bill_TUple[2].get(),self.price_cal,Bill_TUple[1].get(),self.stock_lbl_frametreaview2]

                self.product_present ='no'
                self.index = -1
                for row in Bill_TUple[5]:
                    if Bill_TUple[4].get() ==row[0]:
                        self.product_present = "yes"
                        break
                    self.index+=1 
                
                if self.checkdiscount(Bill_TUple[6])==True:
                    messagebox.showerror("Error", "Discount percentage should be numeric please dont use special caracters and strings")
                if self.product_present =='yes':
                    op = messagebox.askyesno('Confirm',"product aready present do you want to update or remove product from cart list",parent= Bill_TUple[0])
                    if op ==True:
                        if Bill_TUple[1].get()=="0":
                            Bill_TUple[5].pop(self.index)
                        else:
                           # Bill_TUple[5][self.index][2] = self.price_cal
                            Bill_TUple[5][self.index][3] =Bill_TUple[1].get()
                else:
                    Bill_TUple[5].append(self.cart_data)
                self.show_cart(Bill_TUple2)
                self.bill_update(Bill_update)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Bill_TUple[0])


    def show_cart(self,Bill_TUple2):
        try:
            Bill_TUple2[2].delete(*Bill_TUple2[2].get_children())
            for row in Bill_TUple2[1]:
                Bill_TUple2[2].insert('',END,values=row)
            Bill_TUple2[3].config(text=f"Cart \t \t\t\tTotal Products\t[{str(len(Bill_TUple2[1]))}]")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Bill_TUple2[0])

    def bill_update(self,Bill_update):
        self.bill_amount = 0
        self.net_pay = 0
        for row in Bill_update[0]:
            self.bill_amount = self.bill_amount+ int(row[2])*int(row[3])
        if Bill_update[1].get()=="" or Bill_update[1].get()==0:
            self.net_pay= self.bill_amount-(self.bill_amount*100)/100
        else:
            self.net_pay= self.bill_amount-(self.bill_amount*int(Bill_update[1].get()))/100
            self.total_discount = self.bill_amount*int(Bill_update[1].get())/100
        Bill_update[2].config(text=f"Net Pay \n [{str(self.net_pay)}]")
        Bill_update[3].config(text=f"Billl Amount \n [{str(self.bill_amount)}]")


    def generate_bill(self,Bill_tuple):
        if Bill_tuple[0].get() =="" or Bill_tuple[1].get() =="":
            messagebox.showerror("Error","Custumer Details must be required please enter both details",parent = Bill_tuple[8])
        elif self.check_name(Bill_tuple[0])!=True:
            messagebox.showerror("Error","Invalid name please Don't use numbers and special character in Name",parent=Bill_tuple[8])
        elif Bill_tuple[1].get().isnumeric()!=True:
            messagebox.showerror("Error","Contact must be numeric please don't use strings and special characters in contact",parent=Bill_tuple[8])
        elif len(str(Bill_tuple[1].get()))!=10:
            messagebox.showerror("Error","Invalid Contact number please check",parent=Bill_tuple[8])
        elif len(Bill_tuple[2]) == 0:
            messagebox.showerror("Error","please select product",parent=Bill_tuple[8])
        else:
            self.bill_amount = 0
            self.net_pay = 0
            for row in Bill_tuple[2]:
                self.bill_amount = self.bill_amount+ int(row[2])*int(row[3])
            if Bill_tuple[3].get()=="" or Bill_tuple[3].get()==0:
                self.net_pay= self.bill_amount-(self.bill_amount*100)/100
            else:
                Bill_tuple[6].config(state="normal")
                self.net_pay= self.bill_amount-(self.bill_amount*int(Bill_tuple[3].get()))/100
                self.total_discount = self.bill_amount*int(Bill_tuple[3].get())/100
            Bill_tuple[4].config(text=f"Net Pay \n [{str(self.net_pay)}]")
            Bill_tuple[5].config(text=f"Billl Amount \n [{str(self.bill_amount)}]")
            Bill_tuple2 =(Bill_tuple[6],self.bill_amount,self.total_discount,self.net_pay)
            self.bill_top(Bill_tuple)
            self.bill_middle(Bill_tuple)
            self.bill_bottom(Bill_tuple2)
            Bill_tuple[6].config(state="disabled")

            Bill_file= open(f'Bills/{str(Bill_tuple[0].get())+str(self.Bill_no)}.txt',"w")
            Bill_file.write(Bill_tuple[6].get('1.0',END))
            Bill_file.close()
            messagebox.showinfo('Saved',"Bill saved Successfully",parent=Bill_tuple[8])
            self.file_print= 1
            return self.file_print


    def bill_top(self,Bill_tuple):
        self.Bill_no = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
        self.bill_top_temlet =f'''\t         Jhai Ambe Kirana Store
Phone No. 626745XXXX   
Junapani-208329
{str("*"*62)}
Customer Name :- {Bill_tuple[0].get()}          
Ph. No :- {Bill_tuple[1].get()}
Bill No. {str(self.Bill_no)}       \t  \t  \t          Date : {str(time.strftime("%d/%m/%y"))}
{str("*"*62)}
Product Name \t\t            QTY      \t     Price
{str("*"*62)}
           '''
        Bill_tuple[6].delete(0.1,END)
        Bill_tuple[6].insert(END,self.bill_top_temlet)

    def bill_middle(self,Bill_tuple):
        con = sqlite3.connect(database=r"Billing_System.db")
        cur = con.cursor()
        for row in Bill_tuple[2]:
            name = row[1]
            qty = int(row[4])-int(row[3])
            price = row[2]
            pid = row[0]
            if int(row[3])==row[4]:
                status = 'Inactive'
            elif int(row[3])!=row[4]:
                status = 'Active'
            Bill_tuple[6].insert(END,"\n "+str(name)+"\t\t\t"+str(row[3])+"\t "+str(price))
            cur.execute("update product set qty=?,status=? where pid=?",(
                qty,
                status,
                pid
                ))
            con.commit()
            self.Billsection_show(Bill_tuple[7])
    





    def bill_bottom(self,Bill_tuple2):
        self.bill_bottom_temp = f''' 
{str("*"*62)}  
Bill Amount  :-  {str(Bill_tuple2[1])}
Total Discount :- {str(Bill_tuple2[2])}
Net Pay :-{str(Bill_tuple2[3])}
{str("*"*62)}

            ''' 
        Bill_tuple2[0].insert(END,self.bill_bottom_temp)



    def clear_cart(self,Bill_tuple1):
        Bill_tuple1[0].config(state=WRITABLE)
        Bill_tuple1[1].config(state=WRITABLE)
        Bill_tuple1[1].delete(0, END)
        Bill_tuple1[0].delete(0, END)
        Bill_tuple1[2].set("")
        Bill_tuple1[3].delete(0,END) 
        Bill_tuple1[4].config(text=f"In Stock []")
        Bill_tuple1[5].config(text="Billl Amount \n [0]")
        Bill_tuple1[6].config(text="Net Pay \n [0]")
        Bill_tuple1[0].config(state="readonly")
        Bill_tuple1[7].delete(0,END)
        Bill_tuple1[7].insert(END,0)
        Bill_tuple1[1].config(state="readonly")

    def clear_all(self,Bill_tuple1,Bill_TUple2):
        Bill_TUple2[4].config(state="normal")
        del Bill_TUple2[1][:]
        Bill_TUple2[5].delete(0,END)
        Bill_TUple2[6].delete(0,END)
        Bill_TUple2[4].delete('1.0',END)
        Bill_TUple2[4].config(state=DISABLED)
        self.clear_cart(Bill_tuple1)
        self.Billsection_show(Bill_TUple2[2])
        self.show_cart(Bill_TUple2)


    def print_file(self,billtextarea):
        if self.file_print ==1:
            messagebox.showinfo("print","Please wait while printing")
            my_file = tempfile.mkstemp('.txt')
            open(my_file[1],'w').write(billtextarea.get('1.0',END))
            os.startfile(my_file[1],'print')
        else:
            messagebox.showerror("Error","Please generate bill, to print the reciept")



    def get_cart_data(self,Bill_tuple):
       # self.clear()
        try:
            f=Bill_tuple[1].focus()
            content = (Bill_tuple[1].item(f))
            row=content['values']
            Bill_tuple[2].config(state=WRITABLE)
            Bill_tuple[3].config(state=WRITABLE)
            Bill_tuple[3].delete(0, END)
            Bill_tuple[2].delete(0, END)
            Bill_tuple[4].set(row[0])
            Bill_tuple[3].insert(0,row[1]) 
            Bill_tuple[2].insert(0,row[2])  
            Bill_tuple[5].config(text=f"In Stock [{row[4]}]")
            Bill_tuple[2].config(state="readonly")
            Bill_tuple[3].config(state="readonly")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent = Bill_tuple[0])

if __name__=="__main__":
    obj = function()