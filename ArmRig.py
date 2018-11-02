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
    pm.optionMenu('Ori_Menu', cc = scriptName + '.colorChange()')
    pm.menuItem(label='lf_')
    pm.menuItem(label='rt_')
    pm.menuItem(label='ct_')
    pm.text('label_txt', label='Label:')
    pm.optionMenu('Label_Menu')
    pm.menuItem(label='Leg')
    pm.menuItem(label='Arm')
    pm.setParent(main_layout)

    #Rig type
    pm.text('rigType_text', label ="step 2: Set rig type")
    pm.radioButtonGrp("armType_Btn", labelArray3=('IK','FK','IKFK'),numberOfRadioButtons=3,columnWidth3=[50,50,50],select=3, cc=scriptName +'.armTypeVis()')
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
    pm.text('handStyle_Text', label ='Hand Icon Style:')
    pm.optionMenu('handIcon_menu')
    pm.menuItem(label="Circle")
    pm.menuItem('COG')
    pm.text('pvStyle_Text', label ='PV Icon Style:')
    pm.optionMenu('pvIcon_menu')
    pm.menuItem(label='Diamond')
    pm.menuItem(label='Arrow')
    pm.setParent(main_layout)
    pm.button('testIconButton', l='Make test icon to set scale', w=150, c=scriptName + '.armIconScale()')
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



def colorChange():
    ori_Opt = pm.optionMenu('Ori_Menu',q=True,sl=True)
    if ori_Opt == 1:
        ori_color = 7
    if ori_Opt == 2:
        ori_color = 14
    if ori_Opt == 3:
        ori_color = 18
    pm.colorIndexSliderGrp('armColor', e=True, value=ori_color)

def armTypeVis():
    armType=pm.radioButtonGrp("armType_Btn",q=True, sl=True)
    if armType == 1:
        ik_val = 1
        fk_val = 0
        ikfk_val = 0
    if armType == 2:
        ik_val = 0
        fk_val = 1
        ikfk_val = 0
    if armType == 3:
        ik_val = 1
        fk_val = 1
        ikfk_val = 1

    pm.text('ikStyleText', e=True, vis=ik_val)
    pm.optionMenu('ikIcon_Menu',e=True, vis=ik_val)
    pm.text('fkStyle_Text', e=True, vis=fk_val)
    pm.optionMenu('fkIcon_Menu',e=True, vis=fk_val)
    pm.optionMenu('handIcon_menu',e=True, vis=ikfk_val)
    pm.text('handStyle_Text',e=True,vis=ikfk_val)
    pm.text('pvStyle_Text',e=True, vis=ikfk_val)
    pm.optionMenu('pvIcon_menu',e=True,vis=ikfk_val)
    pm.text('PV_text',e=True,vis=ik_val)
    pm.radioButtonGrp('addPVElbow_btn',e=True,vis=ik_val)


def armIconScale():
    #variables
    armType = pm.radioButtonGrp('armType_Btn', q=True,sl=True)
    ikShape = pm.optionMenu('ikIcon_Menu',q=True, sl=True)
    fkShape = pm.optionMenu('fkIcon_Menu',q=True, sl=True)
    pvShape = pm.optionMenu('pvIcon_menu',q=True, sl=True)
    handShape = pm.optionMenu('handIcon_menu',q=True, sl=True)
    pvType = pm.radioButtonGrp('addPVElbow_btn', q=True , sl=True)
    selected = pm.ls(sl=True, dag=True, type='joint')

    transform_list=[]
    icon_test_list=[]

    #create IK icon
    #cube
    ik_box = pm.curve(n='ik_arm_box_curve', d=1, p=([1,1,1],[1,1,1],[1,-1,1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,-1],[-1,-1,1],[-1,1,1],[1,1,1],[1,-1,1],[-1,-1,1],[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1]))
    ik_box_list = pm.ls(ik_box, dag=True)
    #4 Arrows

    ik_arrows = pm.curve(n='ik_arm_4Arrows',d=1,p=([1,0,1],[1,0,1.5],[1,0,2],[1,0,2.5],[1,0,3],[2,0,0]))
    ik_arrows_list = pm.ls(ik_arrows, dag=True)
    pm.setAttr(ik_arrows_list[0] + '.rotateZ', -90)
    pm.scale(ik_arrows_list[0], 0.2, 0.2, 0.2)
    pm.makeIdentity(ik_arrows_list[0],apply=True , t=1, r=1 ,s=1,n=0, pn=1)

    ik_4pin = pm.curve(n='ik_arm_4Pin',d=1,p=([-1.2,0,0],[-1.276,0.235114,0],[-1.476393,0.380432,0]))
    ik_4pin_list = pm.ls(ik_arrows, dag=True)
    pm.setAttr(ik_arrows_list[0] + '.rotateZ', -90)
    pm.scale(ik_arrows_list[0], 0.2, 0.2, 0.2)
    pm.makeIdentity(ik_arrows_list[0],apply=True , t=1, r=1 ,s=1,n=0, pn=1)

    #empty group
    ik_ctrl = pm.group(empty=True , n ='ARM_IK_SCALE_TEST_DONT_DELETE')
    pm.parent(ik_box_list[1],ik_arrows_list[1],ik_4pin_list[1],ik_ctrl, r=True, s=True)
    transform_list.append(ik_box_list[0])
    transform_list.append(ik_arrows_list[0])
    transform_list.append(ik_4pin_list[0])

    #setting visibilty
    if ikShape == 1:
        pm.setAttr(ik_arrows + 'Shape.v',0)
        pm.setAttr(ik_4pin + 'Shape.v', 0)
    if ikShape == 1:
        pm.setAttr(ik_arrows + 'Shape.v',0)
        pm.setAttr(ik_4pin + 'Shape.v', 0)
    if ikShape == 1:
        pm.setAttr(ik_arrows + 'Shape.v',0)
        pm.setAttr(ik_4pin + 'Shape.v', 0)

    #position the control
    tempCONST = pm.parentConstraint(selected[1],ik_ctrl, mo=False)
    pm.delete(tempCONST)
    tempCONST = pm.parentConstraint(selected[-1],ik_ctrl, mo=False)
    pm.delete(tempCONST)
    pm,parentConstraint(selected[-1],ik_ctrl, mo=True)
    icon_test_list.append(ik_ctrl)




    #crate the icon
    #cirlce
