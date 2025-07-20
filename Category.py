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
        self.root.state("zoomed")

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
