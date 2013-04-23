Tornado + Mako = tomako
=======================

Tomako is a tiny library designed to provide an easy way to use Mako
as a template engine for Tornado.

This lib was tested with Tornado 2.3/2.4 and Mako 0.7.2, but should
work in other versions - although it wasn't tested in other versions.

Usage
-----

The recommended approach is to pass ``template_loader`` configuration
to ``Application`` class.

```
from tomako import MakoTemplateLoader

conf = {
    'template_loader': MakoTemplateLoader('/full/template/path')
}
app = Application(urls, **conf)
```

If you can't for any reason modify the ``template_loader``
configuration or you want to use Mako as a template engine only on
some handlers, you can overwrite ``RequestHandler.create_template_loader``.

```
from tornado.web import RequestHandler
from tomako import MakoTemplateLoader

class MyHandler(RequestHandler):
    def create_template_loader(self, template_path):
        return MakoTemplateLoader(template_path)
```

Install
-------

```
pip install tomako
```

License
-------

This work is licensed under MIT license (see LICENSE file).
