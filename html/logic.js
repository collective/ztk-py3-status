  $(function() {
    // empty strings are for spacing (because I can't figure out how to achieve that effect with CSS)
    var known_versions = ['', '2.7', '', '3.3', '3.4', '3.5', '3.6', '', 'PyPy', ''];
    $.getJSON('data.json', function(data, textStatus, jqXHR) {
        var tbl = $('#support-table');
        tbl.html(
          '<colgroup>' +
            '<col class="package-name"></col>' +
            '<col class="package-vcs"></col>' +
            '<col class="package-version"></col>' +
            '<col class="supports-py3"></col>' +
          '</colgroup>' +
          '<colgroup>' +
            '<col class="version-column" span="'+known_versions.length+'"></col>' +
          '</colgroup>' +
          '<colgroup>' +
            '<col class="blockers"></col>' +
            '<col class="blocks"></col>' +
            '<col class="depgraph"></col>' +
            '<col class="depgraph"></col>' +
            '<col class="buildstatus"></col>' +
          '</colgroup>' +
          '<thead>' +
            '<tr>' +
              '<th class="package-name" rowspan="2">Package</th>' +
              '<th class="package-vcs" rowspan="2">VCS</th>' +
              '<th class="package-version" rowspan="2">Version</th>' +
              '<th class="supports-py3" rowspan="2">Supports Python 3</th>' +
              '<th colspan="'+known_versions.length+'">Python Versions</th>' +
              '<th class="blockers" rowspan="2" title="Direct dependencies that have not been ported to Python 3 yet">Blockers</th>' +
              '<th class="blocks" rowspan="2" title="Packages that cannot be ported to Python 3 yet because they depend on this package">Blocks</th>' +
              '<th class="depgraph" rowspan="2">Dep. Graph</th>' +
              '<th class="depgraph" rowspan="2">(incl. extras)</th>' +
              '<th class="buildstatus" rowspan="2">Build status</th>' +
            '</tr>' +
            '<tr>' +
            '</tr>' +
          '</thead>' +
          '<tbody>' +
          '</tbody>');
        var last_header_row = tbl.find('thead > tr:last');
        $.each(known_versions, function(idx, v) {
            var th = $('<th class="version-column">').text(v);
            th.appendTo(last_header_row);
        });
        var tbody = tbl.find('tbody');
        data.sort(function(a, b) {
            var r = 0;
            if (r == 0) r = !!b.version - !!a.version;        // unreleased last
            if (r == 0) r = b.supports_py3 - a.supports_py3;  // py3k-supporting first
            if (r == 0) r = !!b.supports.length - !!a.supports.length;
            if (r == 0) r = a.blockers.length - b.blockers.length;
            if (r == 0) r = (a.name < b.name ? -1 : 1); // assume a.name != b.name
            return r;
        });
        var pypi_url = 'https://pypi.python.org/pypi/';
        var count_py3 = 0, count_nopy3 = 0, count_unreleased = 0;
        var filter = null;
        $.each(location.search.slice(1).split(';'), function(idx, arg) {
            arg = arg.split('=')
            if (arg[0] == 'filter') {
                filter = arg[1];
            }
        });
        $.each(data, function(idx, pkg) {
            if (filter && pkg.name.slice(0, filter.length) != filter)
                return;
            var row = $('<tr>'), td;
            // package name
            td = $('<td>')
                  .append(pkg.version ? $('<a>').text(pkg.name).attr('href', pypi_url + pkg.name)
                                      : pkg.name)
                  .appendTo(row);
            // package vcs
            var uses_git = (pkg.github_web_url && (!pkg.svn_web_url || pkg.removed_from_svn));
            var primary_url = uses_git ? pkg.github_web_url : pkg.svn_web_url;
            td = $('<td>');
            td.addClass('vcs');
            var a_link = $('<a>');
            a_link.attr('href', primary_url);
            a_link.addClass(uses_git ? 'git' : 'svn');
            a_link.text(uses_git ? 'Git' : 'SVN');
            td.append(a_link);
            td.appendTo(row);
            if (pkg.svn_web_url && pkg.svn_web_url != primary_url) {
                var a = $('<a>').attr('href', pkg.svn_web_url)
                                  .addClass('svn secondary')
                                  .text('(SVN)');
                if (pkg.removed_from_svn)
                   a.text('(svn)')
                    .attr('title', 'moved to Github');
                td.append(a);
            }
            if (pkg.github_web_url && pkg.github_web_url != primary_url) {
                var a = $('<a>').attr('href', pkg.github_web_url)
                                  .addClass('git secondary')
                                  .text('(Git)');
                if (pkg.empty_github_repo)
                   a.text('(git)')
                    .attr('title', 'empty Github repository');
                td.append(a);
            }
            // package version
            td = $('<td>')
                  .addClass('version')
                  .text(pkg.version || '(unreleased)')
                  .appendTo(row);
            if (!pkg.version) td.addClass('unreleased');
            // python 3 support
            td = $('<td>')
                  .text(pkg.supports_py3 ? 'yes' : 'no')
                  .addClass(pkg.supports_py3 ? 'supported' :
                            pkg.version ? 'unsupported' : 'unknown')
                  .appendTo(row);
            if (pkg.supports_py3) count_py3 += 1;
            else if (pkg.version) count_nopy3 += 1;
            else count_unreleased += 1;
            // detailed python version support
            $.each(known_versions, function(idx, v) {
                if (!v) {
                    // hack to add spacing because I suck at CSS
                    row.append('<td>&nbsp;</td>');
                } else if (pkg.supports.length == 0) {
                    row.append('<td class="unknown">?</td>');
                } else if ($.inArray(v.toLowerCase(), pkg.supports) != -1) {
                    row.append('<td class="supported">+</td>');
                } else if ($.inArray(v.split('.')[0], pkg.supports) != -1) {
                    row.append('<td class="probably" title="supports Python ' + v.split('.')[0] + ', minor versions not listed">?</td>');
                } else {
                    row.append('<td class="unsupported">-</td>');
                }
            });
            // blockers
            var blockers = pkg.blockers || [];
            td = $('<td>')
                  .addClass('blockers')
                  .text(blockers.length)
                  .attr('title', blockers.join('\n'))
                  .appendTo(row);
            if (pkg.supports_py3 || !pkg.version)
                td.addClass('blockers-na')
            else if (blockers.length == 0)
                td.addClass('no-blockers');
            // blocks
            var blocks = pkg.blocks || [];
            td = $('<td>')
                  .addClass('blocks')
                  .text(blocks.length)
                  .attr('title', blocks.join('\n'))
                  .appendTo(row);
            if (pkg.supports_py3 || !pkg.version)
                td.addClass('blocks-na')
            else if (blocks.length == 0)
                td.addClass('blocks-nothing');
            // dependency graph
            td = $('<td>')
                  .addClass('depgraph')
                  .append($('<a>').attr('href', 'deps/' + pkg.name + '.svg')
                                  .addClass('svg')
                                  .text('SVG'))
                  .appendTo(row);
            // dependency graph (with extras)
            td = $('<td>')
                  .addClass('depgraph')
                  .append($('<a>').attr('href', 'deps-with-extras/' + pkg.name + '.svg')
                                  .addClass('svg')
                                  .text('SVG'))
                  .appendTo(row);
            // build status
            td = $('<td>')
                  .addClass('buildstatus');
            if (pkg.github_web_url && !pkg.empty_github_repo &&
                pkg.github_web_url.slice(0, 19) == "https://github.com/") {
                var travis_url = 'https://travis-ci.org/' + pkg.github_web_url.slice(19);
                td.append($('<a>').attr('href', travis_url)
                                  .append($('<img>').attr('src', travis_url + '.svg?branch=master')));
            }
            td.appendTo(row);
            // that's it for this row
            row.appendTo(tbody);
        });
        var lastModified = jqXHR.getResponseHeader("Last-Modified");
        $("#last-modified").text("Currently shown dataset was computed on " + lastModified + ".");
        var count_released = count_py3 + count_nopy3;
        var progress = $("#progress")
              .attr('value', count_py3)
              .attr('max', count_released)
              .attr('title', count_py3 + ' out of ' + count_released + ' packages ported')
              .text(count_py3 + ' out of ' + count_released + ' packages ported')
              .attr('style', null);
    });
  });
