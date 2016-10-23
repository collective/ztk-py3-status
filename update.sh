#!/bin/sh
# update dynamic files in /var/www/zope3.pov.lt/py3/
# /srv/ztk-py3-status/ is a checkout of https://github.com/mgedmin/ztk-py3-status
# /srv/ztk-py3-status/*.py require python3
# sponge requires moreutils
# convert requires imagemagick
# dot and neato require graphviz

cache_dir="/srv/py_cache"
mkdir $cache_dir

echo "start"
/srv/ztk-py3-status/plone_packages.py > packages.json
echo "pypi"
/srv/ztk-py3-status/get_pypi_status.py --cache-max-age=300 < packages.json | sponge status.json
echo "deps"
/srv/ztk-py3-status/get_deps.py --cache-dir=$cache_dir < status.json | sponge deps.json
echo "blockers"
/srv/ztk-py3-status/count_blockers.py < deps.json | sponge html/data.json
echo "graphs"
/srv/ztk-py3-status/depgraph.py < html/data.json | sponge deps.dot

echo "big graphs"
neato -Tsvg deps.dot | sponge html/deps.svg
neato -Tpng deps.dot | sponge html/deps.png
convert html/deps.png -resize 128x128 - | sponge html/deps-thumb.png

mkdir -p html/deps/
mkdir -p html/deps-with-extras/
packages=$(/srv/ztk-py3-status/list_packages.py < html/data.json)
for pkg in $packages; do
    echo "graphs for $pkg"
    /srv/ztk-py3-status/depgraph.py $pkg -b < html/data.json | sponge html/deps/$pkg.dot
    /srv/ztk-py3-status/depgraph.py $pkg -a -e < html/data.json | sponge html/deps-with-extras/$pkg.dot

    dot -Tsvg html/deps/$pkg.dot | sponge html/deps/$pkg.svg
    dot -Tsvg html/deps-with-extras/$pkg.dot | sponge html/deps-with-extras/$pkg.svg
done

cp deps.dot html/deps.dot
