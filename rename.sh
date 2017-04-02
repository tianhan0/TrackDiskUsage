
for f in `find *.txt`
do
	filename=$(basename "$f")
	base=${filename%.*}
	extension=${filename##*.}
	mv $filename $base.tsv
done
