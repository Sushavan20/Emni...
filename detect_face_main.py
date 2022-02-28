import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

# To use a video file as input 
# cap = cv2.VideoCapture('VID20200211094726.mp4')


while True:
    # Read the frame
    ret, frame = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (225, 0, 225), 2)
        cv2.putText(frame,"Face Found!",(200,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    if faces is():
        cv2.putText(frame,"Face Not Found!",(200,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    # Display
    cv2.imshow('Image', frame)


    # Stop if escape key is pressed
    if cv2.waitKey(1)==13:
        break

        
# Release the VideoCapture object
cap.release()


