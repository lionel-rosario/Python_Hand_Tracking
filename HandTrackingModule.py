import cv2
import mediapipe as mp
import time




class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.MaxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.MaxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        lmList = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(frame, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

                # ✅ Correct way to access landmarks
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)  # Convert to pixel coordinates
                    lmList.append((id, cx, cy))

        return frame, lmList  # Return landmarks list


# Main function
def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()

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


if __name__ == "__main__":
    main()
