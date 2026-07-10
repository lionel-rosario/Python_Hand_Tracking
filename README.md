# ✋ Python Hand Tracking

A real-time hand tracking application built with **Python**, **OpenCV**, and **MediaPipe**. This project detects hands from a webcam feed, tracks hand landmarks, and displays them in real time with high accuracy and low latency.

## 📌 Features

* 🎥 Real-time hand detection using a webcam
* ✋ Detects one or multiple hands
* 📍 Tracks 21 hand landmarks for each detected hand
* 📐 Draws hand connections and landmark points
* ⚡ Fast and lightweight implementation
* 🧩 Easy to integrate into gesture recognition and computer vision projects

## 🛠️ Technologies Used

* Python 3.x
* OpenCV
* MediaPipe

## 📂 Project Structure

```text
Python_Hand_Tracking/
│
├── HandTrackingModule.py    # Hand tracking helper module
├── main.py                  # Main application
├── requirements.txt         # Project dependencies
├── README.md
└── assets/                  # Screenshots or demo GIFs (optional)
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/lionel-rosario/Python_Hand_Tracking.git
cd Python_Hand_Tracking
```

### 2. Create a virtual environment (optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the required packages manually:

```bash
pip install opencv-python mediapipe
```

## ▶️ Usage

Run the application:

```bash
python main.py
```

Press **Q** to quit the application.

## 📸 Demo

Add screenshots or an animated GIF here.

Example:

```
assets/demo.gif
assets/screenshot.png
```

## 🔍 How It Works

1. Captures video frames from the webcam.
2. Converts each frame from BGR to RGB.
3. Uses MediaPipe Hands to detect hands.
4. Extracts the 21 landmark points for each detected hand.
5. Draws landmarks and connections on the video feed.
6. Displays the processed frame in real time.

## 📦 Requirements

* Python 3.8+
* OpenCV
* MediaPipe

## 💡 Future Improvements

* Hand gesture recognition
* Finger counting
* Virtual mouse control
* Virtual keyboard
* Volume control using hand gestures
* Sign language recognition
* Hand tracking for games and AR applications

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it for learning and personal projects.

## 👨‍💻 Author

**Lionel Rosario**

GitHub: https://github.com/lionel-rosario
