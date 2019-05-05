

import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, image = capture.read()
    cv2.imshow("she xiang tou", image)
    if cv2.waitKey(5) & 0xFF == ord("1"):
        break
capture.release()
cv2.destroyAllWindows()
