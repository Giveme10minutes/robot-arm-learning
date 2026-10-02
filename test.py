import cv2

cap = cv2.VideoCapture(0)  # 0 表示默认摄像头；打不开就试 1
if not cap.isOpened():
    raise SystemExit("打不开摄像头：换索引试试，或检查系统权限")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ok, frame = cap.read()
    if not ok:
        print("读帧失败")
        break

    print(frame.shape, frame.dtype)  # 看一眼"图像"在程序里长什么样

    cv2.imshow("camera", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):  # 按 q 退出
        break
    if key == ord("s"):  # 按 s 存一张图
        cv2.imwrite("shot.jpg", frame)
        print("已保存 shot.jpg")

cap.release()


cv2.destroyAllWindows()
