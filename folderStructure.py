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

        #make stuff
        self.widgetsUI["default_text"] = cmds.text(label = 'Set default directory...', align = 'center')
        self.widgetsUI["textCheck"] = cmds.checkBox(label = 'Create Texture folder', align = 'center')
        self.widgetsUI["documentCheck"] = cmds.checkBox(label = 'Create Documentation folder', align = 'center')
        self.widgetsUI["setRoot"] = cmds.button(label = "Set root folder",bgc=(.5,.5,.5), c = self.tk_setRootFolder,w=490,h=30)
        self.widgetsUI["processButton"] = cmds.button(label = "Process",bgc=(.5,.5,.5), c = self.tk_process,w=490,h=30)

        #set default address
        if os.name == 'nt':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = 'C:/' , w=490, h=25)
        if os.name == 'osx':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = '/users' , w=490, h=25)

        #place stuff
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['targetDir_textField'],'top', 175), (self.widgetsUI['targetDir_textField'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['default_text'],'top', 150), (self.widgetsUI['default_text'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['setRoot'],'top', 200), (self.widgetsUI['setRoot'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['processButton'],'top', 250), (self.widgetsUI['setRoot'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['textCheck'],'top', 0), (self.widgetsUI['setRoot'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['documentCheck'],'top', 25), (self.widgetsUI['setRoot'], 'left', 5)])

        #show
        cmds.showWindow(self.widgetsUI['folderStructure'])

    def tk_setRootFolder(self,*args):

        rootPath = cmds.textField(self.widgetsUI['targetDir_textField'], query= True, text = True)
        print "Path: " + rootPath

    def tk_process(self,*args):
        textCheck = cmds.checkBox(self.widgetsUI['textCheck'], query= True, value = True)
        documentCheck = cmds.checkBox(self.widgetsUI['documentCheck'], query= True, value = True)

        print ("Detected OS: " + os.name)

        if os.name == 'nt':
            if not os.path.exists('C:/Snek'):
                os.mkdir('C:/Snek')
                print('Directory Made')
            else:
                print('Using existing directory at C:/Snek/')

            if textCheck == True:
                print "Creating Texture Directory..."
                if not os.path.exists('C:/Snek/Textures'):
                    os.mkdir('C:/Snek/Textures')
                else:
                    print('Directory already exists at C:/Snek/Textures')

            if documentCheck == True:
                print "Creating Documentation Directory..."
                if not os.path.exists('C:/Snek/Documentation'):
                    os.mkdir('C:/Snek/Documentation')
                else:
                    print('Directory already exists at C:/Snek/Documentation')

        if os.name == 'psix':
            if not os.path.exists('/Users/Shared/Snek'):
                os.mkdir('/Users/Shared/Snek')
            else:
                print('Using existing directory at /Users/Shared/Snek')

            if textCheck == True:
                if not os.path.exists('/Users/Shared/Snek/Textures'):
                    os.mkdir('/Users/Shared/Snek/Textures')
                else:
                    print('Directory already exists at /Users/Shared/Snek/Textures')

            if documentCheck == True:
                if not os.path.exists('/Users/Shared/Snek/Documentation'):
                    os.mkdir('/Users/Shared/Snek/Documentation')
                else:
                    print('Directory already exists at /Users/Shared/Snek/Documentation')
        print 'Process complete'
