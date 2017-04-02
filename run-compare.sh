now="$(date +'%Y-%m-%d')"

python compare-changes.py
python compare-changes.py > "$now-changes.txt"
