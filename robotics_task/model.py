import bge
import serial
import time

port='COM5'
baud=9600
now='h'
ser = serial.Serial(port, baud, timeout=1)

cont = bge.logic.getCurrentController()
rover = cont.owner
scene = bge.logic.getCurrentScene()
motion=0
toggle=1

"""temp"""
#sensors
click = cont.sensors["drop"]
up = cont.sensors["up"]
turn = cont.sensors["turn"]

#actuators
turning_right = cont.actuators["turning_right"]
turning_left = cont.actuators["turning_left"]

def drop_location(object, direction, location, drop_object):
    if drop_object=='rock':
        if direction==0:
            object.worldPosition= [location[0]+2.0,location[1],location[2]]
        elif direction==1:
            object.worldPosition= [location[0],location[1]-2.0,location[2]]
        elif direction==2:
            object.worldPosition= [location[0]-2.0,location[1],location[2]]           
        elif direction==3:
            object.worldPosition= [location[0],location[1]+2.0,location[2]]
        
    elif drop_object=='shape':
        if direction==0:
            object.worldPosition= [location[0],location[1]-3.0,location[2]]
        elif direction==1:
            object.wrldPosition= [location[0]-3.0,location[1],location[2]]
        elif direction==2:
            object.worldPosition= [location[0],location[1]+3.0,location[2]]
        elif direction==3:
            object.worldPosition= [location[0]+3.0,location[1],location[2]]

def drop_rock(type, direction):
    location=rover.worldPosition[0:]
    if type=='e':
        object = scene.addObject("adirondack",rover)
        drop_location(object, direction, location,'rock')
        
    elif type=='f':
       object = scene.addObject("rocknest3",rover)
       drop_location(object, direction, location, 'rock')

    elif type=='g':
        object = scene.addObject("heatshield",rover)
        drop_location(object, direction, location, 'rock')


def drop_shape(type, direction):
    location=rover.worldPosition[0:]
    if type=='h':
        object = scene.addObject("curve",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='i':
        object = scene.addObject("slope",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='j':
        object = scene.addObject("slopeDOWN",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='k':
        object = scene.addObject("slopeLEFT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='l':
        object = scene.addObject("slopeRIGHT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='m':
        object = scene.addObject("slopeUP",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='n':
        object = scene.addObject("BUMP",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='o':
        object = scene.addObject("BUMPDOWN",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='p':
        object = scene.addObject("BUMPLEFT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='q':
        object = scene.addObject("BUMPRIGHT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='x':
        object = scene.addObject("BUMPUP",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='s':
        object = scene.addObject("tunnel",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='t':
        object = scene.addObject("tunnelDOWN",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='u':
        object = scene.addObject("tunnelLEFT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='v':
        object = scene.addObject("tunnelRIGHT",rover)
        drop_location(object, direction, location, 'shape')
    elif type=='w':
        object = scene.addObject("tunnelUP",rover)
        drop_location(object, direction, location, 'shape')
        #object.worldPosition= [location[0],location[1]-3.0,location[2]]
    


def action():
    """
    if click.positive:
        drop_shape('s',rover["motion"])
        #drop_rock('s',rover["motion"])
    elif up.positive:
        rover.applyMovement((0.0,0.028,0.0),True)
    elif turn.positive:
        #rover.applyRotation((0.02,0.0,0.0),True)
        cont.activate(turning)
        rover["motion"] += 1
        if motion == 4:
            rover["motion"] = 0
    cont.deactivate(turning)
    """
    cont.deactivate(turning_left)
    cont.deactivate(turning_right)
    a=' '
    if a==' ':
        while(ser.inWaiting()>0):
            a=str(ser.read(1).decode('ascii'))
    #print(a)
    if a=='a':
        rover.applyMovement((0.0,0.0485,0.0),True)
        object = scene.addObject("PLANE",rover)
        location = rover.worldPosition[0:]
        object.worldPosition= [location[0] ,location[1],location[2]]
        rover.setLinearVelocity([0.0,1.75,0.0], True)
    elif a=='r':
        cont.activate(turning_right)
        rover["motion"] += 1
        if rover["motion"] == 4:
            rover["motion"] = 0
    elif a=='b':
        cont.activate(turning_left)
        rover["motion"]-=1
        if rover["motion"] == 0:
            rover["motion"] = 4
    elif a=='r':
        cont.activate(turning_left)
        rover["motion"] += 1
        if rover["motion"] == 4:
            rover["motion"] = 0    
    elif a=='c':
        rover.applyRotation((0.0,0.0,0.02),False)
        
    elif a=='d':
        rover.applyRotation((0.0,0.0,-(0.02)),True)
        
    if a in ['e','f','g']:
        drop_rock(a,rover["motion"])
    if a in ['h','i','j','k','l','m','n','o','p','q','x','s','t','u','w']:
        drop_shape(a,rover["motion"])
    if a=='z':
        object = scene.addObject("PLANE1",rover)
        location = rover.worldPosition[0:]
        if motion == 0:
            object.worldPosition= [location[0]+1.0 ,location[1],location[2]]
        elif motion == 1:
            object.worldPosition= [location[0],location[1]-1.0,location[2]]
        elif motion == 2:
            object.worldPosition= [location[0]-1.0 ,location[1],location[2]]
        elif motion == 3:
            object.worldPosition= [location[0],location[1]-1.0,location[2]]    
    
   
    
