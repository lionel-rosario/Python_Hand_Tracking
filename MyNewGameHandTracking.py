import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame, lmList = detector.findHands(frame)

    if lmList:
        print("Landmark 4:", lmList[4])  # Print the 5th landmark (index 4)
    else:
        print("No hand detected")

    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()