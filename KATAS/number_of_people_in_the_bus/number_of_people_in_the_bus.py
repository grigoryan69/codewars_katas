def number(*bus_stops):
    x = 0
    for i in range(len(*bus_stops)):
        x += (bus_stops[0][i][0] - bus_stops[0][i][1])
    return x