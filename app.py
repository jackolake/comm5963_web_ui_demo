from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='static', static_url_path='/')

@app.route('/')
def homepage():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/snap_scroll')
def snap_scroll():
    return render_template('snap_scroll.html')

@app.route('/multistep_progress')
def multistep_form():
    return render_template('multistep_progress.html')

if __name__ == '__main__':
    app.run(debug=True)