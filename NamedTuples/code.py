from collections import namedtuple

# color = (55, 155, 255)
# color = {'red': 55, 'green': 155, 'blue': 255}
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)

print(color.red)
