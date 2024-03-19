YEAR=$(date +%Y)

grep motion- events/$YEAR/logs/server.log | egrep -v 'conn|battery|detected|storage|firmware|downloaded' | sed 's/ [A-Z].*//;s/ .*,/,/' | sort >log_check.0
sort -u log_check.0 >log_check.1
diff log_check.1 log_check.0
rm log_check.0 log_check.1
