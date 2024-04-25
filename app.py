from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/mytrip')
def mytrip():
    return render_template('mytrips.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/cal')
def cal():
    return render_template('cal.html')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

if __name__ == '__main__':
    app.run(debug=True)
