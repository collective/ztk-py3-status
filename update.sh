#!/bin/sh
# update dynamic files in /var/www/zope3.pov.lt/py3/
# /opt/ztk-py3-status/ is a checkout of https://github.com/mgedmin/ztk-py3-status
# /opt/ztk-py3-status/*.py require python3
# sponge requires moreutils
# convert requires imagemagick
# dot and neato require graphviz

cache_dir=/stuff/pypi-cache

cd /opt/ztk-py3-status || exit 1
git pull -q

cd /var/www/zope3.pov.lt/py3 || exit 1

/opt/ztk-py3-status/get_zope_packages.py > .packages.json.new
test -s .packages.json.new && mv .packages.json.new packages.json
test -s packages.json || exit 1

/opt/ztk-py3-status/get_move_status.py < packages.json | sponge move-status.json
  # NB: github performs rate limiting, so don't go nuts running this script over and over again
/opt/ztk-py3-status/get_pypi_status.py --cache-max-age=300 < move-status.json | sponge status.json
  # pypi metadata will be cached in ./.cache/meta, which is fine by me, for now
/opt/ztk-py3-status/get_deps.py --cache-dir=$cache_dir < status.json | sponge deps.json
/opt/ztk-py3-status/count_blockers.py < deps.json | sponge data.json
/opt/ztk-py3-status/depgraph.py < data.json | sponge deps.dot

neato -Tsvg deps.dot | sponge deps.svg
neato -Tpng deps.dot | sponge deps.png
convert deps.png -resize 128x128 - | sponge deps-thumb.png

mkdir -p deps/
mkdir -p deps-with-extras/
packages=$(/opt/ztk-py3-status/list_packages.py < data.json)
for pkg in $packages; do
    /opt/ztk-py3-status/depgraph.py $pkg -b < data.json | sponge deps/$pkg.dot
    /opt/ztk-py3-status/depgraph.py $pkg -a -e < data.json | sponge deps-with-extras/$pkg.dot
done
for pkg in $packages; do
    dot -Tsvg deps/$pkg.dot | sponge deps/$pkg.svg
    dot -Tsvg deps-with-extras/$pkg.dot | sponge deps-with-extras/$pkg.svg
done
for pkg in $packages; do
    dot -Tpng deps/$pkg.dot | sponge deps/$pkg.png
    dot -Tpng deps-with-extras/$pkg.dot | sponge deps-with-extras/$pkg.png
done
