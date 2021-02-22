from flask import Flask, request, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(['flask', 'is', 'awesome'])

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/about')
def about():
    return 'This is a flask demo'

@app.route('/user/<username>') # /user/san /user/2
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>') # /post/23, Not /post/newpost
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>') # /path/just/a/path
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath) 
