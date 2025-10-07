# File: MultipleFiles/register.py
from tkinter import *
from tkinter import messagebox
import sqlite3
import re
from PIL import Image, ImageTk


class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Register - Inventory Management System")
        self.root.state('zoomed')  # Fullscreen
        self.root.configure(bg="white")

        # ===== Gradient Background =====
        self.bg_canvas = Canvas(self.root, highlightthickness=0, bd=0)
        self.bg_canvas.pack(fill="both", expand=True)

        screen_w, screen_h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        for i in range(0, screen_h, 2):
            # Blue to Aqua gradient
            r = 40 + i // 20
            g = 116 + i // 30
            b = 166 + i // 25
            color = f"#{min(255,r):02x}{min(255,g):02x}{min(255,b):02x}"
            self.bg_canvas.create_rectangle(0, i, screen_w, i + 2, outline="", fill=color)

        # ===== Decorative Background Images =====
        try:
            deco1 = Image.open("static/deco1.png").resize((200, 200))
            self.deco1 = ImageTk.PhotoImage(deco1)
            self.bg_canvas.create_image(150, 150, image=self.deco1)

            deco2 = Image.open("static/deco2.png").resize((180, 180))
            self.deco2 = ImageTk.PhotoImage(deco2)
            self.bg_canvas.create_image(screen_w-150, screen_h-150, image=self.deco2)
        except:
            pass

        # ===== Card Frame =====
        self.card = Frame(self.bg_canvas, bg="white", bd=0, relief=FLAT,
                          highlightthickness=0)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=600)

        # Simulated shadow (behind card)
        self.shadow = Frame(self.bg_canvas, bg="#aaaaaa")
        self.shadow.place(relx=0.5, rely=0.5, anchor="center", width=1005, height=605)

        self.card.lift()  # Bring card above shadow

        # ===== Left Side - Banner Image =====
        try:
            self.img = Image.open("static/register_banner.png").resize((450, 600))
            self.img = ImageTk.PhotoImage(self.img)
            img_label = Label(self.card, image=self.img, bg="white")
            img_label.pack(side=LEFT, fill=Y)
        except:
            img_label = Label(self.card, text="Welcome\nRegister Here", font=("Segoe UI", 22, "bold"),
                              bg="#2874A6", fg="white", justify="center")
            img_label.pack(side=LEFT, fill=Y, ipadx=50, ipady=80)

        # ===== Right Side - Form =====
        self.form_frame = Frame(self.card, bg="white", padx=40, pady=20)
        self.form_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        title = Label(
            self.form_frame, text="Create Your Shop Account", font=("Segoe UI", 22, "bold"),
            bg="white", fg="#2874A6"
        )
        title.grid(row=0, column=0, columnspan=2, pady=(10, 25))

        # Variables
        self.shop_name = StringVar()
        self.owner_name = StringVar()
        self.email = StringVar()
        self.phone_number = StringVar()
        self.address = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        row_num = 1

        # ===== Input Builder with Icon =====
        def add_input(label, text_var, icon_path=None, show=None):
            nonlocal row_num
            Label(self.form_frame, text=label, font=("Segoe UI", 12, "bold"),
                  bg="white", fg="#2C3E50").grid(row=row_num, column=0, sticky="w", pady=5)

            frame = Frame(self.form_frame, bg="white", bd=1, relief=SOLID)
            frame.grid(row=row_num, column=1, sticky="ew", pady=5, padx=10)

            if icon_path:
                try:
                    icon_img = Image.open(icon_path).resize((20, 20))
                    icon = ImageTk.PhotoImage(icon_img)
                    lbl_icon = Label(frame, image=icon, bg="white")
                    lbl_icon.image = icon
                    lbl_icon.pack(side=LEFT, padx=5)
                except:
                    pass

            entry = Entry(frame, textvariable=text_var, font=("Segoe UI", 12),
                          bd=0, show=show, relief=FLAT)
            entry.pack(side=LEFT, fill=X, expand=True, ipady=5, padx=5)

            # Hover + Focus Effects
            def on_enter(e): frame.config(highlightthickness=2, highlightbackground="#2874A6")
            def on_leave(e): frame.config(highlightthickness=1, highlightbackground="#BDC3C7")
            entry.bind("<FocusIn>", on_enter)
            entry.bind("<FocusOut>", on_leave)

            row_num += 1

        add_input("Shop Name", self.shop_name, "static/shop.png")
        add_input("Owner Name", self.owner_name, "static/user.png")
        add_input("Email", self.email, "static/email.png")
        add_input("Phone Number", self.phone_number, "static/phone.png")
        add_input("Address", self.address, "static/location.png")
        add_input("Password", self.password, "static/lock.png", show="*")
        add_input("Confirm Password", self.confirm_password, "static/lock.png", show="*")

        # ===== Register Button =====
        register_btn = Button(
            self.form_frame, text="Register", command=self.register_user,
            font=("Segoe UI", 13, "bold"), bg="#2874A6", fg="white",
            activebackground="#1A5276", relief=FLAT, padx=25, pady=10, cursor="hand2"
        )
        register_btn.grid(row=row_num, column=0, columnspan=2, pady=25, sticky="ew")

        def on_enter_btn(e): register_btn.config(bg="#1A5276")
        def on_leave_btn(e): register_btn.config(bg="#2874A6")
        register_btn.bind("<Enter>", on_enter_btn)
        register_btn.bind("<Leave>", on_leave_btn)

        # ===== Already have an account? Login =====
        row_num += 1
        login_label = Label(
            self.form_frame, text="Already have an account? Login",
            font=("Segoe UI", 12, "underline"), bg="white", fg="#2874A6",
            cursor="hand2"
        )
        login_label.grid(row=row_num, column=0, columnspan=2, pady=10)

        login_label.bind("<Enter>", lambda e: login_label.config(fg="#1A5276"))
        login_label.bind("<Leave>", lambda e: login_label.config(fg="#2874A6"))
        login_label.bind("<Button-1>", self.go_to_login)

        self.form_frame.grid_columnconfigure(1, weight=1)

    # ===== Register Function =====
    def register_user(self):
        shop = self.shop_name.get()
        owner = self.owner_name.get()
        email = self.email.get()
        phone = self.phone_number.get()
        addr = self.address.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()

        if not all([shop, owner, email, phone, addr, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
            return
        if not re.match(r"^[0-9]{10,15}$", phone):
            messagebox.showerror("Error", "Phone number must be 10-15 digits", parent=self.root)
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
            return

        try:
            con = sqlite3.connect("Billing_System.db")
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                shop_name VARCHAR(255),
                owner_name VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                phone_number VARCHAR(20),
                address TEXT,
                password VARCHAR(255)
            )""")
            cur.execute("SELECT * FROM Users WHERE email=?", (email,))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error", "User already exists", parent=self.root)
            else:
                cur.execute("INSERT INTO Users (shop_name, owner_name, email, phone_number, address, password) VALUES (?, ?, ?, ?, ?, ?)",
                            (shop, owner, email, phone, addr, password))
                con.commit()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                self.go_to_login()
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

    # ===== Go to Login Page =====
    def go_to_login(self, event=None):
        self.root.destroy()
        from login import LoginPage
        new_root = Tk()
        LoginPage(new_root)
        new_root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = RegisterPage(root)
    root.mainloop()
