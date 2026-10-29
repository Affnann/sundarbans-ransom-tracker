# Data sources

Each source is listed with what it is used for, its terms, and the date it was accessed. Download dates are filled in as data is collected.

## Incident reports (news)
Used only to code incidents. Article text is not stored or published; each row links back to the original report.

| Source | Language | Used for | Accessed |
|---|---|---|---|
| Prothom Alo (prothomalo.com) | Bangla | main incident source | 2026-10-29 |
| Samakal (samakal.com) | Bangla | incident source | — |
| Kaler Kantho (kalerkantho.com) | Bangla | incident source | — |
| The Daily Star (thedailystar.net) | English | incident source | — |
| Dhaka Tribune (dhakatribune.com) | English | incident source | — |
| bdnews24.com | English | incident source | — |

## Official context
| Source | Used for | Accessed |
|---|---|---|
| Rapid Action Battalion (rab.gov.bd) | surrender campaign dates and official announcements | — |

## Map
| Source | License | Accessed |
|---|---|---|
| OpenStreetMap via Geofabrik (download.geofabrik.de) | ODbL 1.0, © OpenStreetMap contributors | — |
| Bangladesh administrative boundaries via HDX (data.humdata.org) | to be checked on the dataset page | — |

## Files
- `data/clean/incidents.csv`: one row per incident. Every article was read twice; rows where the two readings disagree or a fact is missing are marked `unconfirmed` or `disputed`.
- `data/raw/held_aside.csv`: reports that could not be dated well enough to include.

## Coverage
Incidents from 1 January 2015 to the present.

## Licenses
- The coded dataset in `data/clean/` is released under CC BY 4.0.
- News reports remain the property of their publishers and are not redistributed.
- Map data keeps its source's license.
