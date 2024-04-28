## World Speed Tour

### Sessions

#### Mon 22

- Additional Knights
  - Arnold,Schreurs,Netherlands,NED-369,Windsurf,Adult
  - Fabien,Mayou,France,FRA-535,Windsurf,Adult
  - Fabien,Mayou,France,FRA-535,Windfoil,Adult
  - Martim,Monteiro,Portugal,POR-13,Windsurf,Adult
  - Ben,Van Der Steen,Netherlands,NED-57,Windsurf,Adult
  - Robert,Fabrice,France,FRA-816,Windsurf,Adult
- Heats
  - 1115 - 1200 = Windfoil Open
  - 1230 - 1316 = Windsurf Women and Youths
  - 1435 - 1535 = Windsurf Men
- Issues
  - Jenna's motion did not have a flashing light at the end of the day
    - Reverted to backup device - personal motion mini
  - Foil course in GPSResults was not wide enough at 250m
    - Needed to widen course to 500m
- Evening tasks
  - Labelling motions for additional knights
  - Assigned new GPS to Jenna
    - TODO - document how existing data was changed with "sed"



#### Tue 23

- Additional Knights
  - Marius,Loglisci,France,FRA-735,Windsurf,Youth
- Heats
  - 1101- 1228 = Windsurf
  - 1427 - 1530 = Windsurf
- Issues
  - Melek's motion could not be found (TOR836MEL)
    - It had accidentally been given to Torsten Mallon
- Evening tasks
  - Tweaked series results to use hyphen as delimiter between heats
  - Came up with way to handle heat numbers during the week correctly
  - Notes a couple of tasks for later - rank when results are the same, and character encoding of sailwave exports




#### Wed 24

- Heats
  - 1120 - 1235 = Windsurf
  - 1445 - 1621 = Windsurf
- Issues
  - Roger Ornvang forgot to take the motion mini
    - Took results from his personal Motion
  - No runs for some people who did not sail
    - Hupert, Thau, Texeira - full day of data recorded (including drive back to campsite), they just did not sail
  - Motion handed in late (Schreurs), requiring results to be done twice
    - Rider decided to carry on sailing after the day had ended
  - Bad data from two motions - Mortefon and Bornemann
    - Used data from backup devices




#### Afterwards

- Wrote script to identify logs that are potentially suspect
    - MOR854PIE - 24 Apr - Poor quality data, so used backup device
    - BOR810CHR - 24 Apr - Poor quality data, so used backup device
    - TOR835MEL - 23 Apr - Only affected one run @ 12:45:01
    - KOL827LUI - 24 Apr - Crash at 13:12:30, not iffy data during a run
    - PRU801AIV - 24 Apr - Crash at 12:54:02, not iffy data during a run
- Entrants
  - Fixed sail numbers
      - Changed K33 and K88 to GBR-33 and GBR-888
      - Added missing sail numbers
  - Fixed names
      - Changed Gautier Bourgeois (FRA-6) to Sebastien Bourgeois (FRA-665)
      - Fixed various names, nationalities, sail numbers
  - Foiling knights
      - Added the foiling knights to entrants, since they did not obtain results
- Fixed "best runs" and "fastest runs" reports
  - Round to 2 decimal places before ranking - affects "fastest runs" ranks on Tue 23 for Laufer and Bordes
- Fixed character encoding for Sailwave
    - Sailwave files are now using latin-1 encoding
- Considered impact of adding youths to men's results
  - Including in heats 2 to 5 is unsupported by the existing software, so it was not done




#### Outstanding

- Add DNC, DNS, DNF results
