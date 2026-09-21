import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="films_lab",
    user="postgres",
    password="admin"
)

cur = conn.cursor()
cur.execute("SELECT Название, Год FROM films WHERE Год > 2010;")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()