#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json


PACKAGES = [
  # plone packages
  'Plone',
  'plone.alterego',
  'plone.api',
  'plone.app.blob',
  'plone.app.caching',
  'plone.app.collection',
  'plone.app.content',
  'plone.app.contentlisting',
  'plone.app.contentmenu',
  'plone.app.contentrules',
  'plone.app.contenttypes',
  'plone.app.controlpanel',
  'plone.app.customerize',
  'plone.app.dexterity',
  'plone.app.discussion',
  'plone.app.event',
  'plone.app.folder',
  'plone.app.i18n',
  'plone.app.imaging',
  'plone.app.intid',
  'plone.app.iterate',
  'plone.app.layout',
  'plone.app.linkintegrity',
  'plone.app.lockingbehavior',
  'plone.app.multilingual',
  'plone.app.openid',
  'plone.app.portlets',
  'plone.app.querystring',
  'plone.app.redirector',
  'plone.app.referenceablebehavior',
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
  'plone.openid',
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
  'plone.transformchain',
  'plone.uuid',
  'plone.z3cform',
  'plonetheme.barceloneta',
  'Products.CMFPlone',

  # zope packages
  'ZODB3',
  'Zope2',
  'zope.annotation',
  'zope.app.appsetup',
  'zope.app.intid',
  'zope.app.locales',
  'zope.app.publication',
  'zope.app.publisher',
  'zope.app.wsgi',
  'zope.authentication',
  'zope.broken',
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
  'zope.copypastemove',
  'zope.datetime',
  'zope.deferredimport',
  'zope.deprecation',
  'zope.dottedname',
  'zope.dublincore',
  'zope.error',
  'zope.event',
  'zope.exceptions',
  'zope.filerepresentation',
  'zope.formlib',
  'zope.globalrequest',
  'zope.i18n',
  'zope.i18nmessageid',
  'zope.interface',
  'zope.intid',
  'zope.keyreference',
  'zope.lifecycleevent',
  'zope.location',
  'zope.minmax',
  'zope.pagetemplate',
  'zope.password',
  'zope.principalregistry',
  'zope.processlifetime',
  'zope.proxy',
  'zope.ptresource',
  'zope.publisher',
  'zope.ramcache',
  'zope.schema',
  'zope.security',
  'zope.sendmail',
  'zope.sequencesort',
  'zope.session',
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
  'ZopeUndo',

  # products
  'Products.Archetypes',
  'Products.ATContentTypes',
  'Products.BTreeFolder2',
  'Products.CMFCore',
  'Products.CMFDiffTool',
  'Products.CMFDynamicViewFTI',
  'Products.CMFEditions',
  'Products.CMFFormController',
  'Products.CMFPlacefulWorkflow',
  'Products.CMFQuickInstallerTool',
  'Products.CMFUid',
  'Products.contentmigration',
  'Products.DCWorkflow',
  'Products.ExtendedPathIndex',
  'Products.ExternalEditor',
  'Products.ExternalMethod',
  'Products.GenericSetup',
  'Products.i18ntestcase',
  'Products.MailHost',
  'Products.Marshall',
  'Products.MIMETools',
  'Products.MimetypesRegistry',
  'Products.OFSP',
  'Products.PasswordResetTool',
  'Products.PlacelessTranslationService',
  'Products.PlonePAS',
  'Products.PloneTestCase',
  'Products.PluggableAuthService',
  'Products.PluginRegistry',
  'Products.PortalTransforms',
  'Products.PythonScripts',
  'Products.ResourceRegistries',
  'Products.StandardCacheManagers',
  'Products.statusmessages',
  'Products.validation',
  'Products.ZCatalog',
  'Products.ZCTextIndex',
  'Products.ZopeVersionControl',
  'Products.ZSQLMethods',

  # other zopeish packages
  'AccessControl',
  'Acquisition',
  'archetypes.multilingual',
  'archetypes.schemaextender',
  'borg.localrole',
  'Chameleon',
  'collective.monkeypatcher',
  'DateTime',
  'diazo',
  'DocumentTemplate',
  'ExtensionClass',
  'five.customerize',
  'five.globalrequest',
  'five.intid',
  'five.localsitemanager',
  'five.pt',
  'initgroups',
  'mechanize',
  'Missing',
  'mockup',
  'MultiMapping',
  'Persistence',
  'persistent',
  'Record',
  'repoze.xmliter',
  'RestrictedPython',
  'roman',
  'sourcecodegen',
  'tempstorage',
  'transaction',
  'z3c.autoinclude',
  'z3c.caching',
  'z3c.coverage',
  'z3c.form',
  'z3c.formwidget.query',
  'z3c.objpath',
  'z3c.pt',
  'z3c.relationfield',
  'z3c.template',
  'z3c.zcmlhook',
  'zc.lockfile',
  'zc.recipe.egg',
  'zc.relation',
  'zc.sourcefactory',
  'ZConfig',
  'zdaemon',
  'zExceptions',
  'zLOG',

  # testing
  'coverage',
  'FormEncode',
  'manuel',
  'mock',
  'robotframework',
  'robotframework_debuglibrary',
  'robotframework_ride',
  'robotframework_selenium2library',
  'robotsuite',
  'selenium',
  'unittest2',
  'watchdog',

  # externals
  'argh',
  'Babel',
  'cssmin',
  'cssselect',
  'decorator',
  'docutils',
  'feedparser',
  'future',
  'lxml',
  'mailinglogger',
  'Markdown',
  'pathtools',
  'Pillow',
  'ply',
  'python_dateutil',
  'python_gettext',
  'python_openid',
  'pytz',
  'PyYAML',
  'setuptools',
  'six',
  'slimit',
  'Unidecode',
  'WebOb',
  'wsgi_intercept',
  'zc.buildout',
]
COLLECTIVE_PACKAGES = [
  'collective.elephantvocabulary',
  'collective.xmltestreport',
  'icalendar',
  'plone.app.locales',
  'Products.DateRecurringIndex',
  'Products.SecureMailHost',
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
