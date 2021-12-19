import cv2
import time
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

past_t = 0

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

if __name__ == "__main__":

    while True:
        _, img = cap.read()
        result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if result.multi_hand_landmarks:
            for hlm in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hlm, mp_hands.HAND_CONNECTIONS)

        current_t = time.time()
        fps = 1 / (current_t - past_t)
        past_t = current_t

        if _:
            cv2.putText(img, 'fps' + str(int(fps)), (40, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 0), 2)
            cv2.imshow("Img", img)
            cv2.waitKey(1)
