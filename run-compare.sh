now="$(date +'%Y-%m-%d')"

python3 compare-changes.py
python3 compare-changes.py > "$now-changes.txt"
