from PIL import Image, ImageDraw
from math import sin, cos, radians, pi, degrees
import random
import time

width = 800
height = 800

image = Image.new("RGB",(width,height),(0,0,0))
draw = ImageDraw.Draw(image)

class line_drawer():
	def __init__(self,source_x,source_y,angle,color = (255,255,255)):
		self.angle = angle
		self.x = source_x
		self.y = source_y
		self.avr_line_length = 10
		self.avr_line_interval = 5
		self.color = color
		self.draw()


	def inside (self):
		if self.x <= width and self.x >= 0 and self.y<=height and self.y>=0:
			return True
		else:
			return False

	def draw(self):
		while(self.inside()):
			line_length = min(self.avr_line_length * 2, max(self.avr_line_length/2, random.gauss(self.avr_line_length, 1)))
			new_x = self.x + cos(radians(self.angle)) * line_length
			new_y = self.y + sin(radians(self.angle)) * line_length 
			draw.line([self.x,self.y,new_x,new_y],fill = self.color)
			new_x = new_x + cos(radians(self.angle)) * self.avr_line_interval
			new_y = new_y + sin(radians(self.angle)) * self.avr_line_interval
			self.x = new_x
			self.y = new_y


class Light():
	def __init__(self,x,y,angle,angle_width,lines,color = (255,255,255)):
		self.source_x = x
		self.source_y = y 
		#self.default_brightness  = 100
		self.lines = 100
		self.angles = (angle-angle_width/2,angle+angle_width/2)
		self.color = color
		self.draw_lines()

	def draw_lines(self):
		min_angle,max_angle = self.angles
		dif_angle = abs(min_angle-max_angle)
		angle = min_angle
		for line in range(self.lines):
			line_drawer(self.source_x,self.source_y,angle,self.color)
			angle += float(dif_angle/self.lines)

# Draws circles with short lines.
def circle_light(x,y,line_length):
	for radius in range(30, 400):
		x1 = x - radius
		y1 = y - radius
		x2 = x + radius
		y2 = y + radius

		#arc_length = (math.pi*radius*2) * (angle/360)
		central_angle = degrees(line_length/radius)
		print("r {} central_angle {}".format(radius,central_angle))
		start = random.randint(0,int(360-central_angle))
		end = start + central_angle
		draw.arc((x1, y1, x2, y2), start=start, end=end, fill=(255, 255, 0))


# Draws circles with short lines. Draws until certain angle is covered in each circle.
def circle_light2(x,y,line_length):
	angle_coverage = 30

	for radius in range(30, 400,1):
		x1 = x - radius
		y1 = y - radius
		x2 = x + radius
		y2 = y + radius

		central_angle = degrees(line_length/radius)
		print("r {} central_angle {}".format(radius,central_angle))
		total_angle = central_angle
		while(total_angle<angle_coverage):
			start = random.randint(0,int(360-central_angle))
			end = start + central_angle
			draw.arc((x1, y1, x2, y2), start=start, end=end, fill=(255, 255, 0))
			total_angle+=central_angle

circle_light2(100,100, 10)
Light(0, height/2,0,60,25)

image.show()
timestr = time.strftime("%Y%m%d-%H%M%S")
image.save(timestr + ".png", 'PNG')
