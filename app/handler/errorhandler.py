# coding: utf-8

from utils.controller import InValidException
from flask import make_response

def add(app):
    """
    アプリケーション全体のエラーハンドラを登録する
        @app.errorhandler(FooException)
        def bar():
            ......
    """
    
    @app.errorhandler(InValidException)
    def invalid_exception(e):
        message, status = e
        resp = make_response(render_template('invalid.html', message=message, status=status), status)
        return resp

