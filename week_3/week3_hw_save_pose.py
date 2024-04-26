import maya.cmds as cmds
import json

#find all nurbs curves from rig without information of shape
def find_rig_curve(): 

    rig = cmds.ls(sl=1, l=1) [0]

    full_rig = cmds.listRelatives(rig, c=1, f=1, ad=1, type = 'nurbsCurve')

    full_rig_without_shape = cmds.listRelatives(full_rig, p=1, f=1)

    return full_rig_without_shape

#find,list and save to file value of all selected rig's curves
def save_value(path_to_file = None):

    curves = find_rig_curve()   

    curves_value = {}

    for crv in curves:
            
        use_channels = cmds.listAttr(crv, k=1, connectable=False, locked=False)

        dict_channels = {}

        if use_channels:
                
            for at in use_channels:

                if 'translate' in at or 'rotate' in at or 'scale' in at:

                    value = cmds.getAttr(crv +'.'+ at)
                    dict_channels[at] = value

            curves_value[crv] = dict_channels

    if curves_value:

        with open(path_to_file, 'w') as f:
            json.dump(curves_value, f, indent = 4)
        

def save_pose():

    path_to_save_file = "D:\DEV\week_3\pose.json"
    save_value(path_to_file = path_to_save_file)

save_pose()