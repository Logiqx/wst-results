YEAR=$(date +%Y)

grep WARN events/$YEAR/logs/server.log  | egrep -v 'battery|interval'
