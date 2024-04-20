# Explanation at https://www.peterbe.com/plog/set-ex
set -ex

# Change dd/yy/yyyy to yyyy-mm-dd
sed -i -r "s/([0-9][0-9])\/([0-9][0-9])\/([0-9][0-9][0-9][0-9])/\3-\2-\1/g" events/*/config/motions*.csv
