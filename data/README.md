# Data sources

Each source is listed with what it is used for, its terms, and the date it was accessed. Download dates are filled in as data is collected.

## Incident reports (news)
Used only to code incidents. Article text is not stored or published; each row links back to the original report.

| Source | Language | Used for | Accessed |
|---|---|---|---|
| Prothom Alo (prothomalo.com) | Bangla | main incident source | 2026-10-29 |
| Samakal (samakal.com) | Bangla | incident source | — |
| Kaler Kantho (kalerkantho.com) | Bangla | incident source | — |
| The Daily Star (thedailystar.net) | English | incident source | 2026-10-29 |
| Dhaka Tribune (dhakatribune.com) | English | incident source | — |
| bdnews24.com (English and Bangla editions) | English, Bangla | incident source | 2026-10-29 |

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
- `data/clean/protection_payments.csv`: reported fees charged to fishers, crab collectors, woodcutters and honey collectors for entry or protection.
- `data/raw/held_aside.csv`: reports that could not be dated, placed or checked well enough to include.

## How incidents were found
Web searches of each outlet, plus Prothom Alo's own site search run year by year from 2015 with several Bangla search terms, keeping headlines that mention the Sundarbans together with abduction, hostage or ransom. Each article was then read in full.

## Key columns
- `date_precision`: `exact`, `derived_from_weekday` (the article says e.g. 'last Friday'; the date is worked out from the publication date), `approximate`, `month`, `year_inferred`.
- `waters`: `forest` (rivers and canals inside the forest) or `coastal_sea` (the sea just off it).
- `confirmation`: `reported`, `unconfirmed` (a key fact is missing or the article contradicts itself) or `disputed` (an official source contests it).
- `site_upazila`: the upazila of the abduction or holding site, filled only when the article names it. Victims' home villages are not used.
- `forest_range`: the forest department range, as named in the article.
- `other_urls`: further reports of the same incident.

## Coverage
Incidents from 1 January 2015 to the present.

## Licenses
- The coded dataset in `data/clean/` is released under CC BY 4.0.
- News reports remain the property of their publishers and are not redistributed.
- Map data keeps its source's license.
