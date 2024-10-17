def water_column_height(tower_height, tank_height): # Calculate the height of the water column
    t = float(tower_height)
    w = float(tank_height)
    w = w*3
    out = t + (w/4)
    return out

def pressure_gain_from_water_height(column_hight):
    density = 998.2 # kg/meter^3
    g = 9.80665 # meter/second^2
    h = float(column_hight) # meters
    out = density * g * h 
    out = out/1000
    return out

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    f = friction_factor
    p = 998.2 # kg/meter^2
    l = pipe_length #in meters
    d = pipe_diameter * 2000 #in meters
    v = fluid_velocity**2
    out = -(f*l*p*v)
    out = out/d
    return out