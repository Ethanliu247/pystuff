#!/usr/bin/python3
from math import sin, cos, radians, degrees
from tkinter import *
from time import sleep
from sys import exit
from random import randint, choice

root = Tk()
root.title("3D Engine")
height = 500
width = 500
root.geometry(str(height+100)+'x'+str(width)+'+0+0')
root.focus()

canvas = Canvas(root, width=width, height=height, bg='white')
info = Label(root, text='House Simulator 2016', fg='blue')
info.pack()
canvas.pack()
object_buffer = []
objects = []
global_points = []
global_lines = []
global_faces = []
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
        self.origin = self.x, self.y, self.z
        self.ux, self.uy, self.uz = self.x, self.y, self.z
    def movex(self, mod):
        if self.xspeed <= self.scap:
            self.xspeed += 1
        self.x += self.xspeed*mod
        self.update_u()
        self.persp_rot()
        self.update_u2()
    def movey(self, mod):
        if self.yspeed <= self.scap:
            self.yspeed += 1
        self.y += self.yspeed*mod
        self.update_u()
        self.persp_rot()
        self.update_u2()
    def movez(self, mod):
        if self.zspeed <= self.scap:
            self.zspeed += 1
        self.z += self.zspeed*mod
        self.update_u()
        self.persp_rot()
        self.update_u2()
    def rotx(self, mod):
        if self.xrot <= self.rcap:
            self.xrot += 1
        self.thetaX += self.xrot*mod
    def roty(self, mod):
        self.origin = self.ux, self.uy, self.uz
        self.x, self.y, self.z = self.ux, self.uy, self.uz
        self.persp_rot()
        self.update_u2()
        if self.yrot <= self.rcap:
            self.yrot += 1
        self.thetaY += self.yrot*mod
        self.persp_rot()
    def rotz(self, mod):
        if self.zrot <= self.rcap:
            self.zrot += 1
        self.thetaZ += self.zrot*mod
    def update_u(self):
        self.ux, self.uy, self.uz = self.x, self.y, self.z
    def update_u2(self):
        self.ux = self.ux
        self.uy = self.uy
        self.uz = self.uz
    def persp_rot(self):
        self.ux, self.uy, self.uz = rotate([self.x, self.y, self.z], self.thetaY, 'y', origin=self.origin)

def rotate(xyz, theta, axis, origin=(0,0,0)):
    theta = radians(theta)
    x, y, z = xyz
    nx, ny, nz = x, y, z
    c = cos(theta)
    s = sin(theta)
    x -= origin[0]
    y -= origin[1]
    z -= origin[2]
    if axis == 'x':
        ny = c*y - s*z
        nz = s*y + c*z
        ny += origin[1]
        nz += origin[2]
    elif axis == 'y':
        nx = c*x - s*z
        nz = s*x + c*z
        nx += origin[0]
        nz += origin[2]
    elif axis == 'z':
        nx = c*x - s*y
        ny = s*x + c*y
        nx += origin[0]
        ny += origin[1]
    else:
        return 1
    return round(nx, 2), round(ny, 2), round(nz, 2)

def map_rotation(xyz, cam):
    x, y, z = xyz
    x += cam.ux
    y -= cam.uy
    z -= cam.uz
    x, y, z = rotate((x, y, z), cam.thetaX, 'x')
    x, y, z = rotate((x, y, z), cam.thetaY, 'y')
    x, y, z = rotate((x, y, z), cam.thetaZ, 'z')
    return x, y, z

def map_2d(mapped_xyz, scale=1):
    x, y, z = mapped_xyz
    if z >= 0: #clipping
        try:
            nx = ((width / 2) * x / z) * scale
            ny = ((height / 2) * y / z) * scale
        except ZeroDivisionError:
            nx = x
            ny = y
        if nx > width/2:
            newx = 0
        elif nx < width/2:
            newx = width
        else:
            newx = x
        if ny > height/2:
            newy = 0
        elif ny < height/2:
            newy = height
        else:
            newy = y
        return newx, newy
    newx = ((width / 2) * x / z) * scale
    newy = ((height / 2) * y / z) * scale
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

camera = Camera(0, -25, 400, 0, 0, 0)  # x is >, y is ^, and z is behind you
def old_controls():
    # Move
    root.bind('<KeyPress-w>', lambda e: camera.movez(-1))
    root.bind('<KeyPress-a>', lambda e: camera.movex(1))
    root.bind('<KeyPress-s>', lambda e: camera.movez(1))
    root.bind('<KeyPress-d>', lambda e: camera.movex(-1))
    root.bind('<KeyPress-q>', lambda e: camera.movey(-1))
    root.bind('<KeyPress-e>', lambda e: camera.movey(1))
    # Rotate
    root.bind('<KeyPress-i>', lambda e: camera.rotx(-1))
    root.bind('<KeyPress-j>', lambda e: camera.rotz(1))
    root.bind('<KeyPress-k>', lambda e: camera.rotx(1))
    root.bind('<KeyPress-l>', lambda e: camera.rotz(-1))
    root.bind('<KeyPress-u>', lambda e: camera.roty(-1))
    root.bind('<KeyPress-o>', lambda e: camera.roty(1))
def new_controls():
    root.bind('<KeyPress-w>', lambda e: camera.movez(-1))
    root.bind('<KeyPress-a>', lambda e: camera.movex(-1))
    root.bind('<KeyPress-s>', lambda e: camera.movez(1))
    root.bind('<KeyPress-d>', lambda e: camera.movex(1))
    root.bind('<KeyPress-q>', lambda e: camera.roty(-1))
    root.bind('<KeyPress-e>', lambda e: camera.roty(1))
new_controls()

floor = canvas.create_rectangle(0, height/2, 500, height, fill='forest green')
canvas.pack()

decrease = 0.1
def mainloop():
    global camera
    try:
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
        for obj in temp:
            canvas.delete(obj)
            object_buffer.remove(obj)
        for obj in objects:
            obj.update()
#        root.update_idletasks()
        root.update()
#        canvas.update_idletasks()
        canvas.update()
        root.after(0, mainloop)
    except TclError:
        print('Application closed by user, or an unknown error occurred.')
        exit()
root.after(0, mainloop)
root.mainloop()
