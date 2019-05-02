from flask import Flask, render_template, Response
from camera import VideoCamera, Pos
import flask_cors
import pdb, json, sys, traceback
app = Flask(__name__)
flask_cors.CORS(app)
cam = VideoCamera()

def make_resp(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    return 'hello'

@app.route('/feed')
def video_feed():
    #cam = VideoCamera()
    return Response(make_resp(cam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/faces')
def faces():
    try:
        return (json.dumps(cam.f))
    except Exception as e:
        print(traceback.format_exc())
        return ''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True, threaded=True)