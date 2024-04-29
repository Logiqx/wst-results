## World Speed Tour

### Sessions

#### Mon 22

- Heat times
  - 1115 - 1200 = Windfoil Open
  - 1230 - 1316 = Windsurf Women and Youths
  - 1435 - 1535 = Windsurf Men
- Additional knights
  - Arnold,Schreurs,Netherlands,NED-369,Windsurf,Adult
  - Fabien,Mayou,France,FRA-535,Windsurf,Adult
  - Fabien,Mayou,France,FRA-535,Windfoil,Adult
  - Martim,Monteiro,Portugal,POR-13,Windsurf,Adult
  - Ben,Van Der Steen,Netherlands,NED-57,Windsurf,Adult
  - Robert,Fabrice,France,FRA-816,Windsurf,Adult
- Beach issues
  - Jenna's motion did not have a flashing light at the end of the day - only one not flashing
    - Reverted to backup device - personal motion mini
- Office issues
  - Motions handed in late - Arnold Schreurs and Antoine Albeau
    - Need to check that all motions are accounted for at the end of the day
  - Gates in GPSResults were not wide enough for the foil course
    - The width of 250m did not include the start buoy so needed to widening to 500m
- Additional tasks
  - Assigned new GPS to Jenna
    - TODO - document how existing data was changed to match the new motion using "sed"
  - Labelled the motions for additional knights



#### Tue 23

- Heat times
  - 1101- 1228 = Windsurf
  - 1427 - 1530 = Windsurf
- Additional knights
  - Marius,Loglisci,France,FRA-735,Windsurf,Youth
- Beach issues
  - Melek's motion could not be found (TOR836MEL) after the briefing
    - It had accidentally been given to Torsten Mallon (MAL870TOR), but resolved before any sailing
- Office issues
  - Motions handed in late - Christophe Deus and Antoine Albeau 
    - Need to check that all motions are accounted for at the end of the day
- Result queries
  - Cédric Bordes asked for his result to be checked
    - It was the common scenario of the best 500 meters starting before the actual course
- Evening tasks
  - Came up with way to correctly report the heat numbers during the week
  - Tweaked series results to use hyphen as delimiter between heats
  - Labelled new motion for additional knight
  - Deferred tasks
    - Equal rank when results are the same (fastest runs, best runs, etc) - now resolved
    - Character encoding of CSV export for Sailwave - now resolved




#### Wed 24

- Heat times
  - 1120 - 1235 = Windsurf
  - 1445 - 1621 = Windsurf
- Beach issues
  - Roger Ornvang forgot to take the motion mini
    - Took results from his personal Motion
- Office issues
  - Motion handed in late by Arnold Schreurs, requiring results to be processed twice
    - Rider decided to carry on sailing after the day had ended
  - No runs for some people who did not sail - Hupert, Thau, Texeira
    - Causes a little bit of confusion when trying to download the data
    - There was a full day of data recorded (including drive back to campsite), they just did not sail
  - Bad data from two motions - Pierre Mortefon and Christian Bornemann
    - Used data from their own Motion LCDs - need to document this process
- Result queries
  - Pierre asked for his result to be checked
    - This turned out to be genuinely bad data
      - Position of motion confirmed as being under his arm, issue is clearly evident in sAcc data
  - Christian asked for his result to be checked
    - This issue was twofold
      - Position of motion (although disputed), somewhat evident in sAcc data
      - The common scenario of the best 500 meters starting before the actual course



#### Afterwards

- Wrote script to identify logs where the data is potentially suspect 
    - Points in the course area (geo-fencing) where SOG \>= 30 knots and sAcc >= 1.5 knots
        - MOR854PIE - 24 Apr - Confirmed as poor quality data, so used backup device
        - BOR810CHR - 24 Apr - Confirmed as poor quality data, so used backup device
        - TOR835MEL - 23 Apr - Potentially affected just one run @ 12:45:01
        - KOL827LUI - 24 Apr - Crash @ 13:12:30, not iffy data during a run
        - PRU801AIV - 24 Apr - Crash @ 12:54:02, not iffy data during a run
- Tweaks to entrants
  - Fixed sail numbers
      - Changed K33 and K88 to GBR-33 and GBR-888
      - Added missing sail numbers
  - Fixed names
      - Changed Gautier Bourgeois (FRA-6) to Sebastien Bourgeois (FRA-665)
      - Fixed various names (e.g. typos, surname + forename switched)
      - Fixed nationalities and sail numbers
  - Foiling knights
      - Added the foiling knights to the list of entrants, subsequently marked as DNS or DNF
- Coding
    - Fixed "best runs" and "fastest runs" reports
        - Round speeds to 2 decimal places before deciding on rankings
        - Fixes equal ranks of "fastest runs" ranks on Tue 23 for Laufer and Bordes
    - Fixed character encoding for Sailwave
        - Sailwave files are now using latin-1 encoding
    - Added support for DNC, DNS, DNF, etc
        - Coerced the software and Sailwave to include DNS and DNF results
        - Series results now show the actual codes, rather than the actual points
- Requests
  - Considered impact of adding youths to men's results
      - Including in heats 2 to 5 is unsupported by the existing software, so it was not done
  - Considered adding "masters" results
      - Can be done but requires some effort - new reports, new Sailwave series, etc



