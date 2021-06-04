# DIT4BEARS "Smart Roads — WinterRoad Maintenance 2021"
## Code & suggestions

## Dependencies

OSMNX - for building roads graph and collection geospatial data
wwo_hist - for collecting weather data
pyowm - for collecting UV-index data
dgl - for GNN training

## Labels (Safety metric)

    label = accidents rate of roadway condition * accidents rate of friction interval

### Accidents rate of friction interval

| Friction    | Rate |
|-------------|------|
| < 0.15      | 0.8  |
| 0.15 - 0.24 | 0.55 |
| 0.25 - 0.44 | 0.25 |
| 0.35 – 0.44 | 0.2  |

### Accidents rate of roadway condition

| Friction | State |
|----------|-------|
| Dry      | 0.12  |
| Moist    | 0.16  |
| Wet      | 0.16  |
| Icy      | 0.53  |
| Snowy    | 0.3   |
| Slushy   | 0.18  |

### Safety metric

| Friction/State | Dry   | Moist | Wet   | Icy    | Snowy | Slushy |
|----------------|-------|-------|-------|--------|-------|--------|
| < 0.15         | 0.096 | 0.128 | 0.128 | 0.424  | 0.24  | 0.144  |
| 0.15 – 0.24    | 0.066 | 0.088 | 0.088 | 0.2915 | 0.165 | 0.099  |
| 0.25 – 0.34    | 0.03  | 0.04  | 0.04  | 0.1325 | 0.075 | 0.045  |
| 0.35 – 0.44    | 0.024 | 0.032 | 0.032 | 0.106  | 0.06  | 0.036  |


## How to install

    pip install -r /path/to/requirements.txt

## How to use

Preprocess road conditions data and collect weather data using utilities from /util and add OSM information using process_osmnx.py.

Continue modifying the gnn.py code:
- in function build_graph():
  - replace src array with indices of points where roads start
  - replace dst array with indices of points where roads end
  - keep new graph bi-directional, OSMNX will handle directions
- for graph G set:
  - G.ndata["feature"] - np.array with information about weather in points
  - G.edata["feature"] - np.array with information about road conditions in edges
  - G.edata["label"] - safety metric
  - G.edata["train_mask"] - train-test split

## Citing
A. Krutsylo and Md. A. Jahin (2021) DIT [Source code]. https://github.com/DentonJC/DIT. 

## References
- https://www.teconer.fi/en/surface-condition-friction-measurements/#RCM411
- http://www.diva-portal.org/smash/get/diva2:673366/FULLTEXT01.pdf
