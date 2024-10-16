def water_column_height(tower_height, tank_height): # Calculate the height of the water column
    t = float(tower_height)
    w = float(tank_height)
    w = w*3
    out = t + (w/4)
    return out

def pressure_gain_from_water_height(column_hight):
    density = 998.2 # kg/meter^2
    g = 9.80665 # meter/second^2
    h = float(column_hight) # meters
    out = density * g * h 
    out = out/1000
    return out
