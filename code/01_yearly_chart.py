"""Chart reported Sundarbans abductions by year.

Reads data/clean/incidents.csv and writes figures/incidents_by_year.png.
Run from the repository root: python code/01_yearly_chart.py
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

SURFACE, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e6e5e1"
BAR, BAR_PARTIAL = "#2a78d6", "#86b6ef"
PARTIAL_YEAR, PARTIAL_LABEL = 2026, "2026 (to 27 October)"

d = pd.read_csv("data/clean/incidents.csv", dtype=str)
d["year"] = d["event_date"].str[:4].astype(int)
d["n_abducted"] = pd.to_numeric(d["n_abducted"], errors="coerce")
years = range(2015, PARTIAL_YEAR + 1)
g = d.groupby("year").agg(incidents=("incident_id", "count"), people=("n_abducted", "sum"))
g = g.reindex(years, fill_value=0)

fig, axes = plt.subplots(2, 1, figsize=(9, 6.6), sharex=True, facecolor=SURFACE)
panels = [("incidents", "Reported incidents"), ("people", "People taken (where the report gives a number)")]
for ax, (col, title) in zip(axes, panels):
    ax.set_facecolor(SURFACE)
    colors = [BAR_PARTIAL if y == PARTIAL_YEAR else BAR for y in years]
    bars = ax.bar(list(years), g[col], width=0.72, color=colors, edgecolor=SURFACE, linewidth=2, zorder=3)
    for b, v in zip(bars, g[col]):
        ax.text(b.get_x() + b.get_width() / 2, v + max(g[col]) * 0.02, f"{int(v)}",
                ha="center", va="bottom", fontsize=9, color=INK2)
    ax.set_title(title, loc="left", fontsize=11, color=INK, pad=6)
    ax.set_ylim(0, max(g[col]) * 1.18)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.tick_params(colors=INK2, labelsize=9, length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.axvspan(2015.5, 2018.5, color="#f0efec", zorder=1)

top = axes[0]
ymax = top.get_ylim()[1]
top.text(2017.2, ymax * 0.93, "Surrender of armed groups\n2016 – Nov 2018", ha="center", va="top", fontsize=8.5, color=INK2)
top.text(2025.55, ymax * 0.86, "New surrenders\nof armed groups,\nJul–Sep 2026", ha="right", va="top", fontsize=8.5, color=INK2)
top.annotate("Change of government,\nAug 2024", xy=(2024, g.loc[2024, "incidents"] + ymax * 0.09),
             xytext=(2022.3, ymax * 0.62), ha="center", va="center", fontsize=8.5, color=INK2,
             arrowprops=dict(arrowstyle="-", color=INK2, linewidth=0.8))
axes[1].set_xticks(list(years))
axes[1].set_xticklabels([str(y) for y in years])
axes[1].legend(handles=[Patch(color=BAR, label="Full year"), Patch(color=BAR_PARTIAL, label=PARTIAL_LABEL)],
               loc="upper center", bbox_to_anchor=(0.6, 0.98), frameon=False, fontsize=8.5, labelcolor=INK2)

fig.suptitle("Kidnapping for ransom in the Bangladesh Sundarbans, as reported in the press",
             x=0.01, ha="left", fontsize=12.5, color=INK, fontweight="bold")
fig.text(0.01, 0.012, "Counts are reported incidents, not all incidents; a rise can reflect more reporting.\n"
         "Sources: Prothom Alo, Kaler Kantho, Samakal, The Daily Star, bdnews24. Data: github.com/Affnann/sundarbans-ransom-tracker",
         fontsize=7.5, color=INK2, ha="left", linespacing=1.5)
fig.tight_layout(rect=(0, 0.055, 1, 0.965))
fig.savefig("figures/incidents_by_year.png", dpi=200, facecolor=SURFACE)
print(g.to_string())
