# Functionality
- Track disk usage over time.

# How it works
- **disk-usage-depth-04.sh** uses `du` command to get the disk usage statistics, and then write these statistics to a file with a name like "2017-02-21-disk-usage.tsv".
- Then **compare-changes.py** takes the latest two ".tsv" files and compares which direcories changed their size over time.

# Run
- Open your **Terminal**.
- Run `chmod u+x disk-usage-depth-04.sh`
- Run `sudo ./disk-usage-depth-04.sh`
- Run `python compare-changes.py`.

# Testing
- Only tested on **OS X Yosemite 10.10.5** and **Python 2.7.13**.

# Copyright
- Please feel free to copy and mofidy this code.