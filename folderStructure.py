'''
MAYA COMMAND
import sys
sys.path.append('C:/Snek')
import folderStructure as fold; reload(fold);
fold.tk_folderStructure()
'''


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
        self.widgetsUI['folderStructure'] = cmds.window("Main Form",w=500,h=400, mnb=True, mxb=False, sizeable=True)
        self.widgetsUI['mainForm'] = cmds.formLayout(w=500,h=400,)

        #make stuff
        self.widgetsUI["default_text"] = cmds.text(label = 'Set default directory...', align = 'center')
        self.widgetsUI["default_textTwo"] = cmds.text(label = 'Project Name', align = 'center')

        self.widgetsUI["assetCheck"] = cmds.checkBox(label = 'Create Asset folder', align = 'center',onc=self.tk_unHideSelections,ofc=self.tk_hideSelections)
        self.widgetsUI["texCheck"] = cmds.checkBox(label = 'Create Texture subfolder', align = 'center',en = False)
        self.widgetsUI["documentCheck"] = cmds.checkBox(label = 'Create Documentation folder', align = 'center')
        self.widgetsUI["renderCheck"] = cmds.checkBox(label = 'Create Render folder', align = 'center')

        self.widgetsUI["setRoot"] = cmds.button(label = "Set root folder",bgc=(.5,.5,.5), c = self.tk_setRootFolder,w=490,h=30,align = 'center')
        self.widgetsUI["processButton"] = cmds.button(label = "Process",bgc=(.5,.5,.5), c = self.tk_process,w=490,h=30, align = 'center')
        self.widgetsUI["setMaya"] = cmds.button(label = "Maya",bgc=(.5,.5,.5), c = self.tk_saveMayaFile,w=490,h=30,align = 'center')
        self.widgetsUI["setCustom"] = cmds.button(label = "Create custom folders",bgc=(.5,.5,.5), c = self.tk_customFolders,w=490,h=30,align = 'center')
        self.widgetsUI["processTexturesButton"] = cmds.button(label = "Process Textures in current project",bgc=(.5,.5,.5), c = self.tk_processTex,w=490,h=30, align = 'center')


        self.widgetsUI["projectName_textField"] = cmds.textField(text = 'UntitledProject' , w=490, h=25)
        self.projectName = "UntitledProject"

        #set default address
        if os.name == 'nt':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = 'C:' , w=490, h=25)
            self.rootPath = "C:"
        if os.name == 'posix':
            self.widgetsUI["targetDir_textField"] = cmds.textField(text = '/users/shared' , w=490, h=25)
            self.rootPath = "/users/shared"

        #place stuff
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['projectName_textField'],'top', 115), (self.widgetsUI['targetDir_textField'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['renderCheck'],'top', 0), (self.widgetsUI['renderCheck'], 'left', 200)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['targetDir_textField'],'top', 175), (self.widgetsUI['targetDir_textField'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['default_textTwo'],'top', 100), (self.widgetsUI['default_text'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['default_text'],'top', 160), (self.widgetsUI['default_text'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['setRoot'],'top', 200), (self.widgetsUI['setRoot'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['processButton'],'top', 240), (self.widgetsUI['processButton'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['setMaya'],'top', 275), (self.widgetsUI['setMaya'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['processTexturesButton'],'top', 350), (self.widgetsUI['processTexturesButton'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['setCustom'],'top', 320), (self.widgetsUI['setCustom'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['assetCheck'],'top', 0), (self.widgetsUI['assetCheck'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['texCheck'],'top', 25), (self.widgetsUI['texCheck'], 'left', 5)])
        cmds.formLayout(self.widgetsUI['mainForm'], edit=1, af=[(self.widgetsUI['documentCheck'],'top', 50), (self.widgetsUI['documentCheck'], 'left', 5)])

        #show
        cmds.showWindow(self.widgetsUI['folderStructure'])
        print ("\n\nDetected OS: " + os.name)

    def tk_setRootFolder(self,*args):

        self.rootPath = cmds.textField(self.widgetsUI['targetDir_textField'], query= True, text = True)
        self.projectName = cmds.textField(self.widgetsUI['projectName_textField'], query= True, text = True)
        print "Path: " + self.rootPath + "/" + self.projectName

    def tk_process(self,*args):
        self.tk_setRootFolder()
        assetCheck = cmds.checkBox(self.widgetsUI['assetCheck'], query= True, value = True)
        textureCheck = cmds.checkBox(self.widgetsUI['texCheck'], query= True, value = True)
        documentCheck = cmds.checkBox(self.widgetsUI['documentCheck'], query= True, value = True)
        renderCheck = cmds.checkBox(self.widgetsUI['renderCheck'], query= True, value = True)

        if os.name == 'nt':
            if not os.path.exists(self.rootPath +"/" + self.projectName):
                os.mkdir(self.rootPath +"/" + self.projectName)
            else:
                print('Using existing directory at: ' + self.rootPath +"/" + self.projectName)
                if assetCheck == True:
                    self.tk_createFolder("Assets")
                if textureCheck == True:
                    self.tk_createFolder("Assets/Textures")
                if documentCheck == True:
                    self.tk_createFolder("Documentation")
                if renderCheck == True:
                    self.tk_createFolder("Renders")
                print 'Process complete \n\n'

        if os.name == 'posix':
            if not os.path.exists(self.rootPath +"/" + self.projectName):
                os.mkdir(self.rootPath +"/" + self.projectName)
            else:
                print('Using existing directory at: ' + self.rootPath +"/" + self.projectName)
            if assetCheck == True:
                self.tk_createFolder("Assets")
            if textureCheck == True:
                self.tk_createFolder("Assets/Textures")
            if documentCheck == True:
                self.tk_createFolder("Documentation")
            if renderCheck == True:
                self.tk_createFolder("Renders")
            print 'Process complete \n\n'


    def tk_unHideSelections(self,*args):
        cmds.checkBox(self.widgetsUI['texCheck'], edit= True, en=True,v=True)

    def tk_hideSelections(self,*args):
        cmds.checkBox(self.widgetsUI['texCheck'], edit= True, en=False)

    def tk_processTex(self,*args):

        #empty arrays
        self.fileDictList = {}

        #For every file node Node f get the location and store them
        nodes = cmds.ls(type = 'file')
        if not len(nodes) == 0:
            for f in self.fileNodes:
                self.fileDictList[f]=cmds.getAttr('%s.fileTextureName' % f)
        else:
            print "No file nodes found"

        if self.fileDictList:
            for key in self.fileDictList:
                src = self.fileDictList[key]
                if os.path.exists(self.rootPath + "/"+self.projectName + "/Assets/Textures"):
                    print ("Copying: " + src)
                    shutil.copy(src, (self.rootPath + "/" + self.projectName + "/Assets/Textures"))
                else:
                    print "Ensure that texture project directory has been created"

    def tk_saveMayaFile(self,*args):
        if not os.path.exists(self.rootPath + "/"+ self.projectName):
            print "Ensure that the project directory has been created"
        else:
            nameEntry = cmds.promptDialog(title='Rename...',message='Enter filename:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
            name = cmds.promptDialog(query=True, text = True)
            print (self.rootPath + "/" + self.projectName + "/"+ name + ".ma")
            cmds.file(rename= (self.rootPath + "/" + self.projectName + "/"+ name + ".ma"))
            cmds.file(save=True, type="mayaAscii")

    def tk_createFolder(self,folderName):
        if not os.path.exists(self.rootPath + "/"+self.projectName + "/" + folderName):
            os.mkdir(self.rootPath + "/"+ self.projectName + "/"  + folderName)
            print (folderName + " path created at "+self.rootPath + "/"+ self.projectName + "/" + folderName)

        else:
            print('Directory already exists at: ' + self.rootPath + "/" + self.projectName + "/" + folderName)

    def tk_customFolders(self,*args):
        numberTwo = int(input("Enter a number"))
        for i in range (0,numberTwo):
            i=i+1
            nameEntry = cmds.promptDialog(title='Rename...',message='Enter folder no.' + str(i) +' name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
            name = cmds.promptDialog(query=True, text = True)
            self.tk_createFolder(name)
