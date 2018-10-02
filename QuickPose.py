import maya.cmds as cmds

def showAbout():
    cmds.confirmDialog( title='About', message='Values Default to 0,0,0. Save a collection of objects using sets, find them in the outliner.  Select the items in order and then set then use the revert functions. \nQuick Poser, Tim Kelly 2017')


def updateSlot(currentValue):
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
    print 'Slot',currentValue
    return currentValue

def setRotate(*args):
    
       
    objects = cmds.ls(sl=True)
    #increment for each item in the array
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
    
    if int (currentValue) ==1:
        i=0
        for o in objects:
            cmds.setAttr(o + '.rotateX', x_rotate_1[i])
            cmds.setAttr(o + '.rotateY', y_rotate_1[i])
            cmds.setAttr(o + '.rotateZ', z_rotate_1[i])

            print o, x_rotate_1[i], y_rotate_1[i], z_rotate_1[i], "| Object rotations loaded from Slot 1"
            i+=1          
            
    if int (currentValue) == 2:
        i=0
        for o in objects:        
            cmds.setAttr(o + '.rotateX', x_rotate_2[i])
            cmds.setAttr(o + '.rotateY', y_rotate_2[i])
            cmds.setAttr(o + '.rotateZ', z_rotate_2[i])
            
            print o, x_rotate_2[i], y_rotate_2[i], z_rotate_2[i], "| Object rotations loaded from Slot 2"
            i+=1
        
    if int (currentValue) == 3:
        i=0
        for o in objects:
            cmds.setAttr(o + '.rotateX', x_rotate_3[i])
            cmds.setAttr(o + '.rotateY', y_rotate_3[i])
            cmds.setAttr(o + '.rotateZ', z_rotate_3[i])
            
        print o, x_rotate_3[i], y_rotate_3[i], z_rotate_3[i], "| Object rotations loaded from Slot 3"            
        i+=1
  
def getRotate(*args):
    
    #clear the list of data and start again
       
    objects = cmds.ls(sl=True)
    numberObjectsSel = len(objects)
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
    
    if '1' in currentValue:
        del x_rotate_1[:]
        del y_rotate_1[:]
        del z_rotate_1[:] 
    if '2' in currentValue:
        del x_rotate_2[:]
        del y_rotate_2[:]
        del z_rotate_2[:]
    if '3' in currentValue:
        del x_rotate_3[:]
        del y_rotate_3[:]
        del z_rotate_3[:] 
    
    #object selected?
    if numberObjectsSel==0 :
        print 'No objects selected'
    else:
        for o in objects:
            readRotateX=cmds.getAttr(o + '.rotateX')
            readRotateY=cmds.getAttr(o + '.rotateY')
            readRotateZ=cmds.getAttr(o + '.rotateZ')
            
            if '1' in currentValue:
                x_rotate_1.insert(0,readRotateX)
                y_rotate_1.insert(0,readRotateY)
                z_rotate_1.insert(0,readRotateZ)
            if '2' in currentValue:
                x_rotate_2.insert(0,readRotateX)
                y_rotate_2.insert(0,readRotateY)
                z_rotate_2.insert(0,readRotateZ)
            if '3' in currentValue:
                x_rotate_3.insert(0,readRotateX)
                y_rotate_3.insert(0,readRotateY)
                z_rotate_3.insert(0,readRotateZ)
            

        if '1' in currentValue:
            x_rotate_1.reverse()
            y_rotate_1.reverse()
            z_rotate_1.reverse()   
            if numberObjectsSel != 0:
                print objects,"X",x_rotate_1,"Y",y_rotate_1, "Z",z_rotate_1, " | Object translations saved to Slot 1"            
                return objects,x_rotate_1, y_rotate_1, z_rotate_1  
                   
        if '2' in currentValue:
            x_rotate_2.reverse()
            y_rotate_2.reverse()
            z_rotate_2.reverse()   
            if numberObjectsSel != 0:
                print objects,"X",x_rotate_2,"Y",y_rotate_2, "Z",z_rotate_2, " | Object translations saved to Slot 2"            
                return objects,x_rotate_2, y_rotate_2, z_rotate_2                 
            
        if '3' in currentValue:
            x_rotate_3.reverse()
            y_rotate_3.reverse()
            z_rotate_3.reverse()  
            if numberObjectsSel != 0:
                print objects,"X",x_rotate_3,"Y",y_rotate_3, "Z",z_rotate_3, " | Object translations saved to Slot 3"            
                return objects,x_rotate_3, y_rotate_3, z_rotate_3                 
    


def setTrans(*args):
    
       
    objects = cmds.ls(sl=True)
    numberObjectsSel = len(objects)
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
        
    if int (currentValue) ==1:
        i=0
        for o in objects:
            cmds.setAttr(o + '.translateX', x_trans_1[i])
            cmds.setAttr(o + '.translateY', y_trans_1[i])
            cmds.setAttr(o + '.translateZ', z_trans_1[i])
            
            print o, x_trans_1[i], y_trans_1[i], z_trans_1[i], "|Object translations loaded from Slot 1"
            
            i+=1
            
            
    if int (currentValue) ==2:
        i=0
        for o in objects:
            cmds.setAttr(o + '.translateX', x_trans_2[i])
            cmds.setAttr(o + '.translateY', y_trans_2[i])
            cmds.setAttr(o + '.translateZ', z_trans_2[i])
            
            print o, x_trans_2[i], y_trans_2[i], z_trans_2[i], "|Object translations loaded from Slot 2"
            
            i+=1
           
    if int (currentValue) ==3:
        i=0
        for o in objects:
            cmds.setAttr(o + '.translateX', x_trans_3[i])
            cmds.setAttr(o + '.translateY', y_trans_3[i])
            cmds.setAttr(o + '.translateZ', z_trans_3[i])
            
            print o, x_trans_3[i], y_trans_3[i], z_trans_3[i], "|Object translations loaded from Slot 3"
            
            i+=1
  
