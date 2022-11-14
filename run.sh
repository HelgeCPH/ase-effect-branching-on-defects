#!/usr/bin/env bash

# TODO: Add more projects
for PROJECT in hadoop camel ignite  # netbeans kafka spark thrift arrow geode hbase beam
do
    python -m study.collect_jira_issues $PROJECT
    python -m study.collect_vcs_history https://github.com/apache/$PROJECT.git
    python -m study.compute_stats $PROJECT
done

montage -density 300 -tile 3x0 -geometry +5+50 10 data/output/*.png data/output/all_stats.png
