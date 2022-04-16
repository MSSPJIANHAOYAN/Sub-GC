echo "Copy data to somewhere"

find test/ -name "*.jpg" | xargs -i cp {} train