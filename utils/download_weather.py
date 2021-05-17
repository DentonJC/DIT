from wwo_hist import retrieve_hist_data
import pandas as pd
import numpy as np

frequency=1 #hrs
start = "30-NOV-2020"
end = "10-MAR-2021"

api_key = "API_KEY"

result = retrieve_hist_data(api_key,
                                ['narvik'],
                                start,
                                end,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
print(result)
