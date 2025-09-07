# Final_Major_Project

## Title
**AI-Powered Real-Time Weapon Detection System Using Deep Learning and YOLOv8**

---

## Description
This project implements a real-time weapon detection system using **YOLOv8**, designed to enhance public safety in areas such as schools, colleges. By leveraging **deep learning** and AI, the system can automatically detect weapons like **guns, knives, scissors, and syringes** from live video feeds, reducing human monitoring workload and response time.

---

## Project Overview
Traditional surveillance systems rely on human operators to monitor live feeds, which is error-prone and slow. This system automates weapon detection using **YOLOv8**, providing fast, accurate, and scalable detection. The system supports **live webcam/CCTV integration** and real-time alerts, helping authorities respond promptly to potential threats.

---

## Features
- Real-time detection of weapons from live video
- Supports detection of multiple weapon types (guns, knives, scissors, syringes)
- Integration with webcam or CCTV
- Highlight detected weapons in video feed
- Instant alert mechanism for detected threats
- Scalable for large environments

---

## Technology Used
- **Python 3.x**
- **YOLOv8 (Ultralytics)**
- **OpenCV** for video processing
- **NumPy**
- **Streamlit** (optional GUI)
- **PyInstaller** (for EXE creation)

---

## System Architecture
[Camera / CCTV Feed] --> [YOLOv8 Detection Model] --> [Processing & Alerts] --> [Display / Notification]

- **Input:** Live video from webcam or CCTV  
- **Processing:** YOLOv8 detects weapons in real time  
- **Output:** Video feed with bounding boxes, alert notifications

---

## Hardware Requirements
- CPU: Intel i5 or higher   
- GPU: NVIDIA GPU with CUDA (optional for faster inference)  
- RAM: Minimum 8GB  
- Storage: 10GB for datasets, weights, and project files  
- Camera: Webcam or CCTV for live feed  

---

## Model and Metrics
- **Model:** YOLOv8 (Ultralytics) pretrained with custom dataset for weapons  
- **Classes:** Gun, Knife, Scissors, Syringe  
- **Metrics:**  
  - **Precision**: Accuracy of correct detections  
  - **Recall**: Detection coverage of all weapons  
  - **mAP50**: Mean Average Precision at IoU 0.5  
  - **Inference Speed:** FPS for real-time performance

---

## Key Elements
- **Weapon Detection Model:** YOLOv8 trained on weapon dataset  
- **Real-Time Video Feed:** Webcam/CCTV integration  
- **Alert System:** Visual indication on detected weapons  
- **Data Processing:** Efficient handling of frames for real-time inference  

---

## Project Structure
weapon-detection/
│
├── app.py # Main application
├── weights/
│ └── best.pt # Trained YOLOv8 weights
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── data/ # Dataset folder (if applicable)
├── utils/ # Utility scripts
└── dist/ # EXE output folder after PyInstaller


---

## Results
- Real-time detection of weapons in live video feed  
- Bounding boxes highlight detected weapons  
- Alerts triggered immediately upon detection  
- FPS suitable for real-time application  

---

## Troubleshooting
- **PyInstaller EXE issues:** Use `--add-data "weights/best.pt;weights"` to include model weights  
- **Missing dependencies:** Ensure `pip install -r requirements.txt` is completed  
- **Camera not detected:** Check webcam drivers and permissions  
- **Slow detection:** Consider using a GPU-enabled environment or lower resolution video  

---

## Acknowledgements
- **Ultralytics YOLOv8** for object detection  
- **OpenCV** for image and video processing  
- Inspiration from research papers on **AI-based weapon detection**  
- Open-source community for Python deep learning resources  


