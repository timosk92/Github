import maya.cmds as cmds
import shutil as shutil
import os

class tk_folderStructure():
    def __init__(self):
        if cmds.window('folderStructure', exists = True):
            cmds.delete('folderStructure')
        #array of UI elements
        self.widgetsUI = {}

        #window
        self.widgetsUI['folderStructure'] = cmds.window("Main Form",w=500,h=300, mnb=True, mxb=False, sizeable=False)
        self.widgetsUI['mainForm'] = cmds.formLayout(w=500,h=300,)


        print ("Detected OS: " + os.name)

        #make stuff
        self.widgetsUI["default_text"] = cmds.text(label = 'Set default directory...', align = 'center')
        self.widgetsUI["setRoot"] = cmds.button(label = "Set root folder",bgc=(.5,.5,.5), c = self.tk_setRootFolder,w=490,h=30)

        #set default address
        if os.name == 'nt':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = 'C:/' , w=490, h=25)
        if os.name == 'osx':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = '/users' , w=490, h=25)

        #place stuff
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['default_text'],'top', 50), (self.widgetsUI['default_text'], 'left', 50)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['setRoot'],'top', 250), (self.widgetsUI['setRoot'], 'left', 250)])

        #show
        cmds.showWindow(self.widgetsUI['folderStructure'])



    def tk_setRootFolder(self,*args):
        print ('test')
        if os.name == 'nt':
            if not os.path.exists('C:/Snek'):
                os.mkdir('C:/Snek')
                print('Directory Made')
            else:
                print('Already exists')
        if os.name == 'osx':
            if not os.path.exists('C:/Snek'):
                os.mkdir('/Users/Shared/Snek')

    def tk_process(self,*args):
        pass
