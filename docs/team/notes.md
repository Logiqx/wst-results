## World Speed Tour

### Notes

#### Office

- Chargers set up in spare room and taped into position
- Router - set up but switched off for most of the day
- Dymo printers on shelf



#### Van

- Laptop bag
  - Glasses
  - Laptop + mouse
  - Notepad + pen
  - Sharpie
- Router which can potentially be plugged into van with generator



#### Motions

- New entrants can be assigned a motion at beach
  - Issue a "sail" device to make it clear that it is a primary device
  - Black out previous surname and forename with sharpie, leave number visible
  - Take a note of the rider name, nationality, sail number, adult / youth and motion ID
- Spares can be assigned with the previous name blacked out
  - Issue "wing" or "kite" device to make it clear that it is a backup device
  - Take a note of the rider name and the motion ID
  



#### Configuration

- Dummy records in motions.csv allow unallocated motions to have their data downloaded at the beach.
  - e.g. `99,724,2024-04-21,2024-04-30,ZZZ601ZZZ,TBC,TBC,TBC`

Notes:

- Dummy records have benefits but can also cause confusion
- New knights should be properly configured, prior to downloading all of the logs



#### Todo

- Documentation
  - Beach activities
    - Motions on the beach - switching on, laying out, collection, end of day, etc
    - New motions on the beach - "sail" (primary), "wing" / "kite" / "boat" (backup) 
    - Make a note of unclaimed motions - helps when doing DNS results
  - Daily processes
    - Assign motions to additional knights prior to download - makes life simpler and logs are clearer
    - Download from all motions, including unused ones to avoid confusion the next day
    - Copy OAO files to Windows for faster loading
    - How to use data from backup devices - e.g. Gibson, Ornvang, Mortefon, Bornemann
  - Event configuration
    - Setup of ISWC event - reports, session times, etc.
    - Use of course types for fin and foil - H1 (hydrofoil) or S1 / S2 (shore)
    - Heats throughout the week - configuration and reporting
    - Heat naming across days and multiple fleets all having heat 1 at different times - 1a, 1b, 1c, etc
  - Laptop
    - Useful aliases - server, results, series
    - Useful scripts - knights, motions, etc
  - GPSResults
    - Processing logs - use Windows folder to improve load times
    - Foil course - requires width of 500m
    - Setting time limits - consider daylight saving
    - Exporting results
  - Reporting
    - Mention DNC, DNS, DNF
  - Poor quality data - e.g. Mortefon, Bornemann
    - Identifying suspect Motion logs - SOG > 30 and sAcc > 1.5 in course area 
  - Fixes
    - Changing names, nationalities and sail numbers
    - Correcting results using logs from backup devices- forgotten device, device failure, or poor quality data
- Coding
  - Heats
    - Consider individual pages / reports for each heat - need to consider CSS implications
  - Series
    - Show individual heat results in different columns
    - Add support for DNC, DNS and DNF
    - Add support for knights that have no max speeds for the week - only DNS, DNF, etc
    - Make more robust, so that slight name / sail number mismatches are not problematic
    - Move Python script into sse-results project
    - Implement UKWA series within wsw-results
  - Entrants
    - Fix sorting of accented characters - e.g. Sébastien should come before Simon in entrant list
  - Adhoc
    - Improve Python code that creates adhoc charts - avoid memory bloat which causes issues on modest laptops
    - Package the Python script that looks for poor quality data in motion logs
      - Check historical WSW data for similar artefacts
  - Create new key for GitHub commits, rather than using the current key
- Administration
  - Nick to send bank details to Principe
  - Mike to introduce Bjorn Haacke to Julien, regarding devices for the German Championship