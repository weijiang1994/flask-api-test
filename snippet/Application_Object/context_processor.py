"""
# coding:utf-8
@Time    : 2021/09/22
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : context_processor.py
@Desc    : context_processor
@Software: PyCharm
"""
from flask import Flask
import datetime

app = Flask(__name__)


# use decorator
@app.context_processor()
def cur_day():
    return datetime.date.today()


# context function
@app.context_processor()
def get_uuid():
    import uuid

    def _uuid():
        return uuid.uuid3()

    return dict(uuid=_uuid)


def current_time():
    return dict(current_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# use context_processor function
app.context_processor(current_time)
if __name__ == '__main__':
    app.run()
