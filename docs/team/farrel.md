## World Speed Tour - Farrel Cup

### Entrants

Google Forms allows entrants to submit their details - [link](https://docs.google.com/forms/d/1Vdut9kwZPH6Ctbg0ytHjSOfjKUviU9akdY0Fa7DA-yg/edit)

Reponses in Google Sheets - [link](https://docs.google.com/spreadsheets/d/1XefPSNJidULl90ibbagc3-47lHHJH0lgfI2XPRSxItA/edit?gid=1881123381#gid=1881123381)



### Downloading Session Data

- Prefix all file names with the sail number, exactly matching the registration (e.g. FRA-192)
- Record which riders have provided data for each session in Google Sheets
- Copy the files into a Windows folder, ensuring problematic formats (e.g. UBX, FIT) are in a sub-folder
- Batch convert all problematic formats (e.g. UBX, FIT) to GPX using GPS Wizard script
- Check the counts in Google Sheets vs files in Windows folder
- Check for GPX files without COG - see example below

How to check for lack of COG in GPX files, which mandates non-Doppler results.

```sh
cd /mnt/c/Users/mwgeo/Downloads/pos
find . -name *gpx -exec grep -Hc course {} \; | grep :0
```



### GPSResults

Load files into GPSResults, apply gates and time limits  (remember to use UTC) and then export the CSV containing all runs.
- Fin heat
  - Files without COG need to be processed separately (non-Doppler) - e.g. GPX files from Apple
- Wing / windfoil heat

Save the CSV results in Linux environment:

```sh
mkdir events/202509/gpsdata/20250923
vi events/202509/gpsdata/20250923/GPSDATA_20250924_S1.csv events/202509/gpsdata/20250923/GPSDATA_20250924_S2.csv
```

Standardise the filenames in the CSV:
```sh
sed -i -r "s/_.*\.([a-zA-Z][a-zA-Z][a-zA-Z]),/_0_20250923_000000.\1,/" events/202509/gpsdata/20250923/*
sed -i -r "s/_.*\.([a-zA-Z][a-zA-Z][a-zA-Z]),/_0_20250924_000000.\1,/" events/202509/gpsdata/20250924/*
```



### Heat Reports

Declare the ISWC heats:

```sh
mkdir events/202509/config/sessions/20250923
cp events/202409/config/sessions/20240911/* events/202509/config/sessions/20250923
vi events/202509/config/sessions/20250923/*   (remember to use local time)
bin/reports.sh
```

After running reports:
- Check count of people in fastest of the day



### ISWC Rankings

- Import heat rankings into Sailwave
- Run the script to merge in the ISWC rankings

```sh
bin/rankings.sh
```

