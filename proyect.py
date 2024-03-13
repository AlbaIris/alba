from flask import Flask

app = Flask('__name__')
  
@app.route('/')
@app.route("/calculadora/num1/num2/num3/operaciones")
def hello_proyect(num1, num2, num3, operaciones):
    if operaciones == 'suma':
        return num1+num2+num3 
    if operaciones == 'resta':
       return num1-num2-num3 
    if operaciones == 'multiplicacion':
        return num1*num2*num3
    if operaciones == 'division':
        return num1/num2/num3 
    
    if __name__ == ('__main_') :
     app.run(debug=True)

def hello_proyect(num1, num2, operaciones):
   if operaciones == 'suma':
        return num1+num2 
   if operaciones == 'resta':
       return num1-num2 
   if operaciones == 'multiplicacion':
        return num1*num2
   if operaciones == 'division':
        return num1/num2
    
if __name__ == ('__main_') :
     app.run(debug=True)
