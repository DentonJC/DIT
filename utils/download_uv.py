from pyowm import OWM
import datetime

owm = OWM("API_KEY")
mgr = owm.uvindex_manager()

uvi_history_list = mgr.uvindex_history_around_coords(
    68.420556, 17.56,
    datetime.datetime(2020, 11, 30, 0, 0, 0),
    end=datetime.datetime(2021, 3, 3, 0, 0, 0))

with open('uv_narvik.csv', 'a') as f:
    for uvi in uvi_history_list:
        f.write(str(uvi) + '\n')

