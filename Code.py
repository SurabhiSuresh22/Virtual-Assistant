# modules to collect information from network
import wx
import wikipedia
import wolframalpha

# module for recongnizing your command
import speech_recognition as sr

class MyFrame(wx.Frame):

    #initialising virtual assistant display - GUI
    def __init__(self):
        
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition,size=wx.Size(450,100),
                          style=wx.MINIMIZE_BOX |wx.SYSTEM_MENU |wx.CAPTION |
                          wx.CLOSE_BOX |wx.CLIP_CHILDREN ,title="PyDa")
        
        panel =wx.Panel(self)
        
        my_sizer =wx.BoxSizer(wx.VERTICAL)
        
        lbl=wx.StaticText(panel,
        label="Hello I am PyDa the python Digital Assistant.How can I help you?")   # Text display on GUI
        
        my_sizer.Add(lbl,0,wx.ALL,5)
        
        self.txt = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        
        my_sizer.Add(self.txt ,0 ,wx.ALL,5)
        panel.SetSizer(my_sizer)
        
        self.Show()

    # taking input and displaying information
    def OnEnter(self,event):
        inp= self.txt.GetValue()
        inp=inp.lower()

        # try taking in your voice command as input 
        if inp == '':
            r =sr.Recognizer()

            with sr.Microphone() as source:
                audio=r.listen(source)  # listening to audio
                
            # using google speech recognition
            try:
                self.txt.SetValue(r.recognize_google(audio))                  #recognizing audio
            except sr.UnknownValueError:
                print('Google Speech Recognition could not understand audio') #displayed when unable to identify audio
            except sr.RequestError as e:
                print('Could not request results; {0} '.format(e))
                
        #if no audio input then check for text input
        
        else:
            #finds result using wolframalpha
            try:
                
               #wolframlapha
                app_id="-----Your app id here -----"
                client=wolframalpha.Client(app_id)

                res=client.query(inp)
                answer=next(res.results).text
                
                print(answer)   #display results
                
            #finds result using wikipedia   
            except:
                #wikipedia
                inp = inp.split(' ')
                inp=' '.join(inp[2:])
                print(wikipedia.summary(inp))  #display results on another window



if __name__=='__main__':
    app=wx.App(True)
    frame=MyFrame()
    app.MainLoop()
               

