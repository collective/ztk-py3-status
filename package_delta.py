#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Get a list of packages missing/not needed on plone_packages.py

Script to update the manual list of packages maintained in plone_packages.py.

It needs a checkout of buildout.coredev branch 5.1 in ../test after running
buildout -c core.cfg, i.e.:
    cd ..
    git clone --depth 1 git@github.com:plone/buildout.coredev test
    cd test
    virtualenv-2.7 .
    source bin/activate
    pip install -r requirements.txt
    buildout -c core.cfg

Then run this script and update plone_packages.py accordingly to the output.
"""
import re


RELEASED_EGG_RE = re.compile(
    r'.buildout/eggs/(?P<pkg>[\w\d.]+)-'
)
DEV_EGG_RE = re.compile(
    r'src/(?P<pkg>[\w\d.]+)'
)
SINGLE_PKG_STRING = re.compile(
    r'\s+\'(?P<pkg>[\w\d.]+)\','
)

PLONE_PACKAGES = 'plone_packages.py'
BIN_TEST = '../test/bin/test'


def get_bin_test_packages():
    packages = []
    with open(BIN_TEST) as bintest:
        for line in bintest.readlines():
            if 'import os' in line:
                break
            packages.append(process_bin_test_line(line))

    # remove None
    return set(packages) - {None, }


def process_bin_test_line(line):
    package = ''
    if '.egg' in line:
        result = RELEASED_EGG_RE.search(line)
        package = process_regex_result(result, line)
    elif '/src/' in line:
        result = DEV_EGG_RE.search(line)
        package = process_regex_result(result, line)

    return package


def process_regex_result(result, line):
    package = ''
    if result:
        package = result.group('pkg')
    else:
        print(
            'Could not find pkg on line {0}'.format(
                line.strip()
            )
        )
    return package


def get_packages_in_plone_packages():
    found = []
    with open(PLONE_PACKAGES) as pkgspy:
        for line in pkgspy.readlines():
            if 'LOWERCASE_PACKAGES' in line:
                break

            match = SINGLE_PKG_STRING.search(line)
            if match:
                found.append(match.group('pkg'))

    return set(found)


if __name__ == '__main__':
    test_pkgs = get_bin_test_packages()
    report_pkgs = get_packages_in_plone_packages()

    print('MISSING PACKAGES')
    print(sorted(test_pkgs - report_pkgs))
    print('PACKAGES NOT NEEDED')
    print(sorted(report_pkgs - test_pkgs))
