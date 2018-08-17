from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

app01 = Flask('app01')
app02 = Flask('app02')


@app01.route('/login')
def login():
    return 'app01.login'


@app01.route('/index')
def index():
    return 'app01.index'


@app02.route('/index')
def index():
    return 'app02.index'


dm = DispatcherMiddleware(app01, {
    '/app02': app02,
})

if __name__ == '__main__':
    run_simple('localhost', 5000, dm)
