import maya.cmds as cmds
import random

def create_moon(moon_name = "moon", radius = 1, offset_distance=0):

    moon_spot = cmds.polySphere(n=moon_name, radius = radius)[0]

    grp_moon = cmds.group(empty = 1, name = moon_name + "_moon")
    grp_planet_orbit = cmds.group(empty = 1, name = moon_name + "_planet_orbit")
    cmds.parent(grp_planet_orbit,grp_moon)
    grp_rotation = cmds.group(empty = 1, name = moon_name + "_rotation")
    cmds.parent(grp_rotation,grp_planet_orbit)
    grp_rotation_offset = cmds.group(empty = 1, name = moon_name + "_rotation_offset")
    cmds.parent(grp_rotation_offset,grp_rotation)
    grp_moon_spot = cmds.group(empty = 1, name = moon_name + "_position")
    cmds.parent(grp_moon_spot,grp_rotation_offset)

    cmds.parent(moon_spot,grp_moon_spot)

    moon_spot_full_path=cmds.ls(moon_spot,l=1)[0]

    rotationZ = random.uniform(-45,45)
    cmds.xform(grp_planet_orbit,ro=[0,0,rotationZ])

    rotationY = random.uniform(0,360)
    cmds.xform(grp_rotation_offset, ro=[0,rotationY,0])

    cmds.xform(grp_moon_spot,t=[offset_distance,0,0])


    return grp_moon

def create_planet(planet_name="Earth", moons = 9):

    planet_r = random.uniform(1,6)
    planet_spot = cmds.polySphere(n = planet_name, r = planet_r)[0]

    grp_main = cmds.group(empty=1, name = planet_name + "_main")
    grp_planet_spot = cmds.group(empty=1, name = planet_name + "_spot")
    cmds.parent(grp_planet_spot,grp_main)

    cmds.parent(planet_spot,grp_planet_spot)

    planet_spot_full_path=cmds.ls(planet_spot,l=1)[0]

    distance_to_moon = planet_r
    for i in range(moons): 
        moon_r = random.uniform(0.1, 0.6)
        moon_offset = distance_to_moon + moon_r + 1

        distance_to_moon = moon_offset + moon_r
        moon = create_moon(moon_name="{}_{}".format(planet_name, i), radius=moon_r, offset_distance=moon_offset)

        cmds.parent(moon, grp_main)


create_planet()