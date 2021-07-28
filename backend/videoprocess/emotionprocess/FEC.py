import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import img_to_array

def FER (video, face_cascade, emotion_classifier):

    emotionResults = np.array([0,0,0,0,0,0,0])

    total_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
    curr_frame=0

    while curr_frame < total_frame :
        curr_frame += 1

        fps = round(video.get(cv2.CAP_PROP_FPS))
        if curr_frame % fps == 0 : ##

          ret, frame = video.read()
          if ret != True :
            break

          grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

          faces = face_cascade.detectMultiScale(grayimg, scaleFactor= 1.1, minNeighbors=5, minSize=(20,20))

          if len(faces) > 0 :
            face = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = face

            target = grayimg[fY: fY+fH, fX:fX+fW]
            target = cv2.resize(target, (64,64))
            target = target.astype("float") / 255.0
            target = img_to_array(target)
            target = np.expand_dims(target, axis=0)

            predictions = emotion_classifier.predict(target)[0]
            emotionResults[predictions.argmax()] += 1

    results = [0,0,0]

    for i in range(3):
        label = emotionResults.argmax()
        results[i] = label
        emotionResults[label] = 0
    return results

