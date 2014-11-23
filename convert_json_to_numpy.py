import json
import numpy


INT_FILL_VALUE=999999
FLOAT_FILL_VALUE=1e+20
fields = [
    ("created_at", object),
    ("uuid", numpy.int),
    ("rssi", numpy.int),
    ("wind_direction", numpy.float),
    ("wind_speed", numpy.int),
    ("outside_temp", numpy.float),
    ("outside_humidity", numpy.float),
    ("rain_spoons", numpy.float),
    ("pressure", numpy.float),
    ("inside_temp", numpy.float)]
fill_values = []
for field in fields:
    if field[1] == object:
        fill_values.append("?")
    elif field[1] == numpy.int:
        fill_values.append(INT_FILL_VALUE)
    elif field[1] == numpy.float:
        fill_values.append(FLOAT_FILL_VALUE)

def convert_json_to_numpy(data):
    data2 = []
    mask=[]
    for item in data["weatherdata"][:1]:
        newitem = []
        itemmask = []
        for field in fields:
            if field[0] in item:
                newitem.append(item[field[0]])
                itemmask.append(0)
            else:
                if field[1] == numpy.int:
                    newitem.append(INT_FILL_VALUE)
                if field[1] == numpy.float:
                    newitem.append(FLOAT_FILL_VALUE)
                itemmask.append(1)
        mask.append(tuple(itemmask))
        data2.append(numpy.array([tuple(newitem)], dtype=numpy.dtype(fields)))
        return numpy.ma.array(data2, mask=mask)

if __name__ == '__main__':
    f = open("c:/Users/dek/Projects/d3webview/app/src/main/assets/static_html/foo.json")
    data = json.load(f)
    n = convert_json_to_numpy(data)
    import pdb; pdb.set_trace()