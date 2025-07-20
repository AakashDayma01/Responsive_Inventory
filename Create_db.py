import sqlite3
def create_db():
    con = sqlite3.connect(database="Billing_System.db")
    cur = con.cursor()

    cur.execute("create table if not exists Employee(eid integer primary key autoincrement, name varchar(225), email varchar(225), gender varchar(225), contact varchar(225), dob varchar(225), doj varchar(225), pass varchar(225), utype varchar(225), address varchar(225), salary varchar(225))")
    cur.execute("create table if not exists Suplier(Invoice integer primary key autoincrement, name text, contact text, description text)")
    cur.execute("create table if not exists category(cid integer primary key autoincrement, name text)")
    cur.execute("create table if not exists product(pid integer primary key autoincrement, supplier varchar(225), category varchar(225), name varchar(225), price varchar(225), qty varchar(225), status varchar(225))")
    con.commit()

create_db()
