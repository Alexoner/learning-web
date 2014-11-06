from flask import Flask ,session,redirect,url_for,escape,request
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
        return '''
        <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    '''
if __name__ == "__main__":
    url_for('static',filename='grouping.css')
    app.run()
