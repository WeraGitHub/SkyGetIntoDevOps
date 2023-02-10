from math import pi, tan, cos

height_of_the_barrel = 1
horizontal_distance = 0.5
gravity_acceleration = 9.8
elevation_in_degrees = 80
elevation_in_radians = elevation_in_degrees * (pi/180)
initial_velocity = 44


projectile = height_of_the_barrel + (horizontal_distance * tan(elevation_in_radians))\
             - ((gravity_acceleration * horizontal_distance ** 2)
                / (2 * (initial_velocity * cos(elevation_in_radians))**2))

print(projectile)

y0 = 1
x = 0.5
g = 9.8
elevation_in_degrees = 80
theta = elevation_in_degrees * (pi/180)
v0 = 44


projectile2 = y0 + x * tan(theta) - (g * (x ** 2)) / (2 * (v0 * cos(theta)) ** 2)

print(projectile2)
