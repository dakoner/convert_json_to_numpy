import os
import pandas
import json
import numpy
base = "/usr/local/google/home/dek/d3webview/app/src/main/assets/static_html"
path = os.path.join(base, "example_weather.json")
hdf_output = os.path.join(base, "example_weather.hf5")

data = json.load(open(path))
d = pandas.io.json.json_normalize(data["weatherdata"])
d["collected_at"] = pandas.to_datetime(d["collected_at"])
d["created_at"] = pandas.to_datetime(d["created_at"])
# Can't be serialized due to differing dtypes.
d.drop("raw", 1, inplace=True)
d.drop("version", 1, inplace=True)
store = pandas.HDFStore(hdf_output, mode="w")
store.put("data", d)
store.close()
