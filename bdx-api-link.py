
from flask import Flask
from flask import render_template
app = Flask(__name__)   # Flask constructor


@app.route('/')
def hello():
    return "Hello le monde"

@app.route('/0')
def hollo():
    return render_template('initial.html')

@app.route('/1')
def holla():
    return render_template('cssPulling.html')

@app.route('/2')
def hollb():
    return render_template('csstemplate.html')






if __name__=='__main__':
    app.run()

