from flask import Flask

app = Flask('__name__')

@app.route("/meta")
@app.route("/meta/<name>")
@app.route("/meta/<name>/<int:edad>")
def hello_meta(name = None, edad =None ):
 if edad == None :

  return f"<center><h1> Mi otro nombre es : {name} </h1></center>"
  
 else:
  
  return f"<center><h1> Mi otro nombre es : {name} y su edad es : {edad}</h1></center>"
 
 if __name__ == ('__main_') :
    app.run(debug=True)