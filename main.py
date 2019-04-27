# Proj. Name: Final Project
# Author: Matthew Wong
# Date: 1/18/2019

from PIL import Image 

# Open Image
image = Image.open("redball.jpeg")

# Create a list to store the pixels that are yellow
x_cord = []
y_cord = []
highest_x = 0
highest_y = 0

# Find red pixels(the ball) in picture (highest x and y + lowest x and y)
def colour(r, g, b):
  if r > 175 and g < 100 and b < 100:
    return 'red'

# Go through all the pixels in the image to find the red pixels
width = image.width
height = image.height

for y in range(height):
  for x in range(width):
    red = image.getpixel((x,y))[0]
    green = image.getpixel((x,y))[1]
    blue = image.getpixel((x,y))[2]

# Take and append Red x and y cords
    if colour(red, green, blue) == "red":
      x_cord.append(x)
      y_cord.append(y)

# Find highest x
for m in x_cord: 
  if m > highest_x: 
    highest_x = m

# Find highest y
for n in y_cord:
  if n > highest_y:
    highest_y = n

# Find lowest cords
lowest_x = highest_x
lowest_y = highest_y

# Find lowest x
for m in x_cord:
  if m < lowest_x:
    lowest_x = m

# Find lowest y
for n in y_cord:
  if n < lowest_y:
    lowest_y = n

#print(lowest_x)

# Find radius between highest/lowest x and y cords
distance_x = (highest_x - lowest_x) / 2
distance_y = (highest_y - lowest_y) / 2

# Find final cord
final_x = lowest_x + distance_x
final_y = lowest_y + distance_y

# Print new cordinate 
print("The middle of the ball is, (" + str(final_x) + "," + str(final_y) + ")")