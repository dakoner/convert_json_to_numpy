import pandas

path="c:/Users/dek/Desktop/example_weather_dates.csv"

d2=pandas.read_csv(path)
#d2.index=d2['created_at']

#d2.index=[d2['created_at'],d2['uuid']]
d2.index = pandas.to_datetime(d2['created_at'])

d2 = d2.drop('created_at',1)
#d2 = d2.drop('uuid',1)
d2 = d2.drop('Unnamed: 0',1)
x=d2.loc[:,['outside_temp']]
x.to_csv("c:/Users/dek/Desktop/test.csv")
# in gnuplot:
# set xdata time
# set timefmt "%Y-%m-%d %H:%M:%S"
# set datafile separator ","
# plot "c:/Users/dek/Desktop/test.csv" every ::1 using 1:2:3 with points palette

d2[['outside_temp','uuid']].to_csv("c:/Users/dek/Desktop/test2.csv",na_rep='NaN')

print(d2.keys())
print(d2.index.names)
