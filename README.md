# DIT4BEARS "Smart Roads — WinterRoad Maintenance 2021"
## Code & suggestions

## Dependencies

OSMNX - for building roads graph and collection geospatial data
wwo_hist - for collecting weather data
pyowm - for collecting UV-index data
dgl - for GNN training

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

