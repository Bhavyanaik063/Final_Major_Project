import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
import winsound
import os

# Load your trained model
MODEL_PATH = r"C:\Users\Bhavya\OneDrive\Desktop\bhummm\Weapons-and-Knives-Detector-with-YOLOv8\runs\detect\Db\weights\best.pt"
model = YOLO(MODEL_PATH)

st.title("🔫 Weapon Detection System (YOLOv8)")
st.write("Detect **Gun** and **Knife** from Webcam, Images, or Videos.")

option = st.sidebar.radio("Choose Mode", ["Webcam", "Image", "Video"])

# Function to check and alert
def alert_if_weapon_detected(label):
    if label.lower() in ["gun", "knife"]:
        st.warning(f"⚠️ {label.upper()} Detected!")
        winsound.Beep(1000, 300)

# ------------------ Webcam Detection ------------------
if option == "Webcam":
    st.subheader("📷 Webcam Detection")
    run = st.checkbox("Start Webcam")

    cap = None
    if run:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while run:
            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Could not access webcam.")
                break

            results = model(frame)

            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    label = model.names[cls]

                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                    # 🔔 Unified alert function
                    alert_if_weapon_detected(label)

            stframe.image(frame, channels="BGR")

        if cap:
            cap.release()

# ------------------ Image Detection ------------------
elif option == "Image":
    st.subheader("🖼️ Image Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        file_bytes = uploaded_file.read()
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tmp.write(file_bytes)
        tmp.close()

        results = model(tmp.name)
        img = results[0].plot()

        # 🔍 Check detections
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]
                alert_if_weapon_detected(label)

        st.image(img, caption="Detection Result", use_column_width=True)
        os.remove(tmp.name)

# ------------------ Video Detection ------------------
elif option == "Video":
    st.subheader("🎥 Video Detection")
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)

            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    label = model.names[cls]

                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                    # 🔔 Alert
                    alert_if_weapon_detected(label)

            stframe.image(frame, channels="BGR")

        cap.release()
        os.remove(tfile.name)
