from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meditate')
def meditate():
    return render_template('meditate.html')

@app.route('/dashboard')
def dashboardwhale():
    cmd = 'python3 whaleplot.py'
    os.system(cmd)
    return render_template('dashboard.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)