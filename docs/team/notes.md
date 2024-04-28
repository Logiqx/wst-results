## World Speed Tour

### Notes

#### Office

- Chargers set up in spare room and taped into position
- Router - set up but switched off
- Dymo printers



#### Van

- Laptop bag
  - Glasses
  - Laptop + mouse
  - Notepad + pen
  - Sharpie
- Router to be plugged into van with generator
  - The ideal is to collect data at the beach, but process it at the camp site



#### Motions

- New entrants can be assigned a motion at beach, previous name blacked out with sharpie
  - Take a note of the rider name and the motion ID
- Spares can be assigned with the previous name blacked out, ideally labelled "wing" or "kite"
  - Take a note of the rider name and the motion ID



#### Configuration

- Dummy records in motions.csv so that unallocated motions will have their data downloaded at the beach.
  - e.g. `99,724,2024-04-21,2024-04-30,ZZZ601ZZZ,TBC,TBC,TBC`

Note: Dummy records should be deemed a last resort. New knights should be configured prior to downloading logs.



#### Todo

- Documentation
  - Beach activities
    - Motions on the beach - switching on, laying out, collection, etc
    - New motions on the beach - sail / yellow label (primary), wing / kite / boat (backup) 
  - Command aliases - server, results, series
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
  - GPSResults
    - Foil course - 500m width
    - Loading logs (use Windows folder) + gates
    - Setting time limits - daylight saving
    - Exporting results
  - Reporting
    - Mention DNC, DNS, DNF
  - Poor quality data - e.g. Mortefon, Bornemann
    - Identifying suspect Motion logs - SOG > 30 and sAcc > 1.5 in course area 
  - Fixes
    - Changing names, nationalities and sail numbers
    - Correcting results using logs from backup devices when device fails or produces poor quality data
- Coding
  - Entrants
    - Fix sorting of accented characters - e.g. Sébastien should come before Simon in entrant list
  - Series
    - Add support for knights in Sailwave file that have no max speeds for the week
    - Add support for DNC, DNS and DNF
    - Make more robust, so that slight name / sail number mismatches are not problematic
    - Show individual heat results in different columns
    - Move Python script into sse-results project
    - Implement UKWA series within wsw-results
  - Adhoc
    - Improve Python code that creates adhoc charts - avoid memory bloat which causes issues on modest laptops
    - Package the Python script that looks for poor quality data in motion logs
  - Create new key for GitHub commits, rather than using the current key
- Administration
  - Nick to send bank details to Principe
  - Mike to contact Bjorn Haacke (German Speed) about Motion Minis, and to introduce Julien