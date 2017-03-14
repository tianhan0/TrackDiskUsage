#!/bin/sh

path=$(pwd)

#now="$(date +'%d/%m/%Y')"
#now="$(date +'%Y-%m-%d_%H-%M')"
now="$(date +'%Y-%m-%d')"
#printf "Current date in dd/mm/yyyy format %s\n" "$now"

cd /
du -h -d 1 > "$path/$now-disk-usage.tsv"
