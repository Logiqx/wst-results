# Explanation at https://www.peterbe.com/plog/set-ex
set -ex

# Change serial numbers to match device IDs in gpsdata
sed -i -r 's/([A-Z]+)([0-9]+)([A-Z]+)_([0-9]+)/\1\2\3_\2/' events/*/gpsdata/*/*.csv
