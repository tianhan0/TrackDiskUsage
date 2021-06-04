#!/bin/sh

path=$(pwd)

now="$(date +'%Y-%m-%d')"

cd /
du -m -d 5 | sort -b -n -r > "$path/$now-disk-usage.tsv"
