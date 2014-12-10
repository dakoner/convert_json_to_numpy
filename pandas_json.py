import Queue
import os
import pandas
import json
import numpy
import urllib
import threading
from matplotlib import pyplot

# vars = (
#     "wind_direction", "outside_humidity", "outside_temp", "inside_temp",
#     "pressure", "daily_rain", "heatindex", "barometer", "rain", "hourly_rain",
#     "inside_humidity", "altimeter", "wind_gust", "wind_gust_direction",
#     "windchill", "total_rain", "dewpoint", "rain_rate", "solar_wm2",
#     "uv_index")


class RequestThread(threading.Thread):

  def __init__(self, station, q):
    threading.Thread.__init__(self)
    self.station = station
    self.q = q

  def run(self):
    url = "http://goosci-outreach.appspot.com/weather/%s" % station
    filename = "%s.json" % station
    print "Reading response from station", station
    urllib.urlretrieve(url, filename)
    print "Response read from station", station
    with open(filename) as f:
      response = "".join(line for line in f)
    self.q.put((self.station, response))


# TODO(dek): make sure this doesn't append the same dataset over and over

url = "http://goosci-outreach.appspot.com/stations"
response = urllib.urlopen(url)
json_data = json.loads(response.read())

stations = [station["uuid"] for station in json_data["stations"]]

requests = []
q = Queue.Queue(len(stations))

for station in stations:
  print "Requesting station", station
  request = RequestThread(station, q)
  requests.append(request)
  request.start()

# for i in range(len(stations)):
  r = q.get()

# #src = "c:/Users/dek/Projects"
# #base = os.path.join(src, "d3webview/app/src/main/assets/static_html")
# #path = os.path.join(base, "test/example_weather.json")

import code
code.interact(local=locals())
