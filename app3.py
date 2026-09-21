import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="films_lab",
    user="postgres",
    password="admin"
)

cur = conn.cursor()
cur.execute("SELECT Название, Режиссёр, Год FROM films;")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()