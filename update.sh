#!/bin/sh
# update dynamic files in /var/www/zope3.pov.lt/py3/
# /srv/ztk-py3-status/ is a checkout of https://github.com/mgedmin/ztk-py3-status
# /srv/ztk-py3-status/*.py require python3
# sponge requires moreutils
# convert requires imagemagick
# dot and neato require graphviz

cache_dir="/srv/py_cache"
mkdir $cache_dir

cd /srv/py3 || exit 1

echo "start"
/srv/ztk-py3-status/plone_packages.py > packages.json
echo "pypi"
/srv/ztk-py3-status/get_pypi_status.py --cache-max-age=300 < packages.json | sponge status.json
echo "deps"
/srv/ztk-py3-status/get_deps.py --cache-dir=$cache_dir < status.json | sponge deps.json
echo "blockers"
/srv/ztk-py3-status/count_blockers.py < deps.json | sponge data.json
echo "graphs"
/srv/ztk-py3-status/depgraph.py < data.json | sponge deps.dot

echo "big graphs"
neato -Tsvg deps.dot | sponge deps.svg
neato -Tpng deps.dot | sponge deps.png
convert deps.png -resize 128x128 - | sponge deps-thumb.png

mkdir -p deps/
mkdir -p deps-with-extras/
packages=$(/srv/ztk-py3-status/list_packages.py < data.json)
for pkg in $packages; do
    echo "graphs for $pkg"
    /srv/ztk-py3-status/depgraph.py $pkg -b < data.json | sponge deps/$pkg.dot
    /srv/ztk-py3-status/depgraph.py $pkg -a -e < data.json | sponge deps-with-extras/$pkg.dot

    dot -Tsvg deps/$pkg.dot | sponge deps/$pkg.svg
    dot -Tsvg deps-with-extras/$pkg.dot | sponge deps-with-extras/$pkg.svg

    dot -Tpng deps/$pkg.dot | sponge deps/$pkg.png
    dot -Tpng deps-with-extras/$pkg.dot | sponge deps-with-extras/$pkg.png
done