def getTrans(*args):

        #clear the list of data and start again
    
    objects = cmds.ls(sl=True)
    numberObjectsSel = len(objects)
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
    
    if '1' in currentValue:
        del x_trans_1[:]
        del y_trans_1[:]
        del z_trans_1[:] 
    if '2' in currentValue:
        del x_trans_2[:]
        del y_trans_2[:]
        del z_trans_2[:]
    if '3' in currentValue:
        del x_trans_3[:]
        del y_trans_3[:]
        del z_trans_3[:] 
    
    #object selected?
    if numberObjectsSel==0 :
        print 'No objects selected'
    else:
        for o in objects:
            readTransX=cmds.getAttr(o + '.translateX')
            readTransY=cmds.getAttr(o + '.translateY')
            readTransZ=cmds.getAttr(o + '.translateZ')
            
            if '1' in currentValue:
                x_trans_1.insert(0,readTransX)
                y_trans_1.insert(0,readTransY)
                z_trans_1.insert(0,readTransZ)
            if '2' in currentValue:
                x_trans_2.insert(0,readTransX)
                y_trans_2.insert(0,readTransY)
                z_trans_2.insert(0,readTransZ) 
            if '3' in currentValue:
                x_trans_3.insert(0,readTransX)
                y_trans_3.insert(0,readTransY)
                z_trans_3.insert(0,readTransZ)               
                
                
        if '1' in currentValue:
            x_trans_1.reverse()
            y_trans_1.reverse()
            z_trans_1.reverse() 
            if numberObjectsSel != 0:
                print objects,"X",x_trans_1,"Y",y_trans_1, "Z",z_trans_1, " | Object translations saved to Slot 1"            
                return objects,x_trans_1, y_trans_1, z_trans_1   

        if '2' in currentValue:
            x_trans_2.reverse()
            y_trans_2.reverse()
            z_trans_2.reverse() 
            if numberObjectsSel != 0:
                print objects,"X",x_trans_2,"Y",y_trans_2, "Z",z_trans_2, " | Object translations saved to Slot 2"            
                return objects,x_trans_1, y_trans_1, z_trans_1  


        if '1' in currentValue:
            x_trans_3.reverse()
            y_trans_3.reverse()
            z_trans_3.reverse() 
            if numberObjectsSel != 0:
                print objects,"X",x_trans_3,"Y",y_trans_3, "Z",z_trans_3, " | Object translations saved to Slot 3"            
                return objects,x_trans_3, y_trans_3, z_trans_3                  
                



def zero(*args):

    objects = cmds.ls(sl=True)
    numberObjectsSel = len(objects)

    #object selected?
    if numberObjectsSel==0 :
        print 'No objects selected'
    else:
        for o in objects:
            cmds.setAttr(o + '.rotateX', 0)
            cmds.setAttr(o + '.rotateY', 0)
            cmds.setAttr(o + '.rotateZ', 0)
            cmds.setAttr(o + '.translateX', 0)
            cmds.setAttr(o + '.translateY', 0)
            cmds.setAttr(o + '.translateZ', 0)
        print o,"| Object properties set to 0"    	



def quickSelect(*args):
    currentValue = cmds.optionMenu(save_Slot, query=True, value=True)
    if '1' in currentValue:
        set1 =cmds.sets(name='SET1')
    if '2' in currentValue:
        set2 =cmds.sets(name='SET2')                        
    if '3' in currentValue:
        set3 =cmds.sets(name='SET3')                


cmds.window( width=325, height=100, title ="Quick Poser Tim Kelly 13th Dec" )
cmds.columnLayout( adjustableColumn=True )
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Revert Rotate', align='left', command=setRotate, image1='sphere.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Save Rotate', align='center', command=getRotate, image1='sphere.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Revert Translate', align='left', command=setTrans, image1='cube.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Save Translate', align='center', command=getTrans, image1='cube.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Make Quick Select', align='center', command=quickSelect, image1='cylinder.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='Zero Out', align='center', command=zero, image1='torus.xpm')
cmds.nodeIconButton( style='iconAndTextHorizontal', label='About', align='center', command=showAbout, image1='cone.xpm')

save_Slot = cmds.optionMenu( label='Slot Number: ', changeCommand=updateSlot )
cmds.menuItem(label='1')
cmds.menuItem(label='2')
cmds.menuItem(label='3')


x_rotate_1 = [0,0,0]
y_rotate_1 = [0,0,0]
z_rotate_1 = [0,0,0]
x_trans_1 = [0,0,0]
y_trans_1 = [0,0,0]
z_trans_1 = [0,0,0]

x_rotate_2 = [0,0,0]
y_rotate_2 = [0,0,0]
z_rotate_2 = [0,0,0]
x_trans_2 = [0,0,0]
y_trans_2 = [0,0,0]
z_trans_2 = [0,0,0]

x_rotate_3 = [0,0,0]
y_rotate_3 = [0,0,0]
z_rotate_3 = [0,0,0]
x_trans_3 = [0,0,0]
y_trans_3 = [0,0,0]
z_trans_3 = [0,0,0]

currentValue = 0
objects = []
set1 = []

cmds.showWindow()