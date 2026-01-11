Person Matching Using YOLO and Face Recognition

This script implements a person detection and face-matching system by combining YOLO object detection with face recognition techniques.

First, a reference image (image2.jpg) is loaded and processed using the face_recognition library to extract a facial encoding. This encoding acts as a biometric identity of the target person. If no face is detected in the reference image, the program safely exits.

Next, a pre-trained YOLO model (yolov5s.pt) is used to detect persons in a given video (video3.mp4). YOLO efficiently locates all human figures in each video frame by drawing bounding boxes around detected persons.

For every detected person:

The person’s region is cropped from the frame.

The cropped image is converted to RGB format.

Facial encodings are extracted from the cropped region.

If a face is found, it is compared with the reference face encoding.

If the similarity is within a defined tolerance, the person is labeled “MATCHED”; otherwise, “Unknown”.

If no face is detected in the crop, the label “Person detected” is displayed.

The system visually displays the results in real time by:

Drawing bounding boxes around detected persons

Showing identification labels with different colors:

🟢 Green → Matched person

🔴 Red → Unknown person

🟡 Yellow → Person detected but face not visible

This approach is useful for identity verification, surveillance, access control, and person re-identification tasks, where a specific individual needs to be tracked or recognized within video footage.

🎯 Key Technologies Used

YOLO (You Only Look Once) for real-time person detection

face_recognition (dlib-based) for facial feature extraction and comparison

OpenCV for video processing and visualization
<img width="468" height="853" alt="image" src="https://github.com/user-attachments/assets/abcc8ecc-5859-4dce-8d2b-8ab0ab86b202" />
