from flask import Flask

app = Flask('__name__')

@app.route('/')
@app.route("/index")
def hello():
    return 'tu nombre es Alba!'

if __name__ == '__main__':
  app.run(debug=True)
