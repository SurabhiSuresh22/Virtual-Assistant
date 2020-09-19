import wx
import wikipedia
import wolframalpha


class MyFrame(wx.Frame):
    
    def __init__(self):
        
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition,size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX |wx.SYSTEM_MENU |wx.CAPTION |
                          wx.CLOSE_BOX |wx.CLIP_CHILDREN ,title="PyDa")
        
        panel =wx.Panel(self)
        
        my_sizer =wx.BoxSizer(wx.VERTICAL)
        
        lbl=wx.StaticText(panel,
        label="Hello I am PyDa the python Digital Assistant.How can I help you?")
        
        my_sizer.Add(lbl,0,wx.ALL,5)
        
        self.txt = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        
        my_sizer.Add(self.txt ,0 ,wx.ALL,5)
        panel.SetSizer(my_sizer)
        
        self.Show()

    def OnEnter(self,event):
        inp= self.txt.GetValue()
        inp=inp.lower()
        
        
        try:
        #wolframlapha
            app_id= "---Put you id here---"
            client=wolframalpha.Client(app_id)

            res=client.query(inp)
            answer=next(res.results).text

            print(answer)
            
            
        except:
            #wikipedia
            inp = inp.split(' ')
            inp=' '.join(inp[2:])

            
            print(wikipedia.summary(inp))



if __name__=='__main__':
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
               
