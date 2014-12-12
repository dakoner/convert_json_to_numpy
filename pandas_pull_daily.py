import Queue
import os
import pandas
import json
import numpy
import urllib
import threading
from datetime import date, timedelta


def get_data(json_data):
  d = pandas.io.json.json_normalize(json.loads(json_data)["weatherdata"])
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


class RequestThread(threading.Thread):

  def __init__(self, day, q):
    threading.Thread.__init__(self)
    self.day = day
    self.q = q

  def run(self):
    url = (
        "http://goosci-outreach.appspot.com.storage.googleapis.com/cross-sectional/%s.json" % str(self.day))
    filename = "%s.json" % self.day
    print "Reading response from day", self.day
    urllib.urlretrieve(url, filename)
    print "Response read from day", self.day
    with open(filename) as f:
      response = "".join(line for line in f)
    self.q.put((self.day, get_data(response)))


# TODO(dek): make sure this doesn't append the same dataset over and over

startday = date(2014, 10, 16)
endday = date(2014, 12, 10)

day = timedelta(1)
days = []
while startday <= endday:
  days.append(startday)
  startday += day

print days
q = Queue.Queue(len(days))

requests = []
for day in days:
  print "Requesting day", day
  request = RequestThread(day, q)
  requests.append(request)
  request.start()

# Uncomment the following line to make the operation run in parallel.

data = []
for i in range(len(days)):
  r = q.get()
  data.append(r[1])

data = pandas.concat(data)

base = os.getcwd()
hdf_output = os.path.join(base, "example_weather.hf5")

store = pandas.HDFStore(hdf_output, mode="a", complib="zlib", complevel=9)
store.put("data", data)
store.close()
