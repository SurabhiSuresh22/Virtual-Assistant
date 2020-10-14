# Virtual-Assistant
This is basically a virtual assistant built using python.
   
Wx ,wolframalpha and wikipedia modules are used here.<br>
Google speech recongition tool is used for voice commands
   

wx is a cross platform GUI for python.<br>
Wikipedia and wolframalpha modules are downloaded , installed and imported python modules.<br>
You need to install PyAudio for running speech recongnition on windows 10

Use this code :<br>

For wx-

        Win and Mac     -     pip install -U wxPython  ,
        Ubuntu      -     sudo apt-get install python-wxgtk2.8
<br><br> 
Wikipedia module - To get search results of almost everything.
         win     -      pip install wikipedia
<br><br>  
wolframalpha - To create an app .You have to sign in to wolframapha , create an app , you get an Id , you use it here.<br>
               pip install wolframaplha
<br><br>
PyAudio -  pip install pipwin <br>
           Then run this : pipwin install pyaudio      
<br><br>
You get a pop up window like this : (the window on top)
This is your GUI of virtual assistant. Below is the windows that pops up displaying your search results .<br><br>
![GUI](https://github.com/Surbi-22/Virtual-Assistant/blob/master/window.png)
<br><br>
If google fails to recognize your audio , then pop up window will show "Google was unable to recongize your input" - This is your given code.
