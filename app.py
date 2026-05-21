from flask import Flask,render_template,request,redirect,url_for
import psycopg2

app =Flask(__name__)

def db_connection():
    conn = psycopg2.connect(
    host ="localhost",
    database ="flask_db",
    port = 5432,
    user ="postgres",
    password  = "12345678")
    return conn

@app.route("/")
def index():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(''' SELECT * FROM customers ORDER BY id''')
    data = cur.fetchall()
    return render_template("index.html",data =data)
@app.route("/create", methods=["post"])
def create():
    conn = db_connection()
    cur = conn.cursor() 
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    cur.execute('''INSERT INTO customers(name,age,email) VALUES(%s,%s,%s)''',(name,age,email))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route("/update",methods=["POST"])
def update():
    conn =db_connection()
    cur =conn.cursor()
    name =request.form['name']
    age =request.form['age']
    email =request.form['email']
    id =request.form['id']
    cur.execute('''UPDATE customers SET name=%s,age=%s,email=%s WHERE id=%s''',(name,age,email,id))
    conn.commit()
    return redirect(url_for('index'))

@app.route("/delete",methods=["POST"])
def delete():
    conn = db_connection()
    cur =conn.cursor()
    id = request.form['id']
    cur.execute('''DELETE FROM customers WHERE id=%s''',(id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug=True)