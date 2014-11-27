import os
import pandas
import json
import numpy
src = "/home/dek"
#src = "c:/Users/dek/Projects"
base = os.path.join(src, "d3webview/app/src/main/assets/static_html")
path = os.path.join(base, "test/example_weather.json")
hdf_output = os.path.join(base, "example_weather.hf5")

data = json.load(open(path))
d = pandas.io.json.json_normalize(data["weatherdata"])
d["collected_at"] = pandas.to_datetime(d["collected_at"])
d["created_at"] = pandas.to_datetime(d["created_at"])
d.set_index(d["created_at"], inplace=True)
# Can't be serialized due to differing dtypes.
d.drop("raw", 1, inplace=True)
d.drop("version", 1, inplace=True)
store = pandas.HDFStore(hdf_output, mode="a")
store.put("data", d, format="table")
store.close()
