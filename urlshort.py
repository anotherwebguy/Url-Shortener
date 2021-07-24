from flask import Flask,render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/your-url',methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
       return render_template('your_url.html',code=request.form['code'])    
    else:
        return redirect(url_for('index'))