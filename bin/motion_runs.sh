YEAR=$(date +%Y)

for motion in $(grep Wind events/$YEAR/config/motions.csv | cut -d , -f5)
do
  echo $motion: $(cat events/$YEAR/gpsdata/*/* | grep -c $motion)
done
