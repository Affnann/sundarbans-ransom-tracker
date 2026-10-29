"""Map where reported Sundarbans abductions happened, as far as the reports say.

Left: upazilas of Satkhira, Khulna and Bagerhat, shaded by the number of
incidents whose article names the upazila of the abduction or holding site.
Right: incidents by forest range, as named in the article.

Reads data/clean/incidents.csv and data/raw/hdx_upazilas_satkhira_khulna_bagerhat.geojson.
Writes figures/location_map.png.
Run from the repository root: python code/02_location_map.py
"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

SURFACE, INK, INK2, EDGE, EMPTY = "#fcfcfb", "#0b0b0b", "#52514e", "#c3c2b7", "#f0efec"
STEPS = {1: "#9ec5f4", 2: "#5598e7", 3: "#256abf", 4: "#104281"}  # one hue, light to dark
BAR = "#2a78d6"

d = pd.read_csv("data/clean/incidents.csv", dtype=str).fillna("")
g = gpd.read_file("data/raw/hdx_upazilas_satkhira_khulna_bagerhat.geojson")

site = d[d["site_upazila"] != ""]["site_upazila"].value_counts()
g["n"] = g["adm3_name"].map(site).fillna(0).astype(int)
missing = set(site.index) - set(g["adm3_name"])
assert not missing, f"upazila names not found in boundaries: {missing}"

range_label = {
    "Satkhira": "Satkhira range",
    "Khulna": "Khulna range",
    "Chandpai": "Chandpai range",
    "Sharankhola": "Sharankhola range",
    "Sharankhola/Chandpai": "Sharankhola or Chandpai",
    "East Sundarbans": "East Sundarbans, range not named",
    "": "No range named",
}
unlabelled = set(d["forest_range"]) - set(range_label)
assert not unlabelled, f"forest ranges without a label: {unlabelled}"
r = d["forest_range"].map(range_label).value_counts()
order = [v for v in range_label.values() if v in r.index]
r = r.reindex(order)
assert r.sum() == len(d), "range chart does not cover every incident"

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 6.4), facecolor=SURFACE,
                             gridspec_kw={"width_ratios": [1.15, 1]})
ax.set_facecolor(SURFACE)
g.plot(ax=ax, color=[STEPS.get(min(n, 4), EMPTY) for n in g["n"]], edgecolor=EDGE, linewidth=0.6)
from shapely.geometry import box
LABEL_BAND = {"Dacope": (21.85, 22.15), "Mongla": (22.30, 22.50)}  # keep these two narrow labels apart
for _, row in g[g["n"] > 0].iterrows():
    geom = row.geometry
    if row["adm3_name"] in LABEL_BAND:
        lo, hi = LABEL_BAND[row["adm3_name"]]
        geom = geom.intersection(box(88.0, lo, 91.0, hi))
    p = geom.representative_point()
    ax.annotate(f"{row['adm3_name']}\n{row['n']}", (p.x, p.y), ha="center", va="center", fontsize=8.5,
                color="#ffffff" if row["n"] >= 2 else INK)
for _, row in g[(g["n"] == 0) & g["adm3_name"].isin(["Paikgachha", "Sharankhola", "Assasuni"])].iterrows():
    p = row.geometry.representative_point()
    ax.annotate(row["adm3_name"], (p.x, p.y), ha="center", va="center", fontsize=7.5, color=INK2)
ax.set_axis_off()
ax.set_title(f"Where the article names the upazila ({int(site.sum())} of {len(d)} incidents)",
             loc="left", fontsize=10.5, color=INK)
for lab, x in [("Satkhira", 89.05), ("Khulna", 89.45), ("Bagerhat", 89.82)]:
    ax.text(x, 22.93, lab, ha="center", fontsize=8, color=INK2, style="italic")

bx.set_facecolor(SURFACE)
y = range(len(r))[::-1]
bx.barh(list(y), r.values, color=BAR, height=0.62, edgecolor=SURFACE, linewidth=2)
bx.set_yticks(list(y))
bx.set_yticklabels(r.index, fontsize=9, color=INK)
for yi, v in zip(y, r.values):
    bx.text(v + 0.4, yi, str(v), va="center", fontsize=9, color=INK2)
bx.set_xlim(0, r.max() * 1.15)
bx.set_xticks([])
for s in bx.spines.values():
    s.set_visible(False)
bx.tick_params(length=0)
bx.set_title(f"Incidents by forest range, as named in the article (all {len(d)})", loc="left", fontsize=10.5, color=INK)

fig.suptitle("Where reported Sundarbans abductions took place, 2015–2026", x=0.01, ha="left",
             fontsize=12.5, fontweight="bold", color=INK)
fig.text(0.01, 0.012,
         "Most reports name only a river, canal or forest range, so most incidents cannot be placed on an upazila map. "
         "Victims' home villages are not used.\n"
         "Boundaries: Bangladesh Bureau of Statistics via HDX (CC BY-IGO). "
         "Data: github.com/Affnann/sundarbans-ransom-tracker",
         fontsize=7.5, color=INK2, ha="left", linespacing=1.5)
fig.tight_layout(rect=(0, 0.06, 1, 0.95))
fig.savefig("figures/location_map.png", dpi=200, facecolor=SURFACE)
print(site.to_string()); print(r.to_string())
