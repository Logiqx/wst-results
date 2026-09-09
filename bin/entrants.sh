for i in events/*/config/entrants.csv
do
	csvcut -c Title,"First Name","Family Name",Country,"Sail No","Craft Type",Age $i | tail +2
done | sort -u -t, -k2
