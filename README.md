`pip install flask flask-cors opencv-python --user`

`python app.py`

If it gets stuck at `Restarting with stat` (doesn't generate a debugger pin):

 * comment out line 7 in app
 * `python app.py`
 * uncomment line 7 and save
 * server will restart

(For some reason opening the camera stream makes it hang?)

Open index.html (tested in firefox)