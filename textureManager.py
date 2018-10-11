import maya.cmds as cmds
import shutil as shutil

class tk_textureManager():
    def __init__(self):
        if cmds.window('textureManager', exists=1):
            cmds.deleteUI('textureManager')

        self.widgets = {}


        self.widgets["textureManager"] = cmds.window("textureManager", title = "Texture Manager", w=500, h=300, mnb=True, mxb=False, sizeable=0)

        self.widgets['mainForm'] = cmds.formLayout(w=500,h=300,)

        self.widgets["Anaylise_Button"] = cmds.button(label = "Anaylise scene for Files",bgc=(1,0.5,.8), c = self.tk_module_fileListFiles,w=490,h=30)
        self.widgets["Analyse_field"] = cmds.textScrollList(w=490, h=120, ams = 1)
        self.widgets["targetDir_textField"] = cmds.textField(text = 'C:/' , w=490, h=25)
        self.widgets["copy_button"] = cmds.button(label = "Copy Selected Files",bgc=(1,0.5,.8),w=240,h=40, c = self.tk_module_copyFiles)
        self.widgets["setPath_button"] = cmds.button(label = "Set New Path",bgc=(1,0.5,.8),w=240,h=40, c=self.tk_module_fileSetPath)

        cmds.formLayout(self.widgets['mainForm'], edit=1, af=[(self.widgets['Anaylise_Button'],'top', 5), (self.widgets['Anaylise_Button'], 'left', 5)])
        cmds.formLayout(self.widgets['mainForm'], edit=1, af=[(self.widgets['Analyse_field'],'top', 40), (self.widgets['Analyse_field'], 'left', 5)])
        cmds.formLayout(self.widgets['mainForm'], edit=1, af=[(self.widgets['targetDir_textField'],'top', 165), (self.widgets['targetDir_textField'], 'left', 5)])
        cmds.formLayout(self.widgets['mainForm'], edit=1, af=[(self.widgets['copy_button'],'top', 200), (self.widgets['copy_button'], 'left', 5)])
        cmds.formLayout(self.widgets['mainForm'], edit=1, af=[(self.widgets['setPath_button'],'top', 200), (self.widgets['setPath_button'], 'left', 255)])


        cmds.showWindow(self.widgets['textureManager'])

    def tk_module_fileListFiles(self, *args):
        self.fileNodes = cmds.ls(type='file')
        self.fileDictList = {}

        self.allPaths = []

        for f in self.fileNodes:
            fPathName = cmds.getAttr('%s.fileTextureName' % f)
            self.fileDictList[f]=cmds.getAttr('%s.fileTextureName' % f)

            fPath = fPathName.rpartition('/')[0]

            if fPath in self.allPaths:
                pass
            elif fPath == '':
                pass
            else:
                self.allPaths.append(fPath)

        cmds.textScrollList(self.widgets['Analyse_field'],e=1, ra=1)
        cmds.textScrollList(self.widgets['Analyse_field'],e=1, append=self.allPaths)

    def tk_module_copyFiles(self, *args):
        selectedPath = cmds.textScrollList(self.widgets['Analyse_field'],q=1,selectItem=1)
        self.fileNewPathDict = {}

        if selectedPath:
            for sp in selectedPath:
                if self.fileDictList:
                    for key in self.fileDictList:

                        src=self.fileDictList[key]

                        if sp in src:
                            fileName=self.fileDictList[key].rpartition('/')[2]

                            path = cmds.textField(self.widgets['targetDir_textField'],q=1,text=1)

                            dst = "%s/%s" % (path,fileName)

                            shutil.copy(src,dst)

                            self.fileNewPathDict[key] = dst
        else:
            print ("Nothing selected")

    def tk_module_fileSetPath(self,*args):
        selectedPath = cmds.textScrollList(self.widgets['Analyse_field'],q=1,selectItem=1)

        if selectedPath and self.fileNodes:
            for sp in selectedPath:
                for f in self.fileNodes:
                    file =cmds.getAttr('%s.fileTextureName' % f)
                    fileName = file.rpartition('/')[2]


                    #get name in text textField
                    path = cmds.textField(self.widgets['targetDir_textField'],q=1,text=1)
                    fullPathName ="%s/%s" % (path,fileName)

                    #set the attrivute to the new Path
                    fPathName = cmds.setAttr('%s.fileTextureName' % f,fullPathName,type = 'string')
