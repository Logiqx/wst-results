# Explanation at https://www.peterbe.com/plog/set-ex
set -ex

EVENT=2026

# Multiply motion IDs by 10 for hydrofoil courses
sed -i -r 's/([A-Z]+)([0-9][0-9][0-9])([A-Z]+)/\1\20\3/' events/2026/gpsdata/*/*H[1-9].csv
sed -i -r 's/_([0-9][0-9][0-9])_/_\10_/' events/2026/gpsdata/*/*H[1-9].csv
