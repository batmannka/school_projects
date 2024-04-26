import maya.cmds as cmds

def blendToNeighbours(move = 20):

    sel_channelName = cmds.keyframe(query=1, name=1)[0]  
    sel_time = cmds.keyframe(query=1, timeChange=1)[0] 
    sel_value = cmds.keyframe(query=1, valueChange=1)[0] 

    prevFrame = cmds.findKeyframe(which = "previous", time = (sel_time,sel_time))
    nextFrame = cmds.findKeyframe(which = "next", time = (sel_time,sel_time))

    cmds.selectKey(clear=1)
    prevValue = cmds.keyframe(sel_channelName, query=1, time=(prevFrame,prevFrame), valueChange=1)[0]
    nextValue = cmds.keyframe(sel_channelName, query=1, time=(nextFrame,nextFrame), valueChange=1)[0]
    cmds.selectKey(sel_channelName, time=(sel_time,sel_time))

    nStep = (nextValue - sel_value)/100
    pStep = (sel_value - prevValue)/100

    if move > 0: 
        newValue = sel_value + move * nStep
    elif move < 0: 
        newValue = sel_value + move * pStep

    cmds.keyframe(valueChange = newValue)

blendToNeighbours(move = 75)