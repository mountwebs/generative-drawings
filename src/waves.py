from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image, ImageDraw
import math
import random

im = Image.new('RGBA', (2000, 2000), "#516a76")
draw = ImageDraw.Draw(im)

scale = 2
width, height = im.size
def get_sine_list(x, frequency, amplitude):
  coordinates = []
  wave_y = 0
  while (wave_y < height):
    wave_x = x + amplitude * math.sin(wave_y/frequency - math.radians(150)) # + math.radians(180) 
    coordinates.append((wave_x,wave_y))
    wave_y+=1
  return coordinates

colors = ["#F2545B","#A93F55","#19323C","#19323C","#F3F7F0","#8C5E58"]
stone_colors = ["#3d3b3e","#5a7684","#72869f","#94afc0",
                "#dee4e2","#7a89a6","#8b9cb8","#a3928b",
                "#8ba392","#bba6a1","#9faeab","#bed9e2","#728287","#92837d",
                "#abb6b8","#9faeab","#b5c49b","#bfc9c1"]

def color_picker(color_list):
  n = len(color_list)
  color = color_list[random.randint(0,n-1)]
  return color

def draw_list(path_list,width,color):
  xy = path_list[0]
  for c in path_list:
    draw.line([xy,c],width = width,fill = color)
    xy = c

x = 40 * scale
amplitude = 0.05 * scale
frequency = 30 * scale
count = 0
while x < width + 200:
  draw_list(get_sine_list(x, frequency, amplitude),18 * scale ,color_picker(stone_colors))
  #plus = 0.97**count
  amplitude+=1.05 * scale
  frequency+=1 * scale
  x += 10 * scale
  count+=1

mask_im = Image.new("L", im.size, 0)
draw = ImageDraw.Draw(mask_im)
for x in range(0,width,2):
    for y in range(0,height,2):
        if random.random() < 0.4:
            a = random.randint(0,25)
            draw.point((x, y), fill=a)

imt = Image.new('RGB', im.size, (255, 255, 255))
im.paste(imt, (0, 0), mask_im)

name = "draw_sine"
timestr = time.strftime("%Y%m%d-%H%M%S")
im.save(timestr + " " + name + ".png")
