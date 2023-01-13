#!/bin/sh

path=$(pwd)

now="$(date +'%Y-%m-%d-%H-%M-%S')"

cd /
du -m -d 7 -x | sort -b -n -r > "$path/$now-disk-usage.tsv"
