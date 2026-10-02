import cv2, os, time

os.makedirs("images_raw", exist_ok=True)
cap = cv2.VideoCapture(0)
n = 0

while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("collect", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        n += 1
        path = f"images_raw/{int(time.time()*1000)}_{n:03d}.jpg"
        cv2.imwrite(path, frame)
        print("saved", path)
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
