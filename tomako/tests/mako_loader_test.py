# coding: utf-8
import os
import unittest

from tornado.escape import to_unicode

from tomako.loader import MakoTemplateLoader


class MakoTemplateLoaderTest(unittest.TestCase):
    def setUp(self):
        path = os.path.join(os.path.dirname(__file__), "templates")
        self.loader = MakoTemplateLoader(path)

    def test_mako_syntax_in_utf8_file(self):
        tmpl = self.loader.load("utf8.html")
        result = tmpl.generate(name='my friend')
        self.assertEqual(to_unicode(result).strip(), u"H\u00e9llo my friend")
