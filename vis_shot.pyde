# -*- coding : utf-8 -*-
import random


SHOT_R = 24

def get_center():
    return (width/2, height/2)

def put_shot(coords):
    center = {width/2, height/2}

    shot_count = len(coords)
    
    for coord in coords:
        r = random.randint(150, 256)
        g = random.randint(150, 256)
        b = random.randint(150, 256)
        fill(r, g, b, 240)
        x = coord[0]*5.55
        y = coord[1]*5.55
        ellipse(int(width/2+x), int(height/2+y), SHOT_R, SHOT_R)
    
def line_shots(coords):
    cx = width/2
    cy = height/2
    
    CON = 5.55
    beginShape(TRIANGLE_STRIP)
    for coord in coords:
        r = random.randint(50, 256)
        g = random.randint(50, 256)
        b = random.randint(50, 256)
        fill(r, g, b, 150)
        vertex(cx+coord[0]*CON, cy+coord[1]*CON)
    endShape()
        
size(876, 880)
smooth()
stroke(210,210,210)
strokeWeight(2)
strokeCap(ROUND)
strokeJoin(ROUND)
img = loadImage('sb-target.png')
background('#FFF9E5')
#background('#A5ECFF')

    
shots = []
with open('ai-nagatoro-20190811-S.csv', 'r') as f:
    header = f.readline()
    shots = f.readlines()

coords = []
for shot in shots:
    coords.append(shot.rstrip('\n').split(','))
    
coords = [[float(coord[8]), float(coord[9])] for coord in coords]

print(coords)

image(img,0,0)
put_shot(coords)
#line_shots(coords)
print(len(coords))    
