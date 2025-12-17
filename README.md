# Gesture Controlled 3D Cube 🎮✋

This project demonstrates a real-time hand gesture controlled 3D cube using computer vision.
The orientation of a 3D cube is controlled using hand movements captured through a webcam.
The cube rotates along X, Y, and Z axes based on the position and gestures of the hand,
providing an intuitive and touchless way to interact with 3D objects.

---

## 🔥 Features
- Real-time hand tracking using MediaPipe
- 3D cube rendered using OpenGL
- Rotation control on X, Y, and Z axes
- Each face of the cube has a different color
- Touchless and interactive 3D visualization
- Smooth and intuitive gesture-based control

---

## 🛠️ Technologies Used
- Python 3.12
- OpenCV
- MediaPipe
- Pygame
- PyOpenGL
- NumPy

---

## 📂 Project Structure
gesture-3d-cube/
│
├── gesture_3d_control.py
├── requirements.txt
├── README.md
└── .gitignore

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install required dependencies
pip install -r requirements.txt

4️⃣ Run the application
python gesture_3d_control.py

✋ Gesture Controls
Hand Gesture	Action
Move hand left / right	Rotate cube along Y-axis
Move hand up / down	Rotate cube along X-axis
Thumb–index distance	Rotate cube along Z-axis
Stop hand movement	Cube rotation stops
🧠 Working Principle

MediaPipe is used to detect 21 hand landmarks in real time.
The palm center coordinates control rotation along X and Y axes,
while the distance between thumb and index finger controls rotation along the Z axis.
OpenGL renders a colored 3D cube whose orientation updates according to these gestures.

🎯 Applications

Human–Computer Interaction (HCI)

Virtual reality and 3D visualization

Gesture-based interfaces

Educational demonstrations of computer vision

👨‍💻 Author

Anshuman Bhardwaj

⭐ Acknowledgements

MediaPipe by Google

OpenCV Community

PyOpenGL Documentation
