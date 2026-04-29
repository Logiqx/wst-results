EVENT=2026

ENTRIES=events/$EVENT/config/entries.tsv
ENTRANTS=events/$EVENT/config/entrants.csv
MOTIONS=events/$EVENT/config/motions.csv
MOTIONS_EXTRA=events/$EVENT/config/motions-extra.csv

# Entrants is relatively straightforward, just add 100 to the foil IDs
echo "ID,Title,First Name,Family Name,Country,Sail No,Craft Type,Age" >$ENTRANTS

# Windsurf
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$2,$3,$4,$5,$6,$7,$10}' | grep -v -P ",-," >>$ENTRANTS

# Windfoil
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$8,$10}' | grep -v -P ",-," >>$ENTRANTS

# Wingfoil
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$9,$10}' | grep -v -P ",-," >>$ENTRANTS

# Motions are similar to entrants, but multiply foil IDs by 10
echo "Entrant ID,Motion ID,Start Date,End Date,File ID,First Name,Family Name,Craft Type" >$MOTIONS

# Windsurf
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$11,"2026-04-27","2026-05-06",$12,$3,$4,$7}' | grep -v -P ",-$" >>$MOTIONS

# Windfoil
tail +2 $ENTRIES | grep -v Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11,"2026-04-27","2026-05-06",$12,$3,$4,$8}' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | grep Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11*10,"2026-04-27","2026-05-06",$12,$3,$4,$8}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS

# Wingfoil
tail +2 $ENTRIES | grep -v Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11,"2026-04-27","2026-05-06",$12,$3,$4,$9}' | grep -v -P ",-$" >>$MOTIONS
tail +2 $ENTRIES | grep Windsurf | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$11*10,"2026-04-27","2026-05-06",$12,$3,$4,$9}' | sed -r 's/([A-Z]+)([0-9]+)([A-Z]+)/\1\20\3/' | grep -v -P ",-$" >>$MOTIONS

# Buoys
tail +2 $MOTIONS_EXTRA >>$MOTIONS

# Quick review

echo $ENTRANTS:
head -4 $ENTRANTS
echo ...
tail -3 $ENTRANTS

echo

echo $MOTIONS:
head -4 $MOTIONS
echo ...
tail -3 $MOTIONS
