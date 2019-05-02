import cv2, json

class Pos:
    x, y, w, h = 0, 0, 0, 0
    def set(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        return self
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class VideoCamera(object):
    f = []

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        faceCascade = cv2.CascadeClassifier('cascade.xml')

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, flipCode=1)
        image = cv2.flip(image, flipCode=1)

        faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5,
		    minSize=(30, 30)
		)

        self.f = []
		
        for (x, y, w, h) in faces:
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.f.append('{"x":'+str(x)+',"y":'+str(y)+',"w":'+str(w)+',"h":'+str(h)+'}')

        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()