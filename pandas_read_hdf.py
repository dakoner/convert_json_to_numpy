import pandas

import os
import pandas
import json
src = "c:/Users/dek/Projects"
base = os.path.join(src, "d3webview/app/src/main/assets/static_html")
path = os.path.join(base, 'example_weather.hf5')

store = pandas.HDFStore(path)

d2 = store.get('data')
store.close()


# d2 = d2.drop('Unnamed: 0', 1)

# x = d2.loc[:, ['outside_temp']]
# in gnuplot:
# set xdata time
# set timefmt "%Y-%m-%d %H:%M:%S"
# set datafile separator ","
# plot "c:/Users/dek/Desktop/test.csv" every ::1 using 1:2:3 with points palette

# d2[['outside_temp', 'uuid']].to_csv(
#     'c:/Users/dek/Desktop/test2.csv', na_rep='NaN')


pandas.set_option('display.width', 235)
import code
code.interact(local=locals())
