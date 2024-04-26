import maya.cmds as cmds

selection = cmds.ls(selection=1)

for sel in selection:

    oName = sel.split("|") [-1]

    oPos = cmds.xform(sel, q=1, worldSpace=1, translation=1)

    offset_curve = "{}_cn_offset".format(oName)
    master_curve = "{}_cn_master".format(oName)

    p1 = (oPos[0]-2,oPos[1], oPos[2]+3)
    p2 = (oPos[0]+3,oPos[1], oPos[2])
    p3 = (oPos[0]-2,oPos[1], oPos[2]-3)
    p4 = (oPos[0]-2,oPos[1], oPos[2]+3)

    cmds.curve(n=offset_curve, d=1, p=[p1,p2,p3,p4], k=[0,1,2,3,])
    cmds.xform(offset_curve, cpc=1)

    cmds.duplicate(offset_curve, name=master_curve)
    cmds.xform(master_curve, r=1,s=[1.4,1.4,1.4])

    constr = cmds.parentConstraint(offset_curve, sel, mo=1, weight=1, n="{}_parentConstraint".format(oName))

    grp_rig = cmds.group(em=1, n="{}_rig".format(oName))
    grp_geo = cmds.group(em=1, n="{}_geo".format(oName))
    grp_control = cmds.group(em=1, n="{}_control".format(oName))
    grp_extras = cmds.group(em=1, n="{}_extras".format(oName))

    cmds.parent(grp_geo, grp_rig)
    cmds.parent(grp_control, grp_rig)
    cmds.parent(master_curve, grp_control)
    cmds.parent(offset_curve, master_curve)
    cmds.parent(sel, grp_geo)
    cmds.parent(grp_extras, grp_rig)
    cmds.parent(constr, grp_extras)
