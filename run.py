import sys
import os
import face_recognition.api as face_recognition
import sys
import pickle
import imutils
import numpy as np
import cv2
import math
from  config import get_list
from urllib.request import urlopen


# print(len(KNOWN_FACE_ENCODINGS))

def load_pickle(file_path):
    with open(file_path, 'rb') as handle:
        data = pickle.load(handle)
        return data

def compare_face(unknown_face_encodings):
    KNOWN_FACE_ENCODINGS,KNOWN_NAMES = get_list()
    # print(len(KNOWN_FACE_ENCODINGS))
    for i,each_known_face in enumerate(KNOWN_FACE_ENCODINGS):
        # results = face_recognition.compare_faces(each_known_face, unknown_face_encodings,tolerance=0.4)
        encodings_distance = np.linalg.norm(each_known_face - unknown_face_encodings)
        score = (1 - math.pow(encodings_distance, 2) / 2) * 100
        if score > 90:
            return KNOWN_NAMES[i]
        elif 90 > score > 85:
            return "look alike "+KNOWN_NAMES[i]
        else:
            continue
    return "UnKnown"

def main():
    # starting video streaming
    # cv2.namedWindow('Live Face Feed')
    # url = 'http://192.168.3.84:8080/shot.jpg'
    camera = cv2.VideoCapture(0)
    # camera.set(cv2.CAP_PROP_FPS, 2)
  

    while True:

        # camera = urlopen(url)
        # vidImg = np.array(bytearray(camera.read()), dtype=np.uint8)
        # frame = cv2.imdecode(vidImg, -1)
        # frame = imutils.resize(frame, width=600)

        frame = camera.read()[1]
        #reading the frame
        print(frame)
        frame = imutils.resize(frame,width=600)

        frameClone = frame.copy()
        # img = face_recognition.load_image_file(frame)
        faces = face_recognition.face_locations(frame)
        unknown_face_encodings = face_recognition.face_encodings(frame)
        if len(faces) > 0:
            for i,each_face in enumerate(unknown_face_encodings):
                result = compare_face(each_face)
                # (fX, fY, fW, fH) = faces[i]
                (fY1, fX2, fY2, fX1) = faces[i]
                cv2.putText(frameClone, result, (fX1, fY1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX1,fY1), (fX2 ,fY2),
                            (0, 0, 255), 2)
        else: 
            # continue
            cv2.putText(frameClone, "No Faces Found", (10, 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255), 2)


        cv2.imshow('your_face', frameClone)
        # cv2.imshow("Probabilities", canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # path_to_pickle = "./database/features/features.pickle"
    # data = load_pickle(path_to_pickle)
    # known_face_encodings = list(data.values())
    # known_names = list(data.keys())
    main()
