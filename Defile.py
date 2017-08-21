import wx
import time
#include <wx/sizer.h>
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        self.panel = wx.Panel(self)
        self.head = wx.StaticText(self.panel, label="Defile Simulator!", style=wx.ALIGN_CENTRE)
        font = self.head.GetFont()
        font.PointSize += 10
        font = font.Bold()
        self.head.SetFont(font)

        self.enemyBoard = wx.StaticText(self.panel, label="Enemy Board Minions:")
        self.button = wx.Button(self.panel, label="Cast Defile!")
        self.yourBoard = wx.StaticText(self.panel, label="Your Board Minions:")
        
        self.endivineShield1 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield2 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield3 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield4 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield5 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield6 = wx.CheckBox(self.panel, label="Divine?")
        self.endivineShield7 = wx.CheckBox(self.panel, label="Divine?")

        self.eb1 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb1.Bind(wx.EVT_CHAR, self.check_int)
        self.eb2 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb2.Bind(wx.EVT_CHAR, self.check_int)
        self.eb3 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb3.Bind(wx.EVT_CHAR, self.check_int)
        self.eb4 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb4.Bind(wx.EVT_CHAR, self.check_int)
        self.eb5 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb5.Bind(wx.EVT_CHAR, self.check_int)
        self.eb6 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb6.Bind(wx.EVT_CHAR, self.check_int)
        self.eb7 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.eb7.Bind(wx.EVT_CHAR, self.check_int)

        self.b1 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b1.Bind(wx.EVT_CHAR, self.check_int)
        self.b2 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b2.Bind(wx.EVT_CHAR, self.check_int)
        self.b3 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b3.Bind(wx.EVT_CHAR, self.check_int)
        self.b4 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b4.Bind(wx.EVT_CHAR, self.check_int)
        self.b5 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b5.Bind(wx.EVT_CHAR, self.check_int)
        self.b6 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b6.Bind(wx.EVT_CHAR, self.check_int)
        self.b7 = wx.TextCtrl(self.panel, size=(70, -1), value='0')
        self.b7.Bind(wx.EVT_CHAR, self.check_int)

        self.divineShield1 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage1 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield2 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage2 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield3 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage3 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield4 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage4 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield5 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage5 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield6 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage6 = wx.CheckBox(self.panel, label="SPDamage?")
        self.divineShield7 = wx.CheckBox(self.panel, label="Divine?")
        self.spDamage7 = wx.CheckBox(self.panel, label="SPDamage?")
        

        

        
        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)        

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(10, 10)
        self.sizer.Add(self.head, (0,0))
        self.sizer.Add(self.endivineShield1, (1,1))
        self.sizer.Add(self.endivineShield2, (1,2))
        self.sizer.Add(self.endivineShield3, (1,3))
        self.sizer.Add(self.endivineShield4, (1,4))
        self.sizer.Add(self.endivineShield5, (1,5))
        self.sizer.Add(self.endivineShield6, (1,6))
        self.sizer.Add(self.endivineShield7, (1,7))
        self.sizer.Add(self.enemyBoard, (2, 0))
        self.sizer.Add(self.eb1, (2, 1))
        self.sizer.Add(self.eb2, (2, 2))
        self.sizer.Add(self.eb3, (2, 3))
        self.sizer.Add(self.eb4, (2, 4))
        self.sizer.Add(self.eb5, (2, 5))
        self.sizer.Add(self.eb6, (2, 6))
        self.sizer.Add(self.eb7, (2, 7))

        self.sizer.Add(self.yourBoard, (4, 0))
        self.sizer.Add(self.b1, (4, 1))
        self.sizer.Add(self.b2, (4, 2))
        self.sizer.Add(self.b3, (4, 3))
        self.sizer.Add(self.b4, (4, 4))
        self.sizer.Add(self.b5, (4, 5))
        self.sizer.Add(self.b6, (4, 6))
        self.sizer.Add(self.b7, (4, 7))
        self.sizer.Add(self.divineShield1, (5,1))
        self.sizer.Add(self.spDamage1, (6,1))
        self.sizer.Add(self.divineShield2, (5,2))
        self.sizer.Add(self.spDamage2, (6,2))
        self.sizer.Add(self.divineShield3, (5,3))
        self.sizer.Add(self.spDamage3, (6,3))
        self.sizer.Add(self.divineShield4, (5,4))
        self.sizer.Add(self.spDamage4, (6,4))
        self.sizer.Add(self.divineShield5, (5,5))
        self.sizer.Add(self.spDamage5, (6,5))
        self.sizer.Add(self.divineShield6, (5,6))
        self.sizer.Add(self.spDamage6, (6,6))
        self.sizer.Add(self.divineShield7, (5,7))
        self.sizer.Add(self.spDamage7, (6,7))
        self.sizer.Add(self.button, (8, 0), flag=wx.EXPAND)

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)  

        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        # create a menu bar
        self.makeMenuBar()
        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to ezDefile!")

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a Calculator to help with you with the warlock spell Defile! (Work in progress)",
                      "About ezDefile",
                      wx.OK|wx.ICON_INFORMATION)
        
    def OnButton(self, e):
        if(self.b1.GetValue() == ''):
            self.b1.SetValue('0')
        if(self.b2.GetValue() == ''):
            self.b2.SetValue('0')
        if(self.b3.GetValue() == ''):
            self.b3.SetValue('0')
        if(self.b4.GetValue() == ''):
            self.b4.SetValue('0')
        if(self.b5.GetValue() == ''):
            self.b5.SetValue('0')
        if(self.b6.GetValue() == ''):
            self.b6.SetValue('0')
        if(self.b7.GetValue() == ''):
            self.b7.SetValue('0')
        if(self.eb1.GetValue() == ''):
            self.eb1.SetValue('0')
        if(self.eb2.GetValue() == ''):
            self.eb2.SetValue('0')
        if(self.eb3.GetValue() == ''):
            self.eb3.SetValue('0')
        if(self.eb4.GetValue() == ''):
            self.eb4.SetValue('0')
        if(self.eb5.GetValue() == ''):
            self.eb5.SetValue('0')
        if(self.eb6.GetValue() == ''):
            self.eb6.SetValue('0')
        if(self.eb7.GetValue() == ''):
            self.eb7.SetValue('0')
        minions = {1: (int(self.b1.GetValue()), self.divineShield1.GetValue(), self.spDamage1.GetValue()),
                   2: (int(self.b2.GetValue()), self.divineShield2.GetValue(), self.spDamage2.GetValue()),
                   3: (int(self.b3.GetValue()), self.divineShield3.GetValue(), self.spDamage3.GetValue()),
                   4: (int(self.b4.GetValue()), self.divineShield4.GetValue(), self.spDamage4.GetValue()),
                   5: (int(self.b5.GetValue()), self.divineShield5.GetValue(), self.spDamage5.GetValue()),
                   6: (int(self.b6.GetValue()), self.divineShield6.GetValue(), self.spDamage6.GetValue()),
                   7: (int(self.b7.GetValue()), self.divineShield7.GetValue(), self.spDamage7.GetValue()),
                   8: (int(self.eb1.GetValue()), self.endivineShield1.GetValue(), False),
                   9: (int(self.eb2.GetValue()), self.endivineShield2.GetValue(), False),
                   10: (int(self.eb3.GetValue()), self.endivineShield3.GetValue(), False),
                   11: (int(self.eb4.GetValue()), self.endivineShield4.GetValue(), False),
                   12: (int(self.eb5.GetValue()), self.endivineShield5.GetValue(), False),
                   13: (int(self.eb6.GetValue()), self.endivineShield6.GetValue(), False),
                   14: (int(self.eb7.GetValue()), self.endivineShield7.GetValue(), False)
                   }
        print(minions)
        minionhps = []
        miniondivines = []
        minionspell = []
        for x in minions:
            minionhps.append(minions[x][0])
            miniondivines.append(minions[x][1])
            minionspell.append(minions[x][2])
        print(minionhps)
        print(miniondivines)
        
        reCast = True
        while(reCast):

            extraSpellDamage = minionspell.count(True)
            reCast = False
            for x in range(0, 14):
                if(miniondivines[x] == True):
                    if(x == 0):
                        self.divineShield1.SetValue(False)
                        miniondivines[x] = False
                    if(x == 1):
                        self.divineShield2.SetValue(False)
                        miniondivines[x] = False
                    if(x == 2):
                        self.divineShield3.SetValue(False)
                        miniondivines[x] == False
                    if(x == 3):
                        self.divineShield4.SetValue(False)
                        miniondivines[x] = False
                    if(x == 4):
                        self.divineShield5.SetValue(False)
                        miniondivines[x] = False
                    if(x == 5):
                        self.divineShield6.SetValue(False)
                        miniondivines[x] = False
                    if(x == 6):
                        self.divineShield7.SetValue(False)
                        miniondivines[x] = False
                    if(x == 7):
                        self.endivineShield1.SetValue(False)
                        miniondivines[x] = False
                    if(x == 8):
                        self.endivineShield2.SetValue(False)
                        miniondivines[x] = False
                    if(x == 9):
                        self.endivineShield3.SetValue(False)
                        miniondivines[x] = False
                    if(x == 10):
                        self.endivineShield4.SetValue(False)
                        miniondivines[x] = False
                    if(x == 11):
                        self.endivineShield5.SetValue(False)
                        miniondivines[x] = False
                    if(x == 12):
                        self.endivineShield6.SetValue(False)
                        miniondivines[x] = False
                    if(x == 13):
                        self.endivineShield7.SetValue(False)
                        miniondivines[x] = False                    
                else:
                    if(minionhps[x] < 0):
                        minionhps[x] = 0
                    if(minionhps[x] > 0):                        
                        print(minionspell.count(True))
                        minionhps[x] = minionhps[x] - 1 - extraSpellDamage
                        if(minionhps[x] < 0):
                            minionhps[x] = 0
                        if(minionhps[x] <= 0):
                            reCast = True
                            if(x == 0):
                                self.spDamage1.SetValue(False)
                                minionspell[x] = False
                            if(x == 1):
                                self.spDamage2.SetValue(False)
                                minionspell[x] = False
                            if(x == 2):
                                self.spDamage3.SetValue(False)
                                minionspell[x] = False
                            if(x == 3):
                                self.spDamage4.SetValue(False)
                                minionspell[x] = False
                            if(x == 4):
                                self.spDamage5.SetValue(False)
                                minionspell[x] = False
                            if(x == 5):
                                self.spDamage6.SetValue(False)
                                minionspell[x] = False
                            if(x == 6):
                                self.spDamage7.SetValue(False)
                                minionspell[x] = False
                            
        self.b1.SetValue(str(minionhps[0]))
        self.b2.SetValue(str(minionhps[1]))
        self.b3.SetValue(str(minionhps[2]))
        self.b4.SetValue(str(minionhps[3]))
        self.b5.SetValue(str(minionhps[4]))
        self.b6.SetValue(str(minionhps[5]))
        self.b7.SetValue(str(minionhps[6]))
        self.eb1.SetValue(str(minionhps[7]))
        self.eb2.SetValue(str(minionhps[8]))
        self.eb3.SetValue(str(minionhps[9]))
        self.eb4.SetValue(str(minionhps[10]))
        self.eb5.SetValue(str(minionhps[11]))
        self.eb6.SetValue(str(minionhps[12]))
        self.eb7.SetValue(str(minionhps[13]))

        
        print(minionhps)
        print(miniondivines)
        
    def toggleCheckBox(cb):
        evt = wx.CommandEvent(commandType=wx.EVT_CHECKBOX.typeId)
        evt.SetEventObject(cb)
        cb.SetValue( not cb.GetValue())
        wx.PostEvent(cb, evt)

    def check_int(self, event):
        keypress = event.GetKeyCode()
        print(keypress)
        if (((keypress >=48) and (keypress <= 57)) or (keypress == 8)):
                event.Skip()



        
if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='ezDefile')
    frm.Show()
    app.MainLoop()
