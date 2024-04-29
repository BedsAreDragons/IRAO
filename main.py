from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/org')
def org():
    return render_template('342698.pdf')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
