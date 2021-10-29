# Functionality
- Track disk usage over time on Mac.

# How it works
1. `disk-usage-depth-05.sh` uses `du` command to get the disk usage statistics, and then write these statistics to a file with a name like "2017-02-21-disk-usage.tsv".
2. Then `compare-changes.py` takes the two most recent `.tsv` files and compares which direcories have changed their sizes over time.

# Run
1. Open your **Terminal**.
2. Run `chmod u+x disk-usage-depth-05.sh`
3. Run `sudo ./disk-usage-depth-05.sh`
4. Run `python compare-changes.py`.

# Testing
- Only tested on **OS X Yosemite 10.10.5** and **Python 2.7.13**.

# Copyright
- Please feel free to copy and modify the code.
