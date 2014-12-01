import os
import pandas
import json
import numpy
import urllib
from matplotlib import pyplot

vars = "wind_direction", "outside_humidity", "outside_temp", "inside_temp","pressure","daily_rain","heatindex","barometer","rain","hourly_rain","inside_humidity","altimeter","wind_gust","wind_gust_direction","windchill","total_rain","dewpoint", "rain_rate", "solar_wm2", "uv_index"

def get_data(json_data):
    d = pandas.io.json.json_normalize(json_data["weatherdata"])
    d["collected_at"] = pandas.to_datetime(d["collected_at"])
    d["created_at"] = pandas.to_datetime(d["created_at"])
    for var in vars:
        d[var] = d[var].astype(float)
    d.drop("raw", 1, inplace=True)
    d.drop("version", 1, inplace=True)
#    d.set_index(d["created_at"], inplace=True)

    return d

def store_data(hdf_output, data):
    store = pandas.HDFStore(hdf_output, mode="a")
    store.put("data", data, format="table")
    store.close()


# url = "http://goosci-outreach.appspot.com/weather/%s" % 202481588171316
# response = urllib.urlopen(url)
# json_data = json.loads(response.read())
# data=get_data(json_data)



url = "http://goosci-outreach.appspot.com/stations"
response = urllib.urlopen(url)
json_data = json.loads(response.read())

stations = [station['uuid'] for station in json_data['stations']]
print stations

base = os.getcwd()
hdf_output = os.path.join(base, "example_weather.hf5")
## TODO(dek): make sure this doesn't append the same dataset over and over
store = pandas.HDFStore(hdf_output, mode="a")


for station in stations:
    print "station", station
    url = "http://goosci-outreach.appspot.com/weather/%s" % station
    response = urllib.urlopen(url)
    r = response.read()
    open("%s.json" % station, "w").write(r)
    json_data = json.loads(r)
    try:
        data=get_data(json_data)
        store.put("station/S%s" % station, data)#, format="table")
    except KeyError:
        pass

store.close()
# #src = "c:/Users/dek/Projects"
# #base = os.path.join(src, "d3webview/app/src/main/assets/static_html")
# #path = os.path.join(base, "test/example_weather.json")

import code
code.interact(local=locals())
