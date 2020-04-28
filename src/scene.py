from PIL import Image, ImageDraw
from math import sin, cos, radians
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
			print(line_length)
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

Light(0, height/2,0,60,50)
Light(width/2,0,90,60,50,(255,0,0))
Light(width, height/2,180,60,50,(0,255,0))
Light(width/2,height,270,60,50,(0,0,255))


image.show()
timestr = time.strftime("%Y%m%d-%H%M%S")
image.save(timestr + ".png", 'PNG')
r
