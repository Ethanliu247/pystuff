#!/usr/bin/python3 
from math import sin, cos, radians, degrees
from tkinter import *
from time import sleep
from sys import exit

root = Tk()
root.title("3D Engine")
height = 500
width = 500
root.geometry(str(height+100)+'x'+str(width)+'+0+0')
root.focus()

canvas = Canvas(root, width=width, height=height, bg='SteelBlue1')
info = Label(root, text='2D Projection of 3D Points', fg='blue')
info.pack()
canvas.pack()
object_buffer = []
objects = []

def die(k, msg='Application closed by user.', status=0):
	print(msg)
	exit(status)

class Camera:
	def __init__(self, x, y, z, thetaX, thetaY, thetaZ):
		self.x, self.y, self.z = x, y, z
		self.thetaX = thetaX
		self.thetaY = thetaY
		self.thetaZ = thetaZ
		self.xspeed = 1
		self.yspeed = 1
		self.zspeed = 1
		self.xrot = 1
		self.yrot = 1
		self.zrot = 1
		self.rcap = 10
		self.scap = 20
		self.moving = False
	def move_true(self):
		self.moving = True
	def move_false(self):
		self.moving = False
	def movex(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.xspeed <= self.scap:
			self.xspeed += 1
		self.x += self.xspeed*mod
	def movey(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.yspeed <= self.scap:
			self.yspeed += 1
		self.y += self.yspeed*mod
	def movez(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.zspeed <= self.scap:
			self.zspeed += 1
		self.z += self.zspeed*mod
	def rotx(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.xrot <= self.rcap:
			self.xrot += 1
		self.thetaX += self.xrot*mod
	def roty(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.yrot <= self.rcap:
			self.yrot += 1
		self.thetaY += self.yrot*mod
	def rotz(self, mod):
		self.move_true()
		canvas.after(100, self.move_false)
		if self.zrot <= self.rcap:
			self.zrot += 1
		self.thetaZ += self.zrot*mod

def rotate(xyz, theta, axis):
	theta = radians(theta)
	x, y, z = xyz
	nx, ny, nz = x, y, z
	if axis == 'x':
		ny = cos(theta)*y - sin(theta)*z
		nz = sin(theta)*y + cos(theta)*z
	elif axis == 'y':
		nx = cos(theta)*x - sin(theta)*z
		nz = sin(theta)*x + cos(theta)*z
	elif axis == 'z':
		nx = cos(theta)*x - sin(theta)*y
		ny = sin(theta)*x + cos(theta)*y
	else:
		return 1
	return round(nx, 2), round(ny, 2), round(nz, 2)

def map_rotation(xyz, cam):
	x, y, z = xyz
	x -= cam.x
	y -= cam.y
	z -= cam.z
	x, y, z = rotate((x, y, z), cam.thetaX, 'x')
	x, y, z = rotate((x, y, z), cam.thetaY, 'y')
	x, y, z = rotate((x, y, z), cam.thetaZ, 'z')
	return x, y, z

def map_2d(mapped_xyz, scale=1):
	x, y, z = mapped_xyz
	if z >= 0:
		return width*100, height*100
	newx = ((width / 2) * x / z)*scale
	newy = ((height / 2) * y / z)*scale
	return round(newx+width/2, 2), round(newy+height/2, 2)

def convert(cam, x, y, z, scale=1):
	return map_2d(map_rotation((x, y, z), cam), scale)

class Cube:
	def __init__(self, x, y, z, scale=1, color='green', debug=False):
		self.debug = debug
		self.color = color
		objects.append(self)
		self.scale = scale
		self.points = [(100+x, 100+y, 100+z), (-100+x, 100+y, 100+z), (-100+x, -100+y, 100+z), (100+x, -100+y, 100+z),
							(100+x, 100+y, -100+z), (-100+x, 100+y, -100+z), (-100+x, -100+y, -100+z), (100+x, -100+y, -100+z)]
		self.lines = []
		for i in range(len(self.points)):
			try:
				if i < 3 or i > 3:
					self.lines.append((self.points[i], self.points[i+1]))
				else:
					continue
			except IndexError:
				self.lines.append((self.points[-1], self.points[4]))
				self.lines.append((self.points[0], self.points[3]))
				break
		for i in range(len(self.points)):
			try:
				self.lines.append((self.points[i], self.points[i+4]))
			except IndexError:
				break
		self.faces = [(self.points[0], self.points[1], self.points[2], self.points[3]),
					  (self.points[4], self.points[5], self.points[6], self.points[7]),
					  (self.points[1], self.points[2], self.points[6], self.points[5]),
					  (self.points[0], self.points[4], self.points[7], self.points[3]),
					  (self.points[3], self.points[7], self.points[6], self.points[2]),
					  (self.points[0], self.points[1], self.points[5], self.points[4])]
	def update(self):
		global object_buffer
		if self.debug:
			n = 0
			for point in self.points:
				print(point)
				coords = convert(camera, *point, scale=self.scale)
				object_buffer.append(canvas.create_rectangle(coords[0], coords[1], coords[0]+2, coords[1]+2, outline='', fill='black'))
				#object_buffer.append(canvas.create_text(coords[0], coords[1]+20, text=str(n)))
				n += 1
		for face in self.faces:
			object_buffer.append(canvas.create_polygon(*convert(camera, *face[0], scale=self.scale*0.99),
													   *convert(camera, *face[1], scale=self.scale*0.99),
													   *convert(camera, *face[2], scale=self.scale*0.99),
													   *convert(camera, *face[3], scale=self.scale*0.99),
													   fill=self.color, outline=''))
		for line in self.lines:
			#print(line)
			object_buffer.append(canvas.create_line(*convert(camera, *line[0], scale=self.scale),
													*convert(camera, *line[1], scale=self.scale),
													fill='black'))

class CustomShape:
	def __init__(self, points, lines, faces, color='grey', scale=1, debug=False):
		self.debug = debug
		objects.append(self)
		self.points = points
		self.lines = []
		self.faces = []
		self.scale = scale
		for line in lines:
			temp = []
			for point in line:
				temp.append(self.points[point])
			self.lines.append(temp)
		for face in faces:
			temp = []
			for point in face:
				temp.append(self.points[point])
			self.faces.append(temp)
		self.color = color

	def update(self):
		n = 0
		if self.debug:
			for point in self.points:
				coords = convert(camera, *point, scale=self.scale)
				object_buffer.append(canvas.create_rectangle(coords[0], coords[1], coords[0]+2, coords[1]+2, outline='', fill='black'))
				object_buffer.append(canvas.create_text(coords[0], coords[1]+20, text=str(n)))
				n += 1
		for face in self.faces:
			poly_coords = []
			for point in face:
				poly_coords.append(convert(camera, *point, scale=self.scale*0.99))
			object_buffer.append(canvas.create_polygon(*poly_coords, fill=self.color))
		for line in self.lines:
			#print(line)
			object_buffer.append(canvas.create_line(*convert(camera, *line[0], scale=self.scale),
													*convert(camera, *line[1], scale=self.scale)))

camera = Camera(0, -25, 400, 0, 0, 0)  # x is >, y is ^, and z is behind you
# Move
root.bind('<KeyPress-w>', lambda e: camera.movez(-1))
root.bind('<KeyPress-a>', lambda e: camera.movex(1))
root.bind('<KeyPress-s>', lambda e: camera.movez(1))
root.bind('<KeyPress-d>', lambda e: camera.movex(-1))
root.bind('<KeyPress-q>', lambda e: camera.movey(-1))
root.bind('<KeyPress-e>', lambda e: camera.movey(1))

root.bind('<Escape>', die, "Closed by user")

# Rotate
root.bind('<KeyPress-i>', lambda e: camera.rotx(-1))
root.bind('<KeyPress-j>', lambda e: camera.rotz(1))
root.bind('<KeyPress-k>', lambda e: camera.rotx(1))
root.bind('<KeyPress-l>', lambda e: camera.rotz(-1))
root.bind('<KeyPress-u>', lambda e: camera.roty(-1))
root.bind('<KeyPress-o>', lambda e: camera.roty(1))
'''
grass = CustomShape([[-1000, -99, -1000], [1000, -99, -1000], [1000, -99, 1000], [-1000, -99, 1000]],
					[[0,1], [1,2], [2,3], [3,0]],
					[[0,1,2,3]],
					color='forest green', scale=5)'''
house = Cube(0, 0, 0, color='firebrick')
roof = CustomShape([[0, 250, 0], [100, 100, 100], [-100, 100, 100], [-100, 100, -100], [100, 100, -100]],
					  [[0,1], [0,2], [0,3], [0,4], [1,2], [2,3], [3,4], [1,4]],
					  [[0,1,4], [0,2,3], [0,1,2], [0,3,4]],
					  color='saddle brown')
door = CustomShape([[-25, -100, 110], [-25, 0, 100], [-25, 0, 110], [-25, -100, 100], # right side 0 1 2 3
					[25, -100, 110], [25, 0, 100],[25, 0, 110], [25, -100, 100], # left side 4 5 6 7
					[15, -90, 110], [-15, -10, 110],[15, -10, 110], [-15, -90, 110], # front outline 8 9 10 11
					[10, -85, 110], [-10, -65, 110], [10, -65, 110], [-10, -85, 110], # bottom window 12 13 14 15
					[10, -35, 110], [-10, -15, 110], [10, -15, 110], [-10, -35, 110]], # top window 16 17 18 19
				   [[2,1],[1,3],[2,0],[3,0],
					[6,4],[5,7],[6,5],[7,4],
					[0,4],[1,5],[2,6],[3,7],
					[10,9],[9,11],[10,8],[11,8],
					[14,13],[13,15],[14,12],[15,12],
					[16,19],[17,18],[18,16],[19,17]],
				   [[1,2,0,3], [5,6,4,7], [6,2,0,4], [6,5,1,2], [7,3,0,4]],
				   color='sienna')
knob = CustomShape([[13, -49, 110], [15, -49, 110], [15, -51, 110], [13, -51, 110],  # 0 1 2 3
					[13, -49, 112], [15, -49, 112], [15, -51, 112], [13, -51, 112],  # 4 5 6 7
					[11, -47, 112], [17, -47, 112], [17, -53, 112], [11, -53, 112],  # 8 9 10 11
					[11, -47, 114], [17, -47, 114], [17, -53, 114], [11, -53, 114]],  # 12 13 14 15
				   [[0,1], [1,2], [2,3], [3,0],
					[8,9], [9,10], [10,11], [11,8],
					[0,4], [1,5], [2,6], [3,7],
					[4,5], [5,6], [6,7], [7,4],
					[8,12], [9,13], [10,14], [11,15],
					[12,13], [13,14], [14,15], [15,12]],
				   [[12,13,14,15], [8,9,10,11], [12,8,9,13], [9,13,14,10], [10,14,15,11], [11,15,8,9], [0,4,5,1], [1,5,6,2], [2,6,7,3], [3,7,4,0]],
				   color='gold')
temp = object_buffer
def run():
	global camera
	try:
		decrease = 0.1
		if not camera.moving:
			if camera.xspeed >= 1:
				camera.xspeed -= decrease
			if camera.yspeed >= 1:
				camera.yspeed -= decrease
			if camera.zspeed >= 1:
				camera.zspeed -= decrease
			if camera.xrot >= 1:
				camera.xrot -= decrease
			if camera.yrot >= 1:
				camera.yrot -= decrease
			if camera.zrot >= 1:
				camera.zrot -= decrease
		for obj in temp:
			canvas.delete(obj)
			object_buffer.remove(obj)
		for obj in objects:
			obj.update()
#		root.update_idletasks()
		root.update()
#		canvas.update_idletasks()
		canvas.update()
		root.after(0, run)
	except TclError:
		print('Application closed by user, or an unknown error occurred.')
		exit()
root.after(0, run)
root.mainloop()
