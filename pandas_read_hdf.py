import pandas

import os
import pandas
from matplotlib import pyplot
pandas.options.display.mpl_style = 'default'

src = "c:/Users/dek/Projects"
base = os.path.join(src, "d3webview/app/src/main/assets/static_html")
path = os.path.join(base, 'example_weather.hf5')

store = pandas.HDFStore(path)

d2 = store.get('data')
#store.select('data', "index >= '2014-11-25'")
#store.close()


# d2 = d2.drop('Unnamed: 0', 1)

# x = d2.loc[:, ['outside_temp']]
# in gnuplot:
# set xdata time
# set timefmt "%Y-%m-%d %H:%M:%S"
# set datafile separator ","
# plot "c:/Users/dek/Desktop/test.csv" every ::1 using 1:2:3 with points palette

# d2[['outside_temp', 'uuid']].to_csv(
#     'c:/Users/dek/Desktop/test2.csv', na_rep='NaN')


## This will resample two stations at 5Min interval, then merge the resampled.
#u1=d2[d2['uuid']==1][['uuid','outside_temp']].resample('5Min');u1['uuid']=1
#u3=d2[d2['uuid']==3][['uuid','outside_temp']].resample('5Min');u3['uuid']=3
#pandas.concat([u1, u3]).sort_index()

#x=d2[['created_at','uuid','outside_temp']]
#y=x.pivot_table(index = 'created_at', columns='uuid').resample('5Min')
#y.plot()
#pyplot.show()

pandas.set_option('display.width', 235)
import code
code.interact(local=locals())
