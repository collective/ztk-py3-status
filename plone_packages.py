#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json


PACKAGES = [
  # plone packages
  'Plone',
  'plone.alterego',
  'plone.api',
  'plone.app.caching',
  'plone.app.content',
  'plone.app.contentlisting',
  'plone.app.contentmenu',
  'plone.app.contentrules',
  'plone.app.contenttypes',
  'plone.app.customerize',
  'plone.app.dexterity',
  'plone.app.discussion',
  'plone.app.event',
  'plone.app.i18n',
  'plone.app.intid',
  'plone.app.iterate',
  'plone.app.layout',
  'plone.app.linkintegrity',
  'plone.app.lockingbehavior',
  'plone.app.multilingual',
  'plone.app.portlets',
  'plone.app.querystring',
  'plone.app.redirector',
  'plone.app.registry',
  'plone.app.relationfield',
  'plone.app.robotframework',
  'plone.app.testing',
  'plone.app.textfield',
  'plone.app.theming',
  'plone.app.upgrade',
  'plone.app.users',
  'plone.app.uuid',
  'plone.app.versioningbehavior',
  'plone.app.viewletmanager',
  'plone.app.vocabularies',
  'plone.app.widgets',
  'plone.app.workflow',
  'plone.app.z3cform',
  'plone.autoform',
  'plone.batching',
  'plone.behavior',
  'plone.browserlayer',
  'plone.cachepurging',
  'plone.caching',
  'plone.contentrules',
  'plone.dexterity',
  'plone.event',
  'plone.folder',
  'plone.formwidget.namedfile',
  'plone.formwidget.recurrence',
  'plone.i18n',
  'plone.indexer',
  'plone.intelligenttext',
  'plone.keyring',
  'plone.locking',
  'plone.memoize',
  'plone.namedfile',
  'plone.outputfilters',
  'plone.portlet.collection',
  'plone.portlet.static',
  'plone.portlets',
  'plone.protect',
  'plone.recipe.zope2instance',
  'plone.registry',
  'plone.reload',
  'plone.resource',
  'plone.resourceeditor',
  'plone.rest',
  'plone.restapi',
  'plone.rfc822',
  'plone.scale',
  'plone.schema',
  'plone.schemaeditor',
  'plone.session',
  'plone.stringinterp',
  'plone.subrequest',
  'plone.supermodel',
  'plone.synchronize',
  'plone.testing',
  'plone.theme',
  'plone.tiles',
  'plone.transformchain',
  'plone.uuid',
  'plone.z3cform',
  'plonetheme.barceloneta',
  'Products.CMFPlone',

  # zope packages
  'ZODB',
  'ZODB3',
  'Zope2',
  'Zope',
  'zope.annotation',
  'zope.app.locales',
  'zope.browser',
  'zope.browsermenu',
  'zope.browserpage',
  'zope.browserresource',
  'zope.cachedescriptors',
  'zope.component',
  'zope.componentvocabulary',
  'zope.configuration',
  'zope.container',
  'zope.contentprovider',
  'zope.contenttype',
  'zope.copy',
  'zope.deferredimport',
  'zope.deprecation',
  'zope.dottedname',
  'zope.event',
  'zope.exceptions',
  'zope.filerepresentation',
  'zope.globalrequest',
  'zope.hookable',
  'zope.i18n',
  'zope.i18nmessageid',
  'zope.interface',
  'zope.intid',
  'zope.keyreference',
  'zope.lifecycleevent',
  'zope.location',
  'zope.pagetemplate',
  'zope.processlifetime',
  'zope.proxy',
  'zope.ptresource',
  'zope.publisher',
  'zope.ramcache',
  'zope.schema',
  'zope.security',
  'zope.sendmail',
  'zope.sequencesort',
  'zope.site',
  'zope.size',
  'zope.structuredtext',
  'zope.tal',
  'zope.tales',
  'zope.testbrowser',
  'zope.testing',
  'zope.testrunner',
  'zope.traversing',
  'zope.viewlet',

  # products
  'Products.BTreeFolder2',
  'Products.CMFCore',
  'Products.CMFDiffTool',
  'Products.CMFDynamicViewFTI',
  'Products.CMFEditions',
  'Products.CMFFormController',
  'Products.CMFPlacefulWorkflow',
  'Products.CMFQuickInstallerTool',
  'Products.CMFUid',
  'Products.DCWorkflow',
  'Products.ExtendedPathIndex',
  'Products.ExternalMethod',
  'Products.GenericSetup',
  'Products.MailHost',
  'Products.MimetypesRegistry',
  'Products.PlonePAS',
  'Products.PluggableAuthService',
  'Products.PluginRegistry',
  'Products.PortalTransforms',
  'Products.PythonScripts',
  'Products.ResourceRegistries',
  'Products.Sessions',
  'Products.SiteErrorLog',
  'Products.StandardCacheManagers',
  'Products.statusmessages',
  'Products.TemporaryFolder',
  'Products.ZCatalog',
  'Products.ZCTextIndex',
  'Products.ZopeVersionControl',

  # other zopeish packages
  'AccessControl',
  'Acquisition',
  'borg.localrole',
  'BTrees',
  'Chameleon',
  'collective.monkeypatcher',
  'DateTime',
  'diazo',
  'DocumentTemplate',
  'ExtensionClass',
  'five.customerize',
  'five.intid',
  'five.localsitemanager',
  'Missing',
  'mockup',
  'MultiMapping',
  'Persistence',
  'persistent',
  'Record',
  'repoze.xmliter',
  'RestrictedPython',
  'roman',
  'tempstorage',
  'transaction',
  'z3c.autoinclude',
  'z3c.caching',
  'z3c.form',
  'z3c.formwidget.query',
  'z3c.objpath',
  'z3c.pt',
  'z3c.relationfield',
  'z3c.zcmlhook',
  'zc.lockfile',
  'zc.recipe.egg',
  'zc.relation',
  'ZConfig',
  'zdaemon',
  'ZEO',
  'zExceptions',

  # testing
  'FormEncode',
  'manuel',
  'mock',
  'robotframework',
  'robotframework_debuglibrary',
  'robotframework_selenium2library',
  'robotframework_seleniumlibrary',
  'robotframework_python3',
  'robotsuite',
  'selenium',
  'WebTest',

  # externals
  'AuthEncoding',
  'Babel',
  'beautifulsoup4',
  'certifi',
  'chardet',
  'cssselect',
  'decorator',
  'docutils',
  'feedparser',
  'freezegun',
  'future',
  'idna',
  'jsonschema',
  'lxml',
  'Markdown',
  'PasteDeploy',
  'pbr',
  'Pillow',
  'piexif',
  'ply',
  'prompt_toolkit',
  'pyScss',
  'python_dateutil',
  'python_gettext',
  'Pygments',
  'pytz',
  'PyJWT',
  'requests',
  'setuptools',
  'simplejson',
  'six',
  'slimit',
  'Unidecode',
  'urllib3',
  'waitress',
  'wcwidth',
  'WebOb',
  'WSGIProxy2',
  'zc.buildout',
  'zodbpickle',
]
COLLECTIVE_PACKAGES = [
  'collective.xmltestreport',
  'collective.MockMailHost',
  'icalendar',
  'plone.app.locales',
  'Products.DateRecurringIndex',
]
LOWERCASE_PACKAGES = [x.lower() for x in PACKAGES]
MISSING_PACKAGES = LOWERCASE_PACKAGES[:]

