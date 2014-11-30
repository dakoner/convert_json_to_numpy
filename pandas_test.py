import datetime
import pandas
import os
from matplotlib import pyplot
pandas.options.display.mpl_style = 'default'

base = os.getcwd()
path = os.path.join(base, 'example_weather.hf5')
store = pandas.HDFStore(path)
print store

data = []
for key in store.keys():
    d = store.get(key)
    k= key[10:]
    data.append(d)

p = pandas.concat(data)

p.set_index(p["created_at"], inplace=True)
p.sort_index()
for var in 'pressure', 'outside_temp':
    # station = 1337
    # p2 = p[p['station.uuid'] == station]
    # p3 = p2[[var]]

    p2 = p[['created_at', 'station.uuid', var, 'us_units']]
    p2=p2.dropna(axis=0)
    p2.to_csv("%s.csv" % var)
    # p3 = p2.groupby(level=0)
    # p4 = p3.last()
    # p5 = p4.pivot('created_at', 'station.uuid', var)
    # p5.plot()

# import code
# code.interact(local=locals())
