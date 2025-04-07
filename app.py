from collections import defaultdict
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, static_folder='static', static_url_path='/')
like_tracker = defaultdict(set)

def get_like_count(post_id):
    # Should get from Database or excel
    return len(like_tracker[post_id])

def increase_like_count(post_id, user_id):
    # should set in database or excel
    like_tracker[post_id].add(user_id)

def decrease_like_count(post_id, user_id):
    # should set in database or excel
    if user_id in like_tracker[post_id]:
        like_tracker[post_id].remove(user_id)

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

@app.route('/like_button')
def like_button():
    return render_template('like_button.html')

@app.route('/view_like')
def view_like():
    post_id = request.args.get('post_id')
    if post_id:
        return str(get_like_count(post_id))
    return "0"

@app.route('/like')
def like():
    post_id = request.args.get('post_id')
    user_id = request.args.get('user_id', 'jackie')
    if post_id and user_id:
        increase_like_count(post_id, user_id)
        return 'OK'
    return 'Error'

@app.route('/unlike')
def unlike():
    post_id = request.args.get('post_id')
    user_id = request.args.get('user_id', 'jackie')
    if post_id and user_id:
        decrease_like_count(post_id, user_id)
        return 'OK'
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)