import psycopg2

conn = psycopg2.connect(
    host ="localhost",
    database ="flask_db",
    port = 5432,
    user ="postgres",
    password  = 12345678

)                       
cur = conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS customers(id SERIAL PRIMARY KEY, name VARCHAR(255),age INTEGER,email VARCHAR(255) UNIQUE)''')
cur.execute(''' INSERT INTO customers(name,age,email) VALUES('jerri', 22,'jerri@gmail.com'),('jeshly',25,'jeshly@gmail.com')ON CONFLICT (email) DO NOTHING''')

conn.commit()
cur.close()
conn.close()

print("table created successfully")