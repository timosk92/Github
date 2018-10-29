'''
https://www.youtube.com/watch?v=bF-PFPacs88
'''


import pymel.core as pm
scriptName = __name__
newWindow = 'Auto_armRig_maker'


def gui():
    if(pm.window(newWindow, q=True,exists=True)):
        pm.deleteUI(newWindow)

    if(pm.windowPref(newWindow, q=True, exists=True)):
        pm.windowPref(newWindow,r=True)

    myWindow = pm.window(newWindow, t='Auto Arm Rig', w=150,h=325)
    main_layout=pm.columnLayout('Main Header')

    #Naming
    pm.text('naiming_Text', l="Step 1: Set name options")
    pm.rowColumnLayout(nc=4, cw=[(1,20),(2,40),(3,40),(4,50)])
    pm.text('ori_txt', label='Ori:')
    pm.optionMenu('Ori_Menu')
    pm.menuItem(label='lf_')
    pm.menuItem(label='rt_')
    pm.menuItem(label='ct_')
    pm.text('label_txt', label='Label::')
    pm.optionMenu('Label_Menu')
    pm.menuItem(label='Leg')
    pm.menuItem(label='Arm')
    pm.setParent(main_layout)

    #Rig type
    pm.text('rigType_text',
    labelArray3=('IK','FK','IKFK'),numberOfRadioButtons=3,columnWidth=[50,50],select=3)
    #Icon options


    #Icon Colour



    #pick Colour


    #Pole Vector

    pm.showWindow()
