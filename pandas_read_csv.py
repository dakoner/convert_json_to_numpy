import pandas

path="c:/Users/dek/Desktop/example_weather_dates.csv"

d2=pandas.read_csv(path)
#d2.index=d2['created_at']

#d2.index=[d2['created_at'],d2['uuid']]
d2.index = pandas.to_datetime(d2['created_at'])

d2 = d2.drop('created_at',1)
#d2 = d2.drop('uuid',1)
d2 = d2.drop('Unnamed: 0',1)

print(d2.keys())
print(d2.index.names)
