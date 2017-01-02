#coding= utf-8
from flask import Flask, request, url_for, render_template, flash
from flask import abort
from models import User
#实例化一个flask对象
app = Flask(__name__)
app.secret_key = '123'

#路由
@app.route('/')
def hello_world():
    flash('hello bing')
    return render_template('index.html') #渲染模板

@app.route('/user')
def user_index():
    user = User(1, 'bing')
    return render_template('user_index.html', user=user)

# @app.route('/user/<id>')
# def user_id( id ):
#     user = None
#     if int(id) == 1:
#         user = User(1, 'bing')
#     return render_template('user_id.html', user=user)

@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'bing'+str(i))
        users.append(user)
    return render_template("user_list.html", users = users)

@app.route('/one')
def one_base():
    return  render_template('one.html')

@app.route('/two')
def two_base():
    return  render_template('two.html')


@app.route('/query_user')
def query_user():
    id=request.args.get('id')
    return 'hello user'+ id

@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')

@app.route('/login',methods =['post'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash('please enter your username')
        return render_template('index.html')
    if not password:
        flash('please enter your password')
        return render_template('index.html')
    if username == 'bing' and password == '123456':
        flash('login successfully')
        return render_template('index.html')
    else:
        flash('username or password is wrong')
        return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/user/<user_id>')
def user(user_id):
    if int(user_id)==1:
        return render_template('user.html')
    else:
        abort(404)
        return render_template('404.html')

# 默认路径为localhost，端口为5000
if __name__ == '__main__':
    app.run()
