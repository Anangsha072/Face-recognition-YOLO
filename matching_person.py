from ultralytics import YOLO
import face_recognition
import cv2
ref_img = face_recognition.load_image_file("image2.jpg")
ref_encs = face_recognition.face_encodings(ref_img)
if not ref_encs:
    print("No face found in reference image!")
    exit()
ref_encoding = ref_encs[0]
model = YOLO("yolov5s.pt")  
cap = cv2.VideoCapture("video3.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)[0]
    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id != 0:
            continue  # Only process 'person' class
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        person_crop = frame[y1:y2, x1:x2]
        rgb_crop = cv2.cvtColor(person_crop, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_crop)
        if not encodings:
            label = "Person detected"
            color = (255, 255, 0)  # Yellow for no face
        else:
            match = face_recognition.compare_faces([ref_encoding], encodings[0], tolerance=0.5)
            label = "MATCHED" if match[0] else "Unknown"
            color = (0, 255, 0) if match[0] else (0, 0, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Person Detection + Face Match", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
















