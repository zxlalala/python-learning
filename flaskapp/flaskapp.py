#coding= utf-8
from flask import Flask, request, url_for, render_template

#实例化一个flask对象
app = Flask(__name__)

#路由
#dhukjsiuofj
@app.route('/')
def hello_world():
    return render_template('index.html') #渲染模板

@app.route('/user')
def hello_user():
    return 'Hello User!'

@app.route('/user/<id>')
def user_id( id ):
    return 'hello user'+ id

@app.route('/query_user')
def query_user():
    id=request.args.get('id')
    return 'hello user'+ id

@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_user')



# 默认路径为localhost，端口为5000
if __name__ == '__main__':
    app.run()
