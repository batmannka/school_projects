import maya.cmds as cmds
import json

#find,list and save to file value of all selected rig's curves
def open_saved_file(path_to_file = None):

    json_data = {}

    with open(path_to_file, 'r') as f:

        json_data = json.load(f)
        
    for crv in json_data:

        for atr in json_data[crv]:

            value= json_data[crv][atr]

            cmds.setAttr(crv+'.'+ atr, value, l = 0)

def repeat_pose():

    path_to_open_file = "D:\DEV\week_3\pose.json"
    open_saved_file(path_to_file = path_to_open_file)

repeat_pose()
