from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data-analysis')
def data_analysis():
    return render_template('data_analysis.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 