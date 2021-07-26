from os import WIFCONTINUED
from flask import Flask,render_template,request,abort
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
import json,os.path

app = Flask(__name__)
app.secret_key = "vinland"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/your-url',methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
       urls={}
       if os.path.exists('urls.json'):
           with open('urls.json') as urls_file:
               urls = json.load(urls_file)
       if request.form['code'] in urls.keys():
           flash('This short name has been taken. Please try another')
           return redirect(url_for('index'))

       urls[request.form['code']] = {'url':request.form['url']}
       with open('urls.json','w') as url_file:
           json.dump(urls,url_file)

       return render_template('your_url.html',code=request.form['code'])    
    else:
        return redirect(url_for('index'))


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
           urls = json.load(urls_file)
           if code in urls.keys():   
               if 'url' in urls[code].keys():
                   return redirect(urls[code]['url'])
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404
