"""
# coding:utf-8
@Time    : 2021/09/22
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : __init__.py
@Desc    : __init__
@Software: PyCharm
"""
from flask import Flask, render_template
from src.utils import current_time
from src.view.application_obj import ao_bp


def create_app():
    app = Flask(__name__)

    @app.get('/')
    def index():
        return render_template('index.html')

    # register a context processor variable by decorator
    @app.context_processor
    def app_name():
        return dict(app_name='Flask Api')

    # register a context processor variable by context_processor function
    register_context_processor(app)

    # register a context processor function by decorator
    @app.context_processor
    def format_time():
        import datetime

        def current_time(fmt='%Y-%m-%d'):
            return datetime.datetime.now().strftime(fmt)

        return dict(fmt_ct=current_time)

    register_blueprint(app)
    return app


def register_context_processor(app: Flask):
    app.context_processor(current_time)


def register_blueprint(app: Flask):
    app.register_blueprint(ao_bp)