FINAL_PACKAGES = []

plone_packages = json.load(open('plone_packages.json'))
zope_packages = json.load(open('zope_packages.json'))
github_packages = {}
for pkg in plone_packages + zope_packages:
    github_packages[pkg['name'].lower()] = pkg

for pkg in LOWERCASE_PACKAGES:
    if pkg in github_packages:
        FINAL_PACKAGES.append(github_packages[pkg])
        MISSING_PACKAGES.remove(pkg)
    elif pkg == 'zope2':
        data = github_packages['zope']
        data['name'] = 'Zope2'
        FINAL_PACKAGES.append(data)
        MISSING_PACKAGES.remove(pkg)

for pkg in MISSING_PACKAGES:
    FINAL_PACKAGES.append(
        {
            'name': pkg,
            'source_web_url': 'https://pypi.python.org/pypi/{0}'.format(pkg),
        }
    )

for pkg in COLLECTIVE_PACKAGES:
    FINAL_PACKAGES.append(
        {
            'name': pkg,
            'source_web_url': 'https://pypi.python.org/pypi/{0}'.format(pkg),
            'github_web_url': 'https://github.com/collective/{0}'.format(pkg),
        }
    )

with open('packages.json', 'w') as packages_file:
    json.dump(
        FINAL_PACKAGES,
        packages_file,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )
