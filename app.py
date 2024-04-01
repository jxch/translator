import logging

from flask import Flask
from flask import request

import core.deep_google as dg
import util.flask_util as fu
import util.proxy_util as pu

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

if app.debug:
    pu.enable()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/trans')
def trans():
    text = fu.param("text", request)
    target = fu.param("target", request)
    source = fu.param("source", request)
    engine = fu.param("engine", request)
    target = target if target else 'zh-CN'
    source = source if source else 'auto'
    engine = engine if engine else 'GoogleTranslator'
    return dg.trans(text, target=target, source=source, engine=engine)


@app.route('/support_engine')
def support_engine():
    return ['GoogleTranslator', 'MyMemoryTranslator']


if __name__ == '__main__':
    app.run()
