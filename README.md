# 🧑‍💻 Person Matching Using YOLO and Face Recognition

# 📌 Overview

This project demonstrates a person detection and face-matching system by combining YOLO object detection with face recognition. The system detects people in a video and identifies whether any detected person matches a given reference image.

A reference face image is used to extract facial features, which are then compared with faces detected inside person bounding boxes in a video stream.

🚀 Features

Detects people in video using YOLO

Extracts facial features using face_recognition (dlib)

Matches detected faces with a reference image

Real-time bounding box visualization

Color-coded identity labels

🟢 Matched person

🔴 Unknown person

🟡 Person detected (face not visible)

🛠️ Technologies Used

Python

YOLO (Ultralytics)

face_recognition

OpenCV

NumPy

📂 Project Structure

<img width="453" height="220" alt="image" src="https://github.com/user-attachments/assets/cc9b6a87-772b-4300-ba36-c39030e58b66" />


⚙️ How It Works

A reference image is loaded and its face encoding is extracted.

YOLO detects all persons in each frame of the input video.

Each detected person is cropped from the frame.

Facial encodings are extracted from the cropped region.

The extracted face is compared with the reference face.

The person is labeled as:

MATCHED if the face matches the reference

Unknown if the face does not match

Person detected if no face is found

Results are displayed in real time with bounding boxes and labels.

▶️ How to Run

1️⃣ Install Dependencies
pip install ultralytics face_recognition opencv-python numpy

2️⃣ Place Required Files

Reference image → image2.jpg

Video file → video3.mp4

YOLO weights → yolov5s.pt

3️⃣ Run the Script
python matching_person.py


Press q to exit the video window.

🎯 Use Cases

Surveillance systems

Access control

Person re-identification

Video-based identity verification

⚠️ Limitations

Face recognition accuracy depends on lighting and face visibility

Small or blurred faces may not be detected

Matching works best with frontal face images

<img width="468" height="853" alt="image" src="https://github.com/user-attachments/assets/abcc8ecc-5859-4dce-8d2b-8ab0ab86b202" />
