import maya.cmds as cmds
import random

#delete everything from scene
if cmds.ls("*_main"):
    cmds.delete(cmds.ls("*_main"))
    
# exercise 2: animation for planet and moons
def animate_moon(anim_moon_grp=None):

    min_time = cmds.playbackOptions(q=1, minTime=True)
    max_time = cmds.playbackOptions(q=1, maxTime=True)

    anim_moon_cycle = random.randint(1,10)

    cmds.setKeyframe(anim_moon_grp + ".rotateY", inTangentType="linear", time=min_time, value=0)
    cmds.setKeyframe(anim_moon_grp + ".rotateY", outTangentType="linear", time=max_time, value=360*anim_moon_cycle)

def animate_planet(anim_planet_grp=None):
    min_time = cmds.playbackOptions(q=1, minTime=True)
    max_time = cmds.playbackOptions(q=1, maxTime=True)

    anim_planet_cycle = random.randint(1,3)

    cmds.setKeyframe(anim_planet_grp + ".rotateY", inTangentType="linear", time=min_time, value=0)
    cmds.setKeyframe(anim_planet_grp + ".rotateY", outTangentType="linear", time=max_time, value=360*anim_planet_cycle)


#exercise 1 and 3: make planet with random amount of moons + ramdom radiuses                   
def create_moon(moon_name = "moon", radius = 1, offset_distance=0):

    moon_spot = cmds.polySphere(n=moon_name, radius=radius)[0]

    grp_moon = cmds.group(empty=1, name=moon_name + "_moon")
    grp_planet_orbit = cmds.group(empty=1, name=moon_name + "_planet_orbit")
    cmds.parent(grp_planet_orbit,grp_moon)
    grp_rotation = cmds.group(empty=1, name=moon_name + "_rotation")
    cmds.parent(grp_rotation,grp_planet_orbit)
    grp_rotation_offset = cmds.group(empty=1, name=moon_name + "_rotation_offset")
    cmds.parent(grp_rotation_offset,grp_rotation)
    grp_moon_spot = cmds.group(empty=1, name=moon_name + "_position")
    cmds.parent(grp_moon_spot,grp_rotation_offset)

    cmds.parent(moon_spot,grp_moon_spot)

    moon_spot_full_path=cmds.ls(moon_spot,l=1)[0]

    rotationZ = random.uniform(-45,45)
    cmds.xform(grp_planet_orbit,ro=[0,0,rotationZ])

    rotationY = random.uniform(0,360)
    cmds.xform(grp_rotation_offset, ro=[0,rotationY,0])

    cmds.xform(grp_moon_spot,t=[offset_distance,0,0])

    animate_moon(anim_moon_grp=grp_rotation)
    return grp_moon

def create_planet(planet_name="Earth", planet_r_min = 3, planet_r_max = 6, moon_min = 2, moon_max = 7, moon_r_min = 0.4, moon_r_max = 2.0):

    moon_count = random.randint(moon_min,moon_max)

    planet_r = random.uniform(planet_r_min,planet_r_max)
    planet_spot = cmds.polySphere(n=planet_name, r=planet_r)[0]

    grp_main = cmds.group(empty=1, name=planet_name + "_main")
    grp_planet_spot = cmds.group(empty=1, name=planet_name + "_spot")
    cmds.parent(grp_planet_spot,grp_main)

    cmds.parent(planet_spot,grp_planet_spot)

    planet_spot_full_path=cmds.ls(planet_spot,l=1)[0]

# exercise 4: add color to planet and moons
    color_r = random.uniform(0,1)
    color_g = random.uniform(0,1)
    color_b = random.uniform(0,1)

    shader_planet = cmds.shadingNode("lambert", n="lambert_planet", asShader=1)
    cmds.setAttr(shader_planet + ".color", color_r, color_g, color_b, type="double3")
    cmds.select(planet_spot_full_path)
    cmds.hyperShade(assign = shader_planet)

    distance_to_moon = planet_r

    for i in range(moon_count): 
        moon_r = random.uniform(moon_r_min, moon_r_max)
        moon_offset = distance_to_moon + moon_r + 1

        distance_to_moon = moon_offset + moon_r
        moon = create_moon(moon_name="{}_{}".format(planet_name, i), radius=moon_r, offset_distance=moon_offset)

        shader_moon = cmds.shadingNode("lambert", n = "lambert_moon", asShader=1)
        cmds.setAttr(shader_moon + ".color", (color_r+ i*0.005), (color_g + i*0.05), color_b, type="double3")
        cmds.select(moon)
        cmds.hyperShade(assign = shader_moon)

        cmds.parent(moon, grp_main)
    
    animate_planet(anim_planet_grp=planet_spot)

create_planet(planet_name="Earth", planet_r_min = 3, planet_r_max = 6, moon_min = 2, moon_max = 7, moon_r_min = 0.4, moon_r_max = 2.0)
