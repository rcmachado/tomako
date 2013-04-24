# coding: utf-8
from tornado.web import UIModule


class DummyUI(UIModule):
    def render(self, arg1, arg2):
        return 'arg1=%s|arg2=%s' % (arg1, arg2)
