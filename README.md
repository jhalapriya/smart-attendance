# 🎓 Smart Attendance System
### AI-powered face recognition attendance — no registers, no proxies, no manual entry.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)

---

## 📌 Overview

**Smart Attendance System** is an AI-based attendance solution that automatically detects and recognizes student faces using a webcam and marks attendance — without any manual entry.

Instead of calling names or signing registers, the camera scans faces in real time and records attendance directly into a database. Built with Python, OpenCV, and the `face_recognition` library.

---

## 🚀 Features

- 📷 **Live face detection** using OpenCV
- 🧠 **AI face recognition** with 95%+ confidence scoring
- ✅ **Auto attendance marking** — name, date, and time saved instantly
- 🚫 **Duplicate prevention** — one entry per student per day
- 🗄️ **SQLite database** for structured storage
- 📊 **CSV export** for daily/weekly/monthly reports
- 👤 **Unknown face detection** — flags unregistered faces
- 🖥️ **Admin dashboard** (coming in Phase 3)

---

## 🏗️ System Architecture

```
Student Face
     ↓
  Webcam
     ↓
Face Detection (OpenCV)
     ↓
Face Recognition (face_recognition library)
     ↓
Match with Student Database
     ↓
Attendance Marked (SQLite + CSV)
     ↓
Report Generated
```

---

## 📁 Project Structure

```
smart-attendance/
│
├── attendance/
│   └── attendance.csv          # Daily attendance records
│
├── database/
│   ├── attendance.db           # SQLite database
│   └── students.csv            # Registered students
│
├── dataset/
│   └── student_images/         # Face image dataset per student
│       └── 101_Rahul/
│           ├── 101_Rahul_1.jpg
│           └── ...
│
├── models/
│   └── face_model.pkl          # Trained face recognition model
│
├── utils/                      # Utility/helper scripts
│
├── capture_faces.py            # Capture 50 face images via webcam
├── database_setup.py           # Create SQLite tables
├── main.py                     # Entry point
├── mark_attendance.py          # Live recognition + attendance marking
├── register_student.py         # Student registration module
├── train_model.py              # Train face recognition model
├── requirements.txt            # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/jhalapriya/smart-attendance.git
cd smart-attendance
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
py -m pip install opencv-python
py -m pip install face-recognition
py -m pip install numpy
py -m pip install pandas
py -m pip install pillow
py -m pip install cmake
py -m pip install dlib
```

Or install all at once:
```bash
pip install -r requirements.txt
```

---

## 🧪 How to Use

### Step 1 — Set up the database
```bash
py -3.11 database_setup.py
```

### Step 2 — Register a student
```bash
py -3.11 register_student.py
```
Enter student ID and name. A folder is automatically created in `dataset/student_images/`.

### Step 3 — Capture face images
```bash
py -3.11 capture_faces.py
```
Stand in front of the webcam. The system captures 50 images automatically.

### Step 4 — Train the model
```bash
py -3.11 train_model.py
```
Reads all saved face images, extracts AI encodings, and saves `models/face_model.pkl`.

### Step 5 — Start live attendance
```bash
py -3.11 mark_attendance.py
```
Webcam opens → face detected → name and confidence shown → attendance saved automatically.

Press `Q` to quit.

---

## 📋 Sample Attendance Output

```
student_name, date,       time
Rahul,        04-06-2026, 10:15:32
Akshay,       04-06-2026, 10:17:08
Anmol,        04-06-2026, 10:18:45
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11+ |
| Face Detection | OpenCV (Haar Cascade / DNN) |
| Face Recognition | `face_recognition` + `dlib` |
| Database | SQLite → MySQL (Phase 2) |
| Reports | Pandas + CSV |
| GUI | Tkinter (Phase 3) |
| Web Dashboard | Flask (Phase 3) |

---

## 🗺️ Development Roadmap

- [x] **Phase 1** — Core system (registration, capture, training, live recognition, SQLite, CSV)
- [ ] **Phase 2** — CCTV / IP camera support, RTSP stream, multi-camera, unknown face alerts
- [ ] **Phase 3** — Admin dashboard, teacher panel, student analytics, cloud database, deployment

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Priya Jhala**
GitHub: [@jhalapriya](https://github.com/jhalapriya)

---

> Built as an AI/ML project to solve real-world attendance problems using computer vision.