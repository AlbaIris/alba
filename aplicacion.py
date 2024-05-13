from flask import Flask, render_template, request, redirect,url_for
from flask_mail import Mail, Message
app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'e8350258b9a19a'
app.config['MAIL_PASSWORD'] = '5dfc23fd627920'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/proyect')
def proyect():
    return render_template("portafolio.html")
    
@app.route('/mail', methods=['GET','POST'])
def send_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form.get('message')

        msg = Message('Hola Alba Iris, tienes un nuevo contenido de la web:',
                      body=f'Nombre: {name}\nCorreo: {email}\n\nEscribió:\n\n{message}',
                      sender=email,
                      recipients=['Albairiscemas@gmail.com']
        )

        mail.send(msg)
        return render_template('send_mail.html')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)