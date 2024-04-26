import maya.cmds as cmds

sph = cmds.polySphere(r=1, name="MySphere")[0]

minTime = cmds.playbackOptions(query=1, minTime=True)
maxTime = cmds.playbackOptions(query=1, maxTime=True)

cmds.setKeyframe(sph + ".translateX", time=minTime, value=-10)
cmds.setKeyframe(sph + ".translateX", time=maxTime, value=10)