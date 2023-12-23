import cv2

#Take in video live from webcam
cap = cv2.VideoCapture(0)
#check that camera can be used
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True: #Keep running forever
    #Read in a frame
    ret, frame = cap.read()
    #If frame is not read properly, stop
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    ######
    #placeholder functions
    cv2.putText(frame,'testing',(10,100), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow('output', frame)
    ######

    #Stop if any key is pressed
    keyCode = cv2.waitKey(10)
    print(keyCode)
    if keyCode != -1:
        break


cap.release()
cv2.destroyAllWindows()