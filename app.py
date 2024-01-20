from flask import Flask
import core.deep_google as dg
import util.proxy_util as pu
import util.flask_util as fu
from flask import Blueprint, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/trans')
def trans():
    text = fu.param("text", request)
    target = fu.param("target", request)
    return dg.trans(text, target=target)


if __name__ == '__main__':
    app.run()

if app.debug:
    pu.enable()
