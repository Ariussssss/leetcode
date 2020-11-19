basedir=$(dirname "$0")
cd "$basedir/leco-source"
for f in *.py; do python "$f"; done
cd -
