# Bangladesh's Human Development Trajectory and the Digital Divide
### A short analytical note using UNDP's Human Development Index, 1990–2023

---

## Why this note

BD Digital Access, an earlier project of mine, used the World Bank's open data to map how unevenly internet access, mobile penetration, and literacy are distributed across Bangladesh. This note extends that question to UNDP's own flagship measure of development the Human Development Index (HDI), using UNDP's complete 1990–2023 composite indices time series, to ask a more specific version of the same thing, what does Bangladesh's long-run development trajectory actually look like, and where might digital access be one of the forces behind it?

## What the full trajectory shows

Bangladesh's HDI has risen from **0.397 in 1990 to 0.685 in 2023**- a sustained, nearly uninterrupted climb across 34 years, placing it in the **medium human development** category at rank **130**. The single most notable feature of that trajectory is not the endpoint but the shape of the climb relative to its neighbors.

In 1990, Bangladesh (0.397) started behind India (0.446), Nepal (0.404), and Sri Lanka (0.638), and only narrowly ahead of Pakistan (0.396). Over the following three decades, Bangladesh's curve rises more steeply than any of its neighbors except Sri Lanka, and by 2023 it has fully converged with India, both countries now stand at **exactly 0.685**. Bangladesh overtook Nepal by the early 1990s and has held a growing lead over Pakistan throughout. Only Sri Lanka (0.776) remains clearly ahead.

| Country | HDI (1990) | HDI (2023) | Category (2023) |
|---|---|---|---|
| Pakistan | 0.396 | 0.544 | Low |
| Nepal | 0.404 | 0.622 | Medium |
| **Bangladesh** | **0.397** | **0.685** | **Medium** |
| India | 0.446 | 0.685 | Medium |
| Sri Lanka | 0.638 | 0.776 | High |

*(Source: UNDP Human Development Report Office, "All composite indices and components time series (1990–2023)," 2025 data release.)*

This convergence with India is worth pausing on. A country that started noticeably behind another has, over 34 years, closed the entire gap — while a country that started far ahead of everyone (Pakistan) has instead fallen further behind the group. Growth rate alone does not explain outcomes; something about the composition of that growth does.

## Where the growth is coming from

HDI is built from three components: health (life expectancy at birth), education (expected and mean years of schooling), and standard of living (GNI per capita). Pulling apart Bangladesh's own numbers shows where the climb is concentrated: life expectancy rose from 55.8 years in 1990 to 74.7 in 2023, and GNI per capita nearly quintupled, from roughly $1,733 to $8,498 (2017 PPP\$). Health and income gains, in other words, are doing most of the visible work.

What the HDI cannot show is whether that progress is reaching people evenly — and this is exactly the gap BD Digital Access was built to probe from a different angle. If digital access, digital literacy, and mobile-based financial inclusion are increasingly upstream of both the education and income components of HDI, then the open question is whether Bangladesh's digital-access gains are following the same geography as its HDI gains, or whether they are lagging behind in precisely the districts where development progress most needs them. Joining sub-national HDI or proxy indicators with the digital-access data already used in BD Digital Access is the natural next step for this line of work.

## Why this matters here

This note started as a snapshot and turned into something more specific once the full 34-year series was in hand: Bangladesh did not simply grow quickly, it closed a real gap with a larger neighbor while a country that once led the region fell behind. That is the kind of finding that only shows up when you go past the headline number and look at the shape of the trend, which is the habit I would want to bring to the DAI Hub: not just tracking whether a country's indicators are moving in the right direction, but understanding the shape of that movement well enough to ask what is actually driving it, and who it is and isn't reaching yet.

---

## Data and reproducibility

- `bangladesh_south_asia_hdi.csv`- the extracted HDI series (1990–2023) for the five countries used in this analysis.
- `build_charts.py`- the script that generates both charts from that file. Run with `python3 build_charts.py`.
- Full source dataset (all countries, all years): UNDP Human Development Report Office, ["All composite indices and components time series (1990–2023)"](https://hdr.undp.org/data-center/documentation-and-downloads).
