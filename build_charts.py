"""
Builds the two HDI charts (trend line and 2023 comparison bar) from
bangladesh_south_asia_hdi.csv.

Source of the underlying figures: UNDP Human Development Report Office,
"All composite indices and components time series (1990-2023)",
https://hdr.undp.org/data-center/documentation-and-downloads

Usage: python3 build_charts.py
"""
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA_FILE = "bangladesh_south_asia_hdi.csv"
YEARS = list(range(1990, 2024))

LABELS = {"BGD": "Bangladesh", "IND": "India", "PAK": "Pakistan",
          "NPL": "Nepal", "LKA": "Sri Lanka"}
COLORS = {"BGD": "#2E2E2E", "IND": "#6B8FB5", "PAK": "#C97B63",
          "NPL": "#8FA37E", "LKA": "#B79A56"}


def load_data():
    data = {}
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row["iso3"]
            data[code] = {y: float(row[str(y)]) for y in YEARS}
    return data


def plot_trend(data):
    fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
    for code in ["PAK", "NPL", "IND", "LKA", "BGD"]:
        ys = [data[code][y] for y in YEARS]
        ax.plot(YEARS, ys, label=LABELS[code], color=COLORS[code],
                 linewidth=2.8 if code == "BGD" else 1.6,
                 zorder=3 if code == "BGD" else 2)
    ax.set_ylabel("Human Development Index", fontsize=10)
    ax.set_title("HDI Trajectories, 1990–2023: Bangladesh and South Asian Neighbors",
                  fontsize=11, fontweight="bold")
    ax.set_xlim(1990, 2023)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.savefig("bd_hdi_trend_1990_2023.png", dpi=150)
    plt.close(fig)


def plot_2023_comparison(data):
    order = ["Pakistan", "Nepal", "India", "Bangladesh", "Sri Lanka"]
    code_by_name = {v: k for k, v in LABELS.items()}
    values = [data[code_by_name[name]][2023] for name in order]
    colors = ["#AFAFAF"] * 5
    colors[order.index("Bangladesh")] = "#2E2E2E"

    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=150)
    bars = ax.bar(order, values, color=colors, width=0.6)
    ax.set_ylabel("HDI (2023)", fontsize=10)
    ax.set_title("Bangladesh vs. South Asian Neighbors: Human Development Index, 2023",
                  fontsize=11, fontweight="bold")
    ax.set_ylim(0, 0.85)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.015,
                 f"{val:.3f}", ha="center", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.savefig("bd_hdi_comparison.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    data = load_data()
    plot_trend(data)
    plot_2023_comparison(data)
    print("Saved bd_hdi_trend_1990_2023.png and bd_hdi_comparison.png")
