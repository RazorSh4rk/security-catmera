import cv2, json, os
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.f = []
        self.people_index = 0
        self.names = ['']
        self.faces_save = []
        self.labels_save = []
        self.trained = False
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    def __del__(self):
        self.video.release()

    def get_frame(self):   
        success, image = self.video.read()
        faceCascade = cv2.CascadeClassifier('cascade.xml')
    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, flipCode=1)
        image = cv2.flip(image, flipCode=1)

        nm = ""
        if self.trained:
            nm = self.guess_face(gray, self.face_recognizer)
    
        faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.1,
    		minNeighbors=5,
    		minSize=(30, 30)
    	)

        self.f = []
    		
        for (x, y, w, h) in faces:
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.f.append(
                '{"x":'+str(x)+
                ',"y":'+str(y)+
                ',"w":'+str(w)+
                ',"h":'+str(h)+
                ',"name":"'+ nm +'"}'
            )
    
        ret, jpeg = cv2.imencode('.jpg', image)
    
        return jpeg.tobytes()

    def get_names(self):
        pass

    def train(self, name):
        self.people_index = self.people_index + 1
        self.training = True
        path = 'faces/' + str(self.people_index)
        self.names.append(name)
        
        try:
            os.mkdir(path)
        except:
            pass

        faces, labels = self.prepare_data()
        self.faces_save, self.labels_save = faces, labels
        print("Data prepared")
        print("Total faces: ", len(faces))
        print("Total labels: ", len(labels))

        self.face_recognizer.train(faces, np.array(labels))
        self.trained = True
        for i in range(0, 10):
            s, image = self.video.read()
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        
            cv2.imwrite(path + '/' + str(i) + '.jpg', image)

            print('i see ' + self.guess_face(rgb, self.face_recognizer))

    # for training
    def detect_face(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('cascade.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
        if (len(faces) == 0):
            return None, None
        (x, y, w, h) = faces[0]
        return gray[y:y+w, x:x+h], faces[0]
    
    def prepare_data(self):
        dirs = os.listdir('faces/')
        faces, labels = [], []
        for dir in dirs:
            label = int(dir)
            subdir =  'faces/' + dir
            image_names = os.listdir(subdir)
            for image in image_names:
                path = subdir + '/' + image
                im = cv2.imread(path)
                face, rect = self.detect_face(im)
                if face is not None:
                    faces.append(face)
                    labels.append(label)
        return faces, labels

    def guess_face(self, img, recognizer):
        label, confidence = recognizer.predict(img)
        return self.names[label]





