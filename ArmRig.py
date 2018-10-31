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
    pm.text('rigType_text', label ="step 2: Set rig type")
    pm.radioButtonGrp("armType_Btn", labelArray3=('IK','FK','IKFK'),numberOfRadioButtons=3,columnWidth3=[50,50,50],select=3)
    pm.separator('rig_Sep', w=150, h=5)
    #Icon options

    pm.text('conSet_Text',l='Step 3: Set Icon properties')
    pm.rowColumnLayout(nc=2,cw=([1,90],[2,60]))
    pm.text('ikStyleText', label='IK Icon Style:')
    pm.optionMenu('ikIcon_Menu')
    pm.menuItem(label = 'Box')
    pm.menuItem(label = '4 Arrows')
    pm.menuItem(label = '4 Pin')
    pm.text('fkStyle_Text', label ='FK Icon Style:')
    pm.optionMenu('fkIcon_Menu')
    pm.menuItem(label='Circle')
    pm.menuItem('Turn Arrows')
    pm.text('handStyle_Text', label ='FK Icon Style:')
    pm.menuItem(label="Circle")
    pm.menuItem('COG')
    pm.text('pvStyle_Text', label ='FK Icon Style:')
    pm.optionMenu('pvIcon_menu')
    pm.menuItem(label='Diamond')
    pm.menuItem(label='Arrow')
    pm.setParent(main_layout)
    pm.button('testIconButton', l='Make test icon to set scale', w=150)
    pm.separator('style_Sep', w=150, h=5)

    #Icon Colour
    pm.text('armColour_Text', l="Step 4: Pick icon colour")
    pm.gridLayout(nr=1,nc=5, cellWidthHeight = [30,20])
    pm.iconTextButton('darkBlue_button', bgc=[0.000,0.016,0.373])
    pm.iconTextButton('lightBlue_button', bgc=[0,0,1])
    pm.iconTextButton('brown_button', bgc=[0.537,0.278,0.2])
    pm.iconTextButton('red_button', bgc=[1,0,0])
    pm.iconTextButton('yellow_button', bgc=[1,1,0])
    pm.setParent(main_layout)
    pm.colorIndexSliderGrp('armColor', w=150, h=20, cw2=(150,0),min=0, max=31, value = 7)
    pm.separator('icon_Sep', w=150, h=5)

    #Pole Vector
    pm.text('PV_text', label='Step 5: Set IK elbow options')
    pm.radioButtonGrp('addPVElbow_btn', labelArray2 = ('twist','Pole Vector'),numberOfRadioButtons = 2, columnWidth2=[65,85], select =2)
    pm.separator('pole_Sep', w=150, h=5)
    pm.button('final_Button', l='Finalise the arm', w=150)


    pm.showWindow()
