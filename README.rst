Plone on Python 3 porting status
================================

Usage:

.. code-block:: shell

  ./update.sh

This takes a while
(8 minutes just to get PyPI status; more to download source distributions).

Example output::

  [{"name": "zope.interface",
    "version": "4.0.3",
    "supports": ["2.6", "2.7", "3.2", "3.3", "pypy"]},
    "supports_py3": true,
    "requires": ["setuptools"],
    "blockers": [],
    "blocks": [],
    "sdist_url": "http://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.0.3.tar.gz",
    "source_web_url": "https://github.com/zopefoundation/zope.interface",
    "github_web_url": "https://github.com/zopefoundation/zope.interface",
    "svn_web_url": "http://zope3.pov.lt/trac/browser/zope.interface",
    "removed_from_svn": false},
   ...]


Caching
-------

``get_pypi_status.py`` script caches metadata received from PyPI in ``./cache/meta/\*.json`` for 24 hours by default.
You can override these settings with:

.. code-block:: shell

  ./get_pypi_status.py --cache-dir=~/.cache/pypi-meta --cache-max-age=3600

The sdist cache used by ``get_deps.py`` is:

a) configurable, and

b) compatible with buildout

If you use a shared buildout cache,
you can speed up the initial dependency extraction with:

.. code-block:: shell

  ./get_deps.py --cache-dir=~/.buildout/cache/dist < status.json > deps.json

.. note:: You'll have to edit ``update.sh``
