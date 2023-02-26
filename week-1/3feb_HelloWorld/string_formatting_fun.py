# dictionary
# key : value
# Mercury : 57.91

planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}
print(planets)
print(planets['Earth'])

for planet_number, planet in enumerate(planets.keys(), start=1):
    print(planet_number, ': ',  planet, ': ', planets[planet])

for planet_number, planet in enumerate(planets.keys(), start=1):
    print("{:2d}. {:<10s} is {:06.2f} Gm from sun".format(planet_number, planet, planets[planet]))

# literal string interpolation
for planet_number, planet in enumerate(planets.keys(), start=1):
    print(f"{planet_number:2d}. {planet:<10s} is {planets[planet]:06.2f} Gm from sun")


# slicing strings
message = "Goodbye Python"
print(message)

print(message[4:8])
print(message[8:])


print('Group exercise \n------------------')

# create a string variable
line = 'root::0:0:superuser:/root:/bin/sh'
# create a list by splitting string elements on double colon characters
elems = line.split(':')
print(elems)
# replace first item in the list with string avatar
elems[0] = 'avatar'
# replace fourth item in the list with string The super-user (zero)
elems[4] = 'The super-user (zero)'
line = ':'.join(elems)  # using method .join to create a string out of elems list
print(line)
