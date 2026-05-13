grep Windfoil events/2026/config/entrants.csv | cut -d, -f3,4,6 | sed 's/,/ /;s/$/,Windfoil Open/' >events/2026/sailwave/windfoil.csv
grep Windsurf.*Youth events/2026/config/entrants.csv | cut -d, -f3,4,6 | sed 's/,/ /;s/$/,Windfoil Youths/' >events/2026/sailwave/youths.csv
