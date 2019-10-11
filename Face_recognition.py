
## FACE RECOGNITION DEMO USING FACE RECOGNITION API in Python

import face_recognition
import cv2
import numpy as np


video_capture = cv2.VideoCapture(0)

# Loading  sample pictures and make it learn how to recognize them
manoj_image = face_recognition.load_image_file("Manoj.jpg")
manoj_face_encoding = face_recognition.face_encodings(manoj_image)[0]

srinivas_image = face_recognition.load_image_file("Srinivas.jpg")
srinivas_face_encoding = face_recognition.face_encodings(srinivas_image)[0]

malle_image = face_recognition.load_image_file("Malle.jpg")
malle_face_encoding = face_recognition.face_encodings(malle_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    manoj_face_encoding,
    srinivas_face_encoding,
    malle_face_encoding
    
]

known_face_names = [
    "MANOJ",
    "SRINIVAS",
    "DEV"
]

# Initializing the variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Converting the image from BGR color  to RGB color.This is because the face recognition API is compatible with RGB.
    rgb_small_frame = small_frame[:, :, ::-1]



    if process_this_frame:
        
        # Finding all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            # See if the face is a match for the known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # To Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # To Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the modified image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()