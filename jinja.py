

### jinja2 Template Engine

'''
{{  }} expression to print output in html page
{%  %} control structure for loops and conditions
{#  #} comments in jinja2 template
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "<html><body><h1>Welcome to the index page!</h1></body></html>"

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


##variable rules
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"

    return render_template('result.html', result=res)

##variable rules
@app.route('/successers/<int:score>')
def successers(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"

    expression = {'score': score, "res":res}

    return render_template('result1.html', result=expression)

##variable rules
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html', result=score)


@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html', result=score)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total = (science + math + c + data_science)/4

    else:
        return render_template('getresults.html')
    return redirect(url_for('successers', score=total))
    


    
if __name__ == '__main__':
    app.run(debug=True)