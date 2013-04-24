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

.. code-block:: python

    from tomako import MakoTemplateLoader

    conf = {
        'template_loader': MakoTemplateLoader('/full/template/path')
    }
    app = Application(urls, **conf)

If you can't for any reason modify the ``template_loader``
configuration or you want to use Mako as a template engine only on
some handlers, you can overwrite ``RequestHandler.create_template_loader``.

.. code-block:: python

    from tornado.web import RequestHandler
    from tomako import MakoTemplateLoader

    class MyHandler(RequestHandler):
        def create_template_loader(self, template_path):
            return MakoTemplateLoader(template_path)

Tornado UIModules
-----------------

Tomako has basic support for Tornado's UIModules_. You must include a
special namespace called ``tomako.template`` in your templates:

.. code-block:: python

    # Your python file
    from tornado.web import UIModule

    class MyModule(UIModule):
        def render(self, arg1, arg2):
            # do something with args here...
            return 'some string'

.. code-block:: html

    <!-- Your template -->
    <%namespace name="tomako" module="tomako.template" />

    <%tomako:ui uiclass="your.project.module.MyModule" arg1="value1" arg2="value2" />

Install
-------

.. code-block:: shell

    pip install tomako

To-Do
-----

 * Improve support on UIModules

License
-------

This work is licensed under MIT license (see LICENSE file).

.. _UIModules: http://www.tornadoweb.org/en/stable/overview.html#ui-modules
