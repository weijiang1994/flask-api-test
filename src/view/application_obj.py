"""
# coding:utf-8
@Time    : 2021/09/22
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : application_obj.py
@Desc    : application_obj
@Software: PyCharm
"""
from flask import Blueprint, render_template


ao_bp = Blueprint('ao', __name__, url_prefix='/app_obj')


@ao_bp.route('/context_processor')
def ctx_processor():
    return render_template('Application-Object/context_processor.html')
