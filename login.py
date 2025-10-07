# File: MultipleFiles/login.py
from tkinter import *
from tkinter import messagebox
import sqlite3, os
from PIL import Image, ImageTk

SESSION_FILE = "session.txt"

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Inventory Management System")
        self.root.state('zoomed')  # Fullscreen
        self.root.configure(bg="white")

        # ===== Check if already logged in =====
        if os.path.exists(SESSION_FILE):
            self.root.destroy()
            from Page1 import page1
            new_root = Tk()
            page1(new_root)
            new_root.mainloop()
            return

        # Variables
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.remember_var = BooleanVar()

        # ===== Gradient Background =====
        self.bg_canvas = Canvas(self.root, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)

        screen_w, screen_h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        for i in range(0, screen_h, 2):
            color = "#2980B9" if i < screen_h // 2 else "#6DD5FA"
            self.bg_canvas.create_rectangle(0, i, screen_w, i + 2, outline="", fill=color)

        # ===== Card Frame =====
        self.card = Frame(self.bg_canvas, bg="white", bd=0, relief=FLAT,
                          highlightthickness=2, highlightbackground="#2980B9")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=950, height=550)

        # Left Side - Image
        try:
            self.img = Image.open("static/login.png")  # Add a nice login illustration here
            self.img = self.img.resize((400, 550))
            self.img = ImageTk.PhotoImage(self.img)
            img_label = Label(self.card, image=self.img, bg="white")
            img_label.pack(side=LEFT, fill=Y)
        except Exception:
            img_label = Label(self.card, text="Welcome Back!", font=("Segoe UI", 22, "bold"),
                              bg="#2980B9", fg="white")
            img_label.pack(side=LEFT, fill=Y, ipadx=50, ipady=80)

        # Right Side - Form
        self.form_frame = Frame(self.card, bg="white", padx=40, pady=30)
        self.form_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        title = Label(self.form_frame, text="User Login", font=("Segoe UI", 22, "bold"),
                      bg="white", fg="#2980B9")
        title.grid(row=0, column=0, columnspan=2, pady=(10, 25))

        # ===== Email =====
        Label(self.form_frame, text="Email", font=("Segoe UI", 12, "bold"),
              bg="white", fg="#2C3E50").grid(row=1, column=0, sticky="w", pady=10)
        email_entry = Entry(self.form_frame, textvariable=self.email_var, font=("Segoe UI", 12),
                            bd=1, relief=SOLID)
        email_entry.grid(row=1, column=1, sticky="ew", pady=10, padx=10, ipady=6)

        # Hover
        email_entry.bind("<FocusIn>", lambda e: email_entry.config(highlightthickness=2, highlightbackground="#2980B9"))
        email_entry.bind("<FocusOut>", lambda e: email_entry.config(highlightthickness=1, highlightbackground="#BDC3C7"))

        # ===== Password =====
        Label(self.form_frame, text="Password", font=("Segoe UI", 12, "bold"),
              bg="white", fg="#2C3E50").grid(row=2, column=0, sticky="w", pady=10)
        password_entry = Entry(self.form_frame, textvariable=self.password_var, font=("Segoe UI", 12),
                               bd=1, relief=SOLID, show="*")
        password_entry.grid(row=2, column=1, sticky="ew", pady=10, padx=10, ipady=6)

        password_entry.bind("<FocusIn>", lambda e: password_entry.config(highlightthickness=2, highlightbackground="#2980B9"))
        password_entry.bind("<FocusOut>", lambda e: password_entry.config(highlightthickness=1, highlightbackground="#BDC3C7"))

        # ===== Remember Me =====
        Checkbutton(self.form_frame, text="Remember Me", variable=self.remember_var,
                    bg="white", font=("Segoe UI", 11)).grid(row=3, column=0, columnspan=2, sticky="w", pady=10)

        # ===== Login Button =====
        login_btn = Button(
            self.form_frame, text="Login", command=self.login_user,
            font=("Segoe UI", 13, "bold"), bg="#2ECC71", fg="white",
            activebackground="#27AE60", relief=FLAT, padx=25, pady=10, cursor="hand2"
        )
        login_btn.grid(row=4, column=0, columnspan=2, pady=25, sticky="ew")

        def on_enter_btn(e): login_btn.config(bg="#27AE60")
        def on_leave_btn(e): login_btn.config(bg="#2ECC71")
        login_btn.bind("<Enter>", on_enter_btn)
        login_btn.bind("<Leave>", on_leave_btn)

        # ===== Don't have an account? Register =====
        register_label = Label(
            self.form_frame, text="Don't have an account? Create one",
            font=("Segoe UI", 12, "underline"), bg="white", fg="#2980B9",
            cursor="hand2"
        )
        register_label.grid(row=5, column=0, columnspan=2, pady=10)

        register_label.bind("<Enter>", lambda e: register_label.config(fg="#1A5276"))
        register_label.bind("<Leave>", lambda e: register_label.config(fg="#2980B9"))
        register_label.bind("<Button-1>", self.go_to_register)

        self.form_frame.grid_columnconfigure(1, weight=1)

        # Load saved email if exists
        self.load_saved_email()

    # ===== Remember Email =====
    def load_saved_email(self):
        if os.path.exists("config.txt"):
            with open("config.txt", "r") as f:
                email = f.readline().strip()
                if email:
                    self.email_var.set(email)
                    self.remember_var.set(True)

    # ===== Login Function =====
    def login_user(self):
        email, password = self.email_var.get().strip(), self.password_var.get()

        if not (email and password):
            messagebox.showerror("Login Error", "Email and Password are required.", parent=self.root)
            return

        try:
            con = sqlite3.connect(database="Billing_System.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM Users WHERE email=? AND password=?", (email, password))
            user = cur.fetchone()
            con.close()

            if user:
                with open(SESSION_FILE, "w") as f:
                    f.write(email)

                if self.remember_var.get():
                    with open("config.txt", "w") as f:
                        f.write(email)
                else:
                    if os.path.exists("config.txt"):
                        os.remove("config.txt")

                messagebox.showinfo("Login Success", "Welcome back!", parent=self.root)
                self.root.destroy()
                from Page1 import page1
                new_root = Tk()
                page1(new_root)
                new_root.mainloop()
            else:
                messagebox.showerror("Login Error", "Invalid email or password.", parent=self.root)

        except sqlite3.Error as ex:
            messagebox.showerror("Database Error", f"Error during login: {str(ex)}", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Unexpected error: {str(ex)}", parent=self.root)

    # ===== Register Page Redirect =====
    def go_to_register(self, event=None):
        self.root.destroy()
        from register import RegisterPage
        new_root = Tk()
        RegisterPage(new_root)
        new_root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = LoginPage(root)
    root.mainloop()
