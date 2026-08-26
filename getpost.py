from flask import Flask, render_template, request

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


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}! Your form has been submitted."
    return render_template('form.html')


    
if __name__ == '__main__':
    app.run(debug=True)