from flask import Flask, request, render_template,jsonify,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "albairis"

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registro():
    nombre = request.form['nombre']
    correo = request.form['email']
    password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO registros (Nombre, Gmail, Contraseña) VALUES (%s,%s,%s)", (nombre, correo, password))
    mysql.connection.commit()
    cur.close()  
    return redirect(url_for("login_web"))

@app.route("/acceso")
def login_web():
    return render_template("login.html")
@app.route("/login", methods=["POST"])
def login():
    nombre = request.form["nombre"]
    password = request.form["password"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT Nombre, Gmail, Contraseña FROM registros WHERE Nombre = %s AND Contraseña = %s", (nombre, password))
    user = cur.fetchone() 
    
    
    if user:
        
        return jsonify({"message": "Login successful"})
    else:
        
        return jsonify({"message": "Invalid credentials"}), 401

    



if __name__ == '__main__':
    app.run(debug=True, port=5000)
