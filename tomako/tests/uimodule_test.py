# coding: utf-8
import os
import unittest

import mock
from mako.template import Template
from tornado.escape import to_unicode


class UINamespaceTest(unittest.TestCase):
    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), 'templates')
        self.tpl = Template(filename=os.path.join(path, 'uimodule.html'))

    def test_ui_function_imports_uimodule(self):
        result = self.tpl.render(handler=mock.MagicMock())
        content = to_unicode(result).strip()
        self.assertEqual(content, u'arg1=value1|arg2=value2')
