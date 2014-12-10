import urllib
import json
import datetime
import pandas
import os


def get_data(json_data):
  d = pandas.io.json.json_normalize(json_data["weatherdata"])
  d["collected_at"] = pandas.to_datetime(d["collected_at"])
  d["created_at"] = pandas.to_datetime(d["created_at"])
  d.drop("raw", 1, inplace=True)
  d.drop("version", 1, inplace=True)
  vars = (
      "wind_direction", "outside_humidity", "outside_temp", "inside_temp",
      "pressure", "daily_rain", "heatindex", "barometer", "rain", "hourly_rain",
      "inside_humidity", "altimeter", "wind_gust", "wind_gust_direction",
      "windchill", "total_rain", "dewpoint", "rain_rate", "solar_wm2",
      "uv_index")
  for var in vars:
    d[var] = d[var].astype(float)

  return d


url = "http://goosci-outreach.appspot.com/stations"
response = urllib.urlopen(url)
json_data = json.loads(response.read())

stations = [station["uuid"] for station in json_data["stations"]]

base = os.getcwd()
hdf_output = os.path.join(base, "example_weather.hf5")

store = pandas.HDFStore(hdf_output, mode="a", complib="zlib", complevel=9)
for station in stations:
  f = open("%s.json" % station)
  value = f.read()
  try:
    j = json.loads(value)
  except ValueError:
    print "Failed to parse", station
  data = get_data(j)

  store.put("station/S%s" % station, data)  # , format="table")
store.close()
