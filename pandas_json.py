import pandas
import json
import numpy
path="c:/Users/dek/Desktop/example_weather.json"
output="c:/Users/dek/Desktop/example_weather.csv"
output2="c:/Users/dek/Desktop/example_weather_dates.csv"

#d=pandas.io.json.read_json(path)
data = json.load(open(path))
d=pandas.io.json.json_normalize(data["weatherdata"])
d.to_csv(output)
d2=pandas.read_csv(output,index_col=0,parse_dates=["created_at", "collected_at"])
#d2.index=[d2['created_at'],d2['uuid']]
#d2 = d2.drop('created_at.1',1)
#d2 = d2.drop('created_at',1)
#d2 = d2.drop('uuid',1)
d2.to_csv(output2)

import code
code.interact(local=locals())