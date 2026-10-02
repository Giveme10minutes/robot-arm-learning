import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # n = nano，最小最快的一档
cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    results = model(frame, conf=0.4, verbose=False)
    r = results[0]

    for box in r.boxes:  # 每个框：类别、置信度、坐标
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        print(
            f"{model.names[cls_id]}  conf={conf:.2f}  box=({x1:.0f},{y1:.0f},{x2:.0f},{y2:.0f})"
        )

    cv2.imshow("yolo", r.plot())  # plot() 直接返回画好框的图
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
