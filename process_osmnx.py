import osmnx as ox
import numpy as np
import pandas as pd
from tqdm import tqdm


G = ox.graph_from_bbox(68.580, 68.093, 17.757, 16.262, network_type='drive', simplify=False, retain_all=True)
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)
hwy_speeds = {'residential': 35,
              'secondary': 50,
              'tertiary': 60}
G = ox.add_edge_speeds(G, hwy_speeds)
G = ox.add_edge_travel_times(G)

gdf_edges = ox.graph_to_gdfs(G, nodes=False)

def get_ed(x, y, gdf_edges, G):
    edge = ox.get_nearest_edge(G, (x, y))
    
    try:
        u, v = edge[0], edge[1]
        res = gdf_edges.query("u == " + str(u)).query("v == " + str(v))
    except:    
        u, v = edge[0][0], edge[0][1]
        res = gdf_edges.query("u == " + str(u)).query("v == " + str(v))
   
    return res

df = pd.read_csv('data.csv', sep=',')
df = df[df['Latitude'].notna()]
df = df[df['Longitude'].notna()]
df.sort_values(by = ['Latitude', 'Longitude'], ascending = [True, True], na_position = 'first')

df.to_csv('data_prep.csv')

with open("data_osmnx.csv", 'w') as f:
    f.write(','.join(list(gdf_edges)) + '\n')

prev_lat = 0
prev_lon = 0
prev_line = 0
with open("data_osmnx.csv", 'a') as f:
    for i in tqdm(range(len(df.Latitude))):
        lat = round(df.Latitude[i], 4)
        lon = round(df.Longitude[i], 4)
        if prev_lat == lat and prev_lon == lon:
            line = prev_line
        else:
            line = get_ed(lat, lon, gdf_edges, G).values[0]
        print(line)
        f.write(','.join([str(j) for j in line]) + '\n')
        prev_lat, prev_lon, prev_line = lat, lon, line
        
