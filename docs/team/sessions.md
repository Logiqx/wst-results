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



#### Identifying Data Issues

- Wrote script to identify logs where the data is potentially suspect 
    - Look for points on the course, where SOG \>= 30 knots and sAcc >= 1.5 knots
        - 24 Apr
          - BOR810CHR - FIXED - Confirmed as poor quality data, so used backup device
          - KOL827LUI - Crash @ 13:12:30, not iffy data during a run
          - MOR854PIE - FIXED - Confirmed as poor quality data, so used backup device
          - PRU801AIV - Crash @ 12:54:02, not iffy data during a run
        - 23 Apr
          - TOR835MEL - Potentially affected one run @ 12:45:01
    - Add another criteria where sats < 15
        - 24 Apr
          - BOR810CHR_810_20240424 - FIXED - Confirmed as poor quality data, so used backup device
          - FAB625ROB_625_20240424 - Appears to be pretty normal
          - GAR845NIC_845_20240424 - Possibly not the best, but seems ok
          - KOL827LUI_827_20240424 - Crash @ 13:12:30, not iffy data during a run
          - MOR854PIE_854_20240424 - FIXED - Confirmed as poor quality data, so used backup device
          - PRU801AIV_801_20240424 - Crash @ 12:54:02, not iffy data during a run
        - 23 Apr
          - BOR810CHR_810_20240423 - Another track of Christian's
          - OTT869TIM_869_20240423 - FIXED - Confirmed as poor quality data, so used backup device
          - TOR836MEL_836_20240423 - Potentially affected one run @ 12:45:01
    - Add another criteria where hAcc >= 2.5 meters, instead of sats < 15
        - 24 Apr
          - BOR810CHR_810_20240424 - FIXED - Confirmed as poor quality data, so used backup device
          - GAR845NIC_845_20240424 - Possibly not the best, but seems ok
          - KOL827LUI_827_20240424 - Crash @ 13:12:30, not iffy data during a run
          - MOR854PIE_854_20240424 - FIXED - Confirmed as poor quality data, so used backup device
          - OTT869TIM_869_20240424 - SKIPPED - Does not affect the results / rankings
          - PRU801AIV_801_20240424 - Crash @ 12:54:02, not iffy data during a run
        - 23 Apr
          - GAR845NIC_845_20240423 - Seems ok since sAcc around 0.6 knots when hAcc is elevated
          - KUP823KLA_823_20240423 - Possibly not the best, but seems ok
          - MOR854PIE_854_20240423 - Potentially affected one run where sAcc > 2 knots @ 14:45:47
          - OTT869TIM_869_20240423 - FIXED - Confirmed as poor quality data, so used backup device
          - TOR836MEL_836_20240423 - Potentially affected one run @ 12:45:01



#### Finalising Results

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



