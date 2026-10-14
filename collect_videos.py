
import cv2
from pathlib import Path

gesture = input("Название жеста: ")
folder = Path("data/raw_videos") / gesture
folder.mkdir(parents=True, exist_ok=True)

camera = cv2.VideoCapture(0)
video_number = len(list(folder.glob("*.avi"))) + 1

print("Нажми R для записи, Q для выхода")

while True:
    ok, frame = camera.read()
    if not ok:
        break

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if key == ord("r"):
        filename = folder / f"{video_number}.avi"
        writer = cv2.VideoWriter(
            str(filename),
            cv2.VideoWriter_fourcc(*"MJPG"),
            20,
            (frame.shape[1], frame.shape[0])
        )

        for _ in range(60):
            ok, frame = camera.read()
            if not ok:
                break
            writer.write(frame)
            cv2.imshow("Camera", frame)
            cv2.waitKey(1)

        writer.release()
        print("Видео сохранено:", filename)
        video_number += 1

camera.release()
cv2.destroyAllWindows()
