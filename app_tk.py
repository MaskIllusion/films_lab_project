from tkinter import *
from tkinter import ttk
import psycopg


def save_film():
    nazvanie = entry_name.get()
    rezhisser = entry_dir.get()
    god = int(entry_year.get())
    minuty = int(entry_min.get())

    conn = psycopg.connect(
        host="localhost",
        dbname="films_lab",
        user="postgres",
        password="admin"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO films (Название, Режиссёр, Год, Минуты) VALUES (%s, %s, %s, %s);",
        (nazvanie, rezhisser, god, minuty)
    )
    conn.commit()
    cur.close()
    conn.close()
    label["text"] = "Добавлено: " + nazvanie


root = Tk()
root.title("Добавить фильм")
root.geometry("280x280")

ttk.Label(root, text="Название").pack(anchor=NW, padx=6, pady=2)
entry_name = ttk.Entry()
entry_name.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Режиссёр").pack(anchor=NW, padx=6, pady=2)
entry_dir = ttk.Entry()
entry_dir.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Год").pack(anchor=NW, padx=6, pady=2)
entry_year = ttk.Entry()
entry_year.pack(anchor=NW, padx=6, pady=2)

ttk.Label(root, text="Минуты").pack(anchor=NW, padx=6, pady=2)
entry_min = ttk.Entry()
entry_min.pack(anchor=NW, padx=6, pady=2)

btn = ttk.Button(text="Добавить", command=save_film)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()