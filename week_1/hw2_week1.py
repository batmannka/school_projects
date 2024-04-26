import maya.cmds as cmds
#1
sph = cmds.polySphere(r=1, name="MySphere")[0]

min_time = cmds.playbackOptions(query=1, minTime=True)
max_time = cmds.playbackOptions(query=1, maxTime=True)

cmds.setKeyframe(sph + ".translateX", time=min_time, value=-10)
cmds.setKeyframe(sph + ".translateX", time=max_time, value=10) 

#2
cube = cmds.polyCube(name="MyCube")[0]
cmds.xform(cube, worldSpace=1, translation = [-10,0,10])

MyConstrain = cmds.parentConstraint(sph, cube, maintainOffset=1, n="MyConstrain")

cmds.bakeResults(cube +'.translateX', t=(min_time,max_time))

cmds.delete(MyConstrain)