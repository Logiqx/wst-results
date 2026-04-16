EVENT=2026

ENTRIES=events/$EVENT/config/entries.tsv
ENTRANTS=events/$EVENT/config/entrants.csv
MOTIONS=events/$EVENT/config/motions.csv

# Entrants is relatively straightforward, just add 100 to the foil IDs

echo "ID,Title,First Name,Family Name,Country,Sail No,Craft Type,Age" >$ENTRANTS

tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$2,$3,$4,$5,$6,$7,$10}' | grep -v -P ",-," >>$ENTRANTS
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$8,$10}' | grep -v -P ",-," >>$ENTRANTS
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$9,$10}' | grep -v -P ",-," >>$ENTRANTS

# Motions are similar to entrants, but multiply foil IDs by 10

echo "Entrant ID,Motion ID,Start Date,End Date,File ID,First Name,Family Name,Craft Type" >$MOTIONS

tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$11,"2026-04-27","2026-05-06",$12,$3,$4,$7}' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11*10,"2026-04-27","2026-05-06",$12,$3,$4,$8}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11*10,"2026-04-27","2026-05-06",$12,$3,$4,$9}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS

# Quick review

more $ENTRANTS $MOTIONS
