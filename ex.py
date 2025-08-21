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

