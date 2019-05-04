`pip install flask flask-cors numpy opencv-python --user`

`python app.py`

If it gets stuck at `Restarting with stat` (doesn't generate a debugger pin):

 * comment out line 40 in app
 * `python app.py`
 * uncomment line 40 and save
 * server will restart

(For some reason opening the camera stream makes it hang?)

Arduino:

 * 2 x 9g servo
 * wemos D1 mini
 * x axis to D4
 * y axis to D3

change the url to the assigned one in script.js

Open index.html (tested in firefox)