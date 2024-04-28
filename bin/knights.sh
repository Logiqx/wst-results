YEAR=$(date +%Y)

KNIGHTS=events/$YEAR/sailwave/knights.csv

>$KNIGHTS

grep "Mr.*,Windsurf,Adult" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Men/' >>$KNIGHTS
grep "Ms.*,Windsurf," events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Women/' >>$KNIGHTS
grep "Mr.*,Windsurf,Youth" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/Windsurf/Youth Men/' >>$KNIGHTS
grep "Ms.*,Windsurf,Youth" events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/Windsurf/Youth Women/' >>$KNIGHTS
grep ",Windfoil," events/$YEAR/config/entrants.csv | cut -d, -f3-4,7,6 | sed 's/$/ Open/' >>$KNIGHTS

iconv -f utf-8 -t iso-8859-1 $KNIGHTS >$KNIGHTS.tmp
mv $KNIGHTS.tmp $KNIGHTS
