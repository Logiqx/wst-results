YEAR=$(date +%Y)

KNIGHTS=events/$YEAR/sailwave/knights.csv

echo "Helm,Name,Sail No,Fleet" >$KNIGHTS

grep "Mr.*,Windsurf,Adult" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Men/' >>$KNIGHTS
grep "Ms.*,Windsurf," events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Women/' >>$KNIGHTS
grep "Windsurf,Youth" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Youth/' >>$KNIGHTS
grep "Windsurf,Master" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Master/' >>$KNIGHTS
grep ",Windfoil," events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/Windfoil/Windfoil Open/' >>$KNIGHTS

sed -i 's/,/ /' $KNIGHTS

iconv -f utf-8 -t iso-8859-1 $KNIGHTS >$KNIGHTS.tmp
mv $KNIGHTS.tmp $KNIGHTS
