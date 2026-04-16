EVENT=2026

ENTRIES=events/$EVENT/config/entries.tsv
ENTRANTS=events/$EVENT/config/entrants.csv

echo "ID,Title,First Name,Family Name,Country,Sail No,Craft Type,Age" >$ENTRANTS

tail +2 $ENTRIES | cut -f1,2,3,4,5,6,7,10 | sed 's/\t/,/g' | grep -v -P ",-," >>$ENTRANTS
tail +2 $ENTRIES | cut -f1,2,3,4,5,6,8,10 | sed 's/\t/,/g' | grep -v -P ",-," | sed 's/1/2/' >>$ENTRANTS
tail +2 $ENTRIES | cut -f1,2,3,4,5,6,9,10 | sed 's/\t/,/g' | grep -v -P ",-," | sed 's/1/2/' >>$ENTRANTS

cat $ENTRANTS
