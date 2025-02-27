#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2017 Yorik van Havre <yorik@uncreated.net>              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************


# main workbench class

class BIMWorkbench(Workbench):


    def __init__(self):

        self.__class__.MenuText = "BIM"
        self.__class__.ToolTip = "BIM workbench"
        self.__class__.Icon = """
/* XPM */
static char * IFC_xpm[] = {
"16 16 9 1",
" 	c None",
".	c #D80742",
"+	c #C20B5E",
"@	c #B11A71",
"#	c #0E4A94",
"$	c #A12288",
"%	c #61398E",
"&	c #983563",
"*	c #1E8BA6",
"                ",
"     #   ..     ",
"    ### ....    ",
"   ## ##+  ..   ",
"  ##  .##   ..  ",
" ##  +. ##   .. ",
" ## $$$+##**..  ",
"  #%$$$%#**&.   ",
"  $$% ##*+..&*  ",
" $$$###*@..  ** ",
" $$  #**$@@  ** ",
"  $$  **%$  **  ",
"   $$  **  **   ",
"    $$$$****    ",
"     $$  **     ",
"                "};
"""

    def Initialize(self):

        # All BIM commands are specified either in BimCommands.py, or
        # in separate files (BimSetup.py, BimProject.py...) that are imported in BimCommands.
        # So importing BimCommands is all that is needed to get all the commands.

        import DraftTools
        import Arch
        import PartGui
        import SketcherGui

        import BimCommands
        import BimWelcome
        import BimSetup
        import BimProject
        import BimWindows
        import BimIfcElements
        import BimViews
        import BimClassification
        import BimBox
        import BimTutorial
        import BimLibrary
        import BimMaterial
        import BimIfcQuantities
        import BimIfcProperties
        import BimNudge
        import BimUnclone
        import BimPreflight
        import BimReextrude
        import BimDiff
        import BimIfcExplorer
        import BimLayers

        FreeCADGui.addCommand('BIM_TogglePanels',BimCommands.BIM_TogglePanels())
        FreeCADGui.addCommand('BIM_Trash',BimCommands.BIM_Trash())
        FreeCADGui.addCommand('BIM_EmptyTrash',BimCommands.BIM_EmptyTrash())
        FreeCADGui.addCommand('BIM_Copy',BimCommands.BIM_Copy())
        FreeCADGui.addCommand('BIM_Clone',BimCommands.BIM_Clone())
        FreeCADGui.addCommand('BIM_Help',BimCommands.BIM_Help())
        FreeCADGui.addCommand('BIM_Glue',BimCommands.BIM_Glue())
        FreeCADGui.addCommand('BIM_Sketch',BimCommands.BIM_Sketch())
        FreeCADGui.addCommand('BIM_WPView',BimCommands.BIM_WPView())
        FreeCADGui.addCommand('BIM_Convert',BimCommands.BIM_Convert())
        FreeCADGui.addCommand('BIM_Ungroup',BimCommands.BIM_Ungroup())
        FreeCADGui.addCommand('BIM_Column',BimCommands.BIM_Column())
        FreeCADGui.addCommand('BIM_Beam',BimCommands.BIM_Beam())
        FreeCADGui.addCommand('BIM_Slab',BimCommands.BIM_Slab())
        FreeCADGui.addCommand('BIM_Door',BimCommands.BIM_Door())
        FreeCADGui.addCommand('BIM_ResetCloneColors',BimCommands.BIM_ResetCloneColors())
        FreeCADGui.addCommand('BIM_Rewire',BimCommands.BIM_Rewire())
        FreeCADGui.addCommand('BIM_Welcome',BimWelcome.BIM_Welcome())
        FreeCADGui.addCommand('BIM_Setup',BimSetup.BIM_Setup())
        FreeCADGui.addCommand('BIM_Project',BimProject.BIM_Project())
        FreeCADGui.addCommand('BIM_Windows',BimWindows.BIM_Windows())
        FreeCADGui.addCommand('BIM_IfcElements',BimIfcElements.BIM_IfcElements())
        FreeCADGui.addCommand('BIM_Views',BimViews.BIM_Views())
        FreeCADGui.addCommand('BIM_Classification',BimClassification.BIM_Classification())
        FreeCADGui.addCommand('BIM_Box',BimBox.BIM_Box())
        FreeCADGui.addCommand('BIM_Tutorial',BimTutorial.BIM_Tutorial())
        FreeCADGui.addCommand('BIM_Library',BimLibrary.BIM_Library())
        FreeCADGui.addCommand('BIM_Material',BimMaterial.BIM_Material())
        FreeCADGui.addCommand('BIM_IfcQuantities',BimIfcQuantities.BIM_IfcQuantities())
        FreeCADGui.addCommand('BIM_IfcProperties',BimIfcProperties.BIM_IfcProperties())
        FreeCADGui.addCommand('BIM_Nudge_Switch',BimNudge.BIM_Nudge_Switch())
        FreeCADGui.addCommand('BIM_Nudge_Up',BimNudge.BIM_Nudge_Up())
        FreeCADGui.addCommand('BIM_Nudge_Down',BimNudge.BIM_Nudge_Down())
        FreeCADGui.addCommand('BIM_Nudge_Left',BimNudge.BIM_Nudge_Left())
        FreeCADGui.addCommand('BIM_Nudge_Right',BimNudge.BIM_Nudge_Right())
        FreeCADGui.addCommand('BIM_Nudge_Extend',BimNudge.BIM_Nudge_Extend())
        FreeCADGui.addCommand('BIM_Nudge_Shrink',BimNudge.BIM_Nudge_Shrink())
        FreeCADGui.addCommand('BIM_Nudge_RotateLeft',BimNudge.BIM_Nudge_RotateLeft())
        FreeCADGui.addCommand('BIM_Nudge_RotateRight',BimNudge.BIM_Nudge_RotateRight())
        FreeCADGui.addCommand('BIM_Unclone',BimUnclone.BIM_Unclone())
        FreeCADGui.addCommand('BIM_Preflight',BimPreflight.BIM_Preflight())
        FreeCADGui.addCommand('BIM_Diff',BimDiff.BIM_Diff())
        FreeCADGui.addCommand('BIM_IfcExplorer',BimIfcExplorer.BIM_IfcExplorer())
        FreeCADGui.addCommand('BIM_Layers',BimLayers.BIM_Layers())

        self.draftingtools = ["BIM_Sketch","Draft_Line","Draft_Wire","Draft_Circle","Draft_Arc","Draft_Ellipse",
                              "Draft_Polygon","Draft_Rectangle", "Draft_BSpline", "Draft_BezCurve",
                              "Draft_Point"]

        self.annotationtools = ["Draft_Text", "Draft_ShapeString", "Draft_Dimension",
                                "Draft_Label","Arch_Axis","Arch_AxisSystem","Arch_Grid","Arch_SectionPlane"]

        self.bimtools = ["Arch_Floor","Arch_Building","Arch_Site","Arch_Space","Separator",
                         "Arch_Wall","BIM_Column","BIM_Beam","BIM_Slab","Arch_Rebar","BIM_Door","Arch_Window","Arch_Pipe",
                         "Arch_PipeConnector","Arch_Stairs","Arch_Roof","Arch_Panel","Arch_Frame",
                         "Separator","BIM_Box","Part_Builder","Draft_Facebinder","BIM_Library"]

        self.modify = ["Draft_Move","BIM_Copy","Draft_Rotate","BIM_Clone","BIM_Unclone","Draft_Offset",
                       "Part_Offset2D", "Draft_Trimex","Draft_Join","Draft_Split","Draft_Scale","Draft_Stretch",
                       "BIM_Rewire","BIM_Glue","Draft_Upgrade", "Draft_Downgrade",
                       "Draft_Draft2Sketch","Arch_CutPlane","Arch_Add","Arch_Remove","BIM_Reextrude",
                       "Draft_Array","Draft_PathArray","Draft_PointArray",
                       "Draft_Mirror","Part_Extrude","Part_Cut","Part_Fuse","Part_Common","Part_Compound",
                       "Part_SimpleCopy","Draft_Shape2DView"]

        # Support post-v0.18 tools

        if "Arch_Reference" in Gui.listCommands():
            self.bimtools.insert(-4,"Arch_Reference")
        if "Arch_Fence" in Gui.listCommands():
            self.bimtools.insert(-6,"Arch_Fence")
        if "Draft_Arc_3Points" in Gui.listCommands():
            self.draftingtools.insert(5,"Draft_Arc_3Points")
        if 'Draft_CubicBezCurve' in Gui.listCommands():
            self.draftingtools.insert(len(self.draftingtools)-2,'Draft_CubicBezCurve')


        # load rebar tools (Reinforcement addon)
        try:
            import RebarTools
        except:
            pass
        else:
            # create popup group for Rebar tools
            class RebarGroupCommand:
                def GetCommands(self):
                    return tuple(["Arch_Rebar"]+RebarTools.RebarCommands)
                def GetResources(self):
                    return { 'MenuText': 'Reinforcement tools','ToolTip': 'Reinforcement tools'}
                def IsActive(self):
                    return not FreeCAD.ActiveDocument is None
            FreeCADGui.addCommand('Arch_RebarTools', RebarGroupCommand())
            self.bimtools[self.bimtools.index("Arch_Rebar")] = "Arch_RebarTools"

        self.snap = ['Draft_ToggleGrid','Draft_Snap_Lock','Draft_Snap_Midpoint','Draft_Snap_Perpendicular',
                     'Draft_Snap_Grid','Draft_Snap_Intersection','Draft_Snap_Parallel',
                     'Draft_Snap_Endpoint','Draft_Snap_Angle','Draft_Snap_Center',
                     'Draft_Snap_Extension','Draft_Snap_Near','Draft_Snap_Ortho',
                     'Draft_Snap_Special','Draft_Snap_Dimensions','Draft_Snap_WorkingPlane']

        self.manage = ["BIM_Setup","BIM_Project","BIM_Views","BIM_Windows","BIM_IfcElements",
                       "BIM_IfcQuantities","BIM_IfcProperties","BIM_Classification",
                       "BIM_Material","Arch_Schedule","BIM_Preflight"]

        self.utils = ["BIM_TogglePanels","BIM_Trash","BIM_WPView",
                      "Draft_Slope","Draft_SetWorkingPlaneProxy","Draft_AddConstruction",
                      "Arch_SplitMesh","Arch_MeshToShape",
                      "Arch_SelectNonSolidMeshes","Arch_RemoveShape",
                      "Arch_CloseHoles","Arch_MergeWalls","Arch_Check",
                      "Arch_ToggleIfcBrepFlag",
                      "Arch_ToggleSubs","Arch_Survey","BIM_Diff","BIM_IfcExplorer"]

        nudge = ["BIM_Nudge_Switch","BIM_Nudge_Up","BIM_Nudge_Down","BIM_Nudge_Left","BIM_Nudge_Right",
                 "BIM_Nudge_RotateLeft","BIM_Nudge_RotateRight","BIM_Nudge_Extend","BIM_Nudge_Shrink"]

        # post-0.18 tools

        if "Draft_Layer" in Gui.listCommands():
            self.manage.insert(8,"BIM_Layers")

        # try to load bimbots

        try:
            import bimbots
        except:
            pass
        else:
            class BIMBots:
                def GetResources(self):
                    return bimbots.get_plugin_info()
                def Activated(self):
                    bimbots.launch_ui()
            FreeCADGui.addCommand('BIMBots', BIMBots())
            self.utils.append("BIMBots")

        # load Reporting

        try:
            import report
        except:
            pass
        else:
            if "Report_Create" in Gui.listCommands():
                self.manage[self.manage.index("Arch_Schedule")] = "Report_Create"

        # load webtools

        try:
            import BIMServer, Git, Sketchfab
        except:
            pass
        else:
            self.utils.extend(["WebTools_Git","WebTools_BimServer","WebTools_Sketchfab"])

        # load flamingo

        try:
            import CommandsPolar,CommandsFrame,CommandsPipe
        except:
            flamingo = None
        else:
            flamingo = ["frameIt","fillFrame","insertPath","insertSection","FrameLineManager","spinSect",
                        "reverseBeam","shiftBeam","pivotBeam","levelBeam","alignEdge","rotJoin","alignFlange",
                        "stretchBeam","extend","adjustFrameAngle","insertPipe","insertElbow","insertReduct",
                        "insertCap","insertFlange","insertUbolt","insertPypeLine","breakPipe","mateEdges",
                        "extend2intersection","extend1intersection","laydown","raiseup"]

        # load fasteners

        try:
            import FastenerBase,FastenersCmd
        except:
            fasteners = None
        else:
            fasteners = [c for c in FastenerBase.FSGetCommands("screws") if not isinstance(c,tuple)]

        # create toolbars

        self.appendToolbar("Drafting tools",self.draftingtools)
        self.appendToolbar("3D/BIM tools",self.bimtools)
        self.appendToolbar("Annotation tools",self.annotationtools)
        self.appendToolbar("Modification tools",self.modify)
        self.appendToolbar("Manage tools",self.manage)
        #if flamingo:
        #    self.appendToolbar("Flamingo tools",flamingo)

        # create menus

        def QT_TRANSLATE_NOOP(scope, text): return text # dummy function for the QT translator

        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&2D Drafting"),self.draftingtools)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&3D/BIM"),self.bimtools)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Annotation"),self.annotationtools)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Snapping"),self.snap)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Modify"),self.modify)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Manage"),self.manage)
        if flamingo:
            self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Flamingo"),flamingo)
        if fasteners:
            self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Fasteners"),fasteners)
        self.appendMenu(QT_TRANSLATE_NOOP("BIM","&Utils"),self.utils)
        self.appendMenu([QT_TRANSLATE_NOOP("BIM","&Utils"),"Nudge"],nudge)
        self.appendMenu("&Help",["BIM_Welcome","BIM_Help","BIM_Tutorial"])

        # load Arch & Draft preference pages

        if hasattr(FreeCADGui,"draftToolBar"):
            if not hasattr(FreeCADGui.draftToolBar,"loadedArchPreferences"):
                import Arch_rc
                FreeCADGui.addPreferencePage(":/ui/preferences-arch.ui","Arch")
                FreeCADGui.addPreferencePage(":/ui/preferences-archdefaults.ui","Arch")
                FreeCADGui.draftToolBar.loadedArchPreferences = True
            if not hasattr(FreeCADGui.draftToolBar,"loadedPreferences"):
                import Draft_rc
                FreeCADGui.addPreferencePage(":/ui/preferences-draft.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-draftsnap.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-draftvisual.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-drafttexts.ui","Draft")
                FreeCADGui.draftToolBar.loadedPreferences = True

        # add translations path

        FreeCADGui.addLanguagePath(BimCommands.getLanguagePath())

        Log ('Loading BIM module... done\n')

    def setupMultipleObjectSelection(self):

        import BimSelect
        if hasattr(FreeCADGui,"addDocumentObserver") and not hasattr(self,"BimSelectObserver"):
            self.BimSelectObserver = BimSelect.Setup()
            FreeCADGui.addDocumentObserver(self.BimSelectObserver)

    def Activated(self):

        if hasattr(FreeCADGui,"draftToolBar"):
            FreeCADGui.draftToolBar.Activated()
        if hasattr(FreeCADGui,"Snapper"):
            FreeCADGui.Snapper.show()

        from DraftGui import todo
        import BimCommands

        if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/BIM").GetBool("FirstTime",True) and (not hasattr(FreeCAD,"TestEnvironment")):
            todo.delay(FreeCADGui.runCommand,"BIM_Welcome")
        todo.delay(BimCommands.setStatusIcons,True)

        FreeCADGui.Control.clearTaskWatcher()

        class BimWatcher:

            def __init__(self,cmds,name,invert=False):

                self.commands = cmds
                self.title = name
                self.invert = invert

            def shouldShow(self):

                if self.invert:
                    return (FreeCAD.ActiveDocument != None) and (FreeCADGui.Selection.getSelection() != [])
                else:
                    return (FreeCAD.ActiveDocument != None) and (not FreeCADGui.Selection.getSelection())

        FreeCADGui.Control.addTaskWatcher([BimWatcher(self.draftingtools+self.annotationtools,"2D geometry"),
                                           BimWatcher(self.bimtools,"3D/BIM geometry"),
                                           BimWatcher(self.modify,"Modify",invert=True)])

        # restore views widget if needed

        if FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/BIM").GetBool("RestoreBimViews",True):
            import BimViews
            w = BimViews.findWidget()
            if not w:
                FreeCADGui.runCommand("BIM_Views")
            else:
                w.show()

        self.setupMultipleObjectSelection()

        Log("BIM workbench activated\n")


    def Deactivated(self):

        if hasattr(self,"BimSelectObserver"):
            FreeCADGui.removeDocumentObserver(self.BimSelectObserver)
            del self.BimSelectObserver

        if hasattr(FreeCADGui,"draftToolBar"):
            FreeCADGui.draftToolBar.Deactivated()
        if hasattr(FreeCADGui,"Snapper"):
            FreeCADGui.Snapper.hide()

        from DraftGui import todo
        import BimCommands
        import BimViews

        #print("Deactivating status icon")

        todo.delay(BimCommands.setStatusIcons,False)

        FreeCADGui.Control.clearTaskWatcher()

        # store views widget state and vertical size

        w = BimViews.findWidget()
        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/BIM").SetBool("RestoreBimViews",bool(w))
        if w:
            FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/BIM").SetInt("BimViewsSize",w.height())
            w.hide()

        Log("BIM workbench deactivated\n")


    def ContextMenu(self, recipient):

        import BimCommands,DraftTools
        if (recipient == "Tree"):
            groups = False
            ungroupable = False
            for o in FreeCADGui.Selection.getSelection():
                if o.isDerivedFrom("App::DocumentObjectGroup") or o.hasExtension("App::GroupExtension"):
                    groups = True
                else:
                    groups = False
                    break
            for o in FreeCADGui.Selection.getSelection():
                for parent in o.InList:
                    if parent.isDerivedFrom("App::DocumentObjectGroup") or parent.hasExtension("App::GroupExtension"):
                        if o in parent.Group:
                            ungroupable = True
                        else:
                            ungroupable = False
                            break
            if groups:
                self.appendContextMenu("",["Draft_SelectGroup"])
            if ungroupable:
                self.appendContextMenu("",["BIM_Ungroup"])
            if (len(FreeCADGui.Selection.getSelection()) == 1) and (FreeCADGui.Selection.getSelection()[0].Name == "Trash"):
                self.appendContextMenu("",["BIM_EmptyTrash"])
        elif (recipient == "View"):
            self.appendContextMenu("Snapping",self.snap)
        if FreeCADGui.Selection.getSelection():
            if (FreeCADGui.Selection.getSelection()[0].Name != "Trash"):
                self.appendContextMenu("",["BIM_Trash"])
            self.appendContextMenu("",["Draft_AddConstruction"])
            allclones = False
            for obj in FreeCADGui.Selection.getSelection():
                if hasattr(obj,"CloneOf") and obj.CloneOf:
                    allclones = True
                else:
                    allclones = False
                    break
            if allclones:
                self.appendContextMenu("",["BIM_ResetCloneColors"])



    def GetClassName(self):

        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(BIMWorkbench)




