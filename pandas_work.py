import urllib
import json
import datetime
import pandas
import os
from matplotlib import pyplot
pandas.options.display.mpl_style = 'default'

base = os.getcwd()
hdf_output = os.path.join(base, 'example_weather.hf5')
store = pandas.HDFStore(hdf_output)

p = store.get('data')
p.set_index(p['created_at'], inplace=True)
p.sort_index()
vars = (
    'outside_temp', 'pressure', 'rain_spoons', 'inside_humidity', 'inside_temp',
    'outside_humidity')
q = ['station.uuid']
q.extend(vars)
p1 = p[p['us_units'] == 0][q]
import code
code.interact(local=locals())
