from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return"<2>"

@app.route('/abaut')
def abaut():
  return render_template('abaut.html')





app.run(host="0.0.0.0",port=8020)



#heroku piregestret
