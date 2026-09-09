EVENT=202609

ENTRIES=events/$EVENT/config/entries.tsv
ENTRANTS=events/$EVENT/config/entrants.csv

# Entrants is relatively straightforward, just add 100 to the foil IDs
echo "ID,Title,First Name,Family Name,Country,Sail No,Craft Type,Age" >$ENTRANTS

# Windsurf
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$2,$3,$4,$5,$6,$7,$12}' | grep -v -P ",-," >>$ENTRANTS

# Windfoil
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$8,$12}' | grep -v -P ",-," >>$ENTRANTS

# Wingfoil
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$9,$12}' | grep -v -P ",-," >>$ENTRANTS

# Kite
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1,$2,$3,$4,$5,$6,$10,$12}' | grep -v -P ",-," >>$ENTRANTS

# Kitefoil
tail +2 $ENTRIES | awk -F '\t' 'BEGIN {OFS=","} {print $1+100,$2,$3,$4,$5,$6,$11,$12}' | grep -v -P ",-," >>$ENTRANTS

# Quick review

echo $ENTRANTS:
head -4 $ENTRANTS
echo ...
tail -3 $ENTRANTS
