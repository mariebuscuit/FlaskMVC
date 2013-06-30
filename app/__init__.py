# coding: utf-8

from flask import Flask
from app.controller import blueprints
import app.handler.errorhandler
import app.handler.after_request
import app.handler.before_request

class App(Flask):

    def __init__(self, config):
        super(App, self).__init__(__name__)

        #アプリ全体のエラーハンドラの登録
        app.handler.errorhandler.add(self)
        #アプリ全体のアフターリクエストの登録
        app.handler.after_request.add(self)
        #アプリ全体のビフォアーリクエストの登録
        app.handler.before_request.add(self)

        #blueprintの登録
        for blueprint in blueprints:
            self.register_blueprint(blueprint)
        



