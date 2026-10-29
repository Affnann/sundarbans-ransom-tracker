# Sundarbans Ransom Tracker

A hand-coded record of kidnapping-for-ransom incidents in the Bangladesh Sundarbans, built from published news reports, 2015 to the present.

Fishers, crab collectors, honey gatherers and woodcutters who work in the Sundarbans forest have long been abducted by armed groups and held until their families pay. No official dataset of these incidents exists. This project builds one from news coverage, mostly in Bangla, so that the size, prices and timing of the ransom trade can be measured, including before and after the 2016–2018 surrender campaign.

**Status:** 63 incidents (February 2015 to 27 October 2026) from Prothom Alo, Kaler Kantho, Samakal, The Daily Star and bdnews24, plus 9 records of protection payments.

![Reported incidents and people taken, by year](figures/incidents_by_year.png)

The chart counts **reported** incidents. Reporting changed over time: from 2025 many reports come from Coast Guard press releases about its operations, so part of the recent rise may be more reporting, not only more abductions. A new wave of surrenders by armed groups began in July 2026, but abductions were still being reported in September and October.

![Where reported abductions took place](figures/location_map.png)

Most reports name only a forest range, river or canal, not an upazila. Of the incidents that name a range, most are in the **Satkhira range** in the west.

## What each row records
- Date of the incident and date of the report
- Location (forest range, river or canal, and upazila where the article names it)
- Number of people abducted and their occupation
- Ransom demanded and ransom paid, if reported, with a flag for which one
- How many outlets reported it, and links to the reports

## What this dataset does not contain
- No names of victims, families or accused individuals
- No group names that identify a person
- No article text. Only links and our own coded fields are published.

## Limits
- It counts **reported** incidents. Many abductions are never reported, so totals are a lower bound.
- Ransom amounts come from press reports, often from relatives, and are not verified.
- Coverage depends on which outlets were searched and how their archives are indexed.
- The Coast Guard said it had rescued 41 hostages between 12 February and 8 July 2026; this dataset has press reports for about 32 of them, so some rescues never reached the press.
- Only one incident was found for 2019 to 2023. That fits the 2016–2018 surrender of armed groups, but quieter reporting could also explain part of it.

## Protection payments
Besides ransom, armed groups charge forest workers to enter: a fee per boat or per person, paid before a trip. `data/clean/protection_payments.csv` records each reported amount, who paid it and what it was for.

## Repository layout
```
data/raw/     source lists and download records (no article text)
data/clean/   the coded dataset
code/         numbered scripts, run in order from the repository root
              01_yearly_chart.py    -> figures/incidents_by_year.png
              02_location_map.py    -> figures/location_map.png
figures/      charts and the map
```

## License
Code: MIT (see `LICENSE`). Dataset built here: CC BY 4.0. Boundaries: Bangladesh Bureau of Statistics via HDX, CC BY-IGO (see `data/README.md`).
