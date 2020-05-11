from flask import Flask, render_template, request, url_for
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        csvfile = pd.read_csv(f)

    return render_template('data.html', data=csvfile.to_html(classes='table', header=False, index=False))

if __name__ == '__main__':
    app.run(debug=True)