import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="films_lab",
    user="postgres",
    password="admin"
)
cur = conn.cursor()

nazvanie = input("Название: ")
rezhisser = input("Режиссёр: ")
god = int(input("Год: "))
minuty = int(input("Минуты: "))

cur.execute(
    "INSERT INTO films (Название, Режиссёр, Год, Минуты) VALUES (%s, %s, %s, %s);",
    (nazvanie, rezhisser, god, minuty)
)

conn.commit()

print("Строка добавлена.")

cur.execute("SELECT * FROM films;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()