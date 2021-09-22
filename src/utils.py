"""
# coding:utf-8
@Time    : 2021/09/22
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : utils.py
@Desc    : utils
@Software: PyCharm
"""
import datetime


def current_time(fmt='%Y-%m-%d %H:%M:%S'):
    """
    get current time, display by fmt parameter
    :param fmt: display format default is `%Y-%m-%d %H:%M:%S`
    :return: current time
    """
    return dict(current_time=datetime.datetime.now().strftime(fmt))


def ct_function(fmt='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)
