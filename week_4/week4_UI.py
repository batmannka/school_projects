import maya.cmds as cmds
import random

#prepare scene for open new window
def clean_scene():
    
    if cmds.window("primitives_creator", exists=True):
        cmds.deleteUI("primitives_creator")

    if cmds.windowPref("primitives_creator", exists=True):
        cmds.windowPref("primitives_creator", remove=True)


#make general view of the window
def open_window():
    cmds.window("primitives_creator", title="My primitives creator", width=300)

    #place for writing name
    main_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

    text_layout = cmds.columnLayout(adjustableColumn=True, parent=main_layout, columnAlign="left",
                                    columnOffset=["both", 10], rowSpacing=5,
                                    statusBarMessage="Write a primitive name")

    cmds.text("Object Name:", parent=text_layout)
    cmds.textField("new_name", parent=text_layout)

    #make buttons for creating primitives
    prim_b_layout = cmds.rowLayout(parent=main_layout, numberOfColumns=3, columnAttach3=["both", "both", "both"],
                                   columnOffset3=[24, 24, 24])

    cmds.radioCollection()
    cmds.radioButton("sphere_b", parent=prim_b_layout, label="Sphere")
    cmds.radioButton("cube_b", parent=prim_b_layout, label="Cube")
    cmds.radioButton("cone_b", parent=prim_b_layout, label="Cone")

    #option checkboxes
    options_layout = cmds.columnLayout(parent=main_layout, adjustableColumn=True, columnAlign="left",
                                       columnOffset=["both", 10], rowSpacing=10)

    cmds.checkBox("put_grp", label="Put into a group", parent=options_layout)
    cmds.checkBox("move_obj", label="Move", parent=options_layout)
    cmds.checkBox("display_obj", label="Display option", parent=options_layout)

    #create and cancel buttons
    main_b_layout = cmds.rowLayout(parent=main_layout, numberOfColumns=2, columnAttach2=["both", "both"],
                                   columnOffset2=[11, 0], width=300, height=50)

    cmds.button(label="Create", parent=main_b_layout, width=135, height=20,
                command=create_obj)
    cmds.button(label="Cancel", parent=main_b_layout, width=135, height=20,
                command=("cmds.deleteUI('primitives_creator')"))

    cmds.showWindow("primitives_creator")


#creating an object with options
def create_obj(args):
    new_name = cmds.textField("new_name", query=True, text=True)
    prim = None
    if cmds.radioButton("sphere_b", query=True, select=True):
        prim = cmds.polySphere(name=new_name + "_sphere")[0]
    elif cmds.radioButton("cube_b", query=True, select=True):
        prim = cmds.polyCube(name=new_name + "_cube")[0]
    elif cmds.radioButton("cone_b", query=True, select=True):
        prim = cmds.polyCone(name=new_name + "_cone")[0]

    if cmds.checkBox("display_obj", query=True, value=True):
        cmds.setAttr(prim + ".template", True)

    grp = None
    if cmds.checkBox("put_grp", query=True, value=True):
        grp = cmds.group(name=prim + "_grp")

    r_move_x = random.uniform(-20, 20)
    r_move_y = random.uniform(-20, 20)
    r_move_z = random.uniform(-20, 20)
    if cmds.checkBox("move_obj", query=True, value=True):
        if cmds.checkBox("put_grp", query=True, value=True):
            cmds.xform(grp, translation=[r_move_x, r_move_y, r_move_z])
        else:
            cmds.xform(prim, translation=[r_move_x, r_move_y, r_move_z])


clean_scene()
open_window()
