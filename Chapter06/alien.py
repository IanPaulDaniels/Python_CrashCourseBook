alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

alien_0['x-position'] = 0
alien_0['y-position'] = 25
alien_0['speed'] = 'medium'

print(alien_0)

print('The alien is ' + alien_0['color'])

alien_0['color'] = 'yellow'

print('The alien is now ' + alien_0['color'])

print('\nOriginal X position: ' + str(alien_0['x-position']))

# Move the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x-position'] += x_increment

print("New X Position: " + str(alien_0['x-position']))

del alien_0['points']

print(alien_0)
