EVENT=202609

ENTRIES=events/$EVENT/config/entries.tsv
MOTIONS=events/$EVENT/config/motions.csv
MOTIONS_EXTRA=events/$EVENT/config/motions-extra.csv

# Motions are similar to entrants, but multiply foil IDs by 10
echo "Entrant ID,Motion ID,Start Date,End Date,File ID,First Name,Family Name,Craft Type" >$MOTIONS

# Windsurf
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$13,"2026-04-27","2026-05-06",$14,$3,$4,$7}' | grep -v -P ",-$" >>$MOTIONS

# Windfoil
tail +2 $ENTRIES | grep -v Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$13,"2026-04-27","2026-05-06",$14,$3,$4,$8}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | grep Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$13*10,"2026-04-27","2026-05-06",$14,$3,$4,$8}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS

# Wingfoil
tail +2 $ENTRIES | grep -v Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+200,$13,"2026-04-27","2026-05-06",$14,$3,$4,$9}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | grep Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+200,$13*10,"2026-04-27","2026-05-06",$14,$3,$4,$9}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS

# Buoys
tail +2 $MOTIONS_EXTRA >>$MOTIONS

# Quick review

echo $MOTIONS:
head -4 $MOTIONS
echo ...
tail -3 $MOTIONS
