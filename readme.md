# AttendAI -- AI-Based Attendance Management System

AttendAI is an AI-powered attendance management system built with
**Streamlit**, **Supabase**, **Facial Recognition**, and **Voice
Recognition**. The system enables teachers to manage subjects, enroll
students, register face and voice profiles for AI-powered attendance verification., and mark attendance automatically
using AI.

> **Live Demo:** https://attendai-app.streamlit.app/ 

> **GitHub Repository:** https://github.com/dhruvlearner-05/AI-Based-Attendance-Management-System

## Features

### Teacher Portal

-   Teacher registration and login
-   Create and manage subjects
-   Enroll students into subjects
-   Share subject enrollment codes
-   View attendance results

### Student Portal

-   Student registration and login
-   Facial profile registration
-   Voice profile registration
-   Join subjects using enrollment code

### AI Attendance

-   Face recognition for student identification
-   Voice recognition for classroom attendance
-   Automatic attendance logging
-   Attendance summary with present/absent status

## Tech Stack

-   **Frontend:** Streamlit
-   **Database & Authentication:** Supabase
-   **Machine Learning:** Scikit-learn (SVM)
-   **Face Recognition:** dlib, face_recognition_models
-   **Voice Recognition:** Resemblyzer, Librosa
-   **Security:** bcrypt
-   **Language:** Python

## Project Structure

``` text
AttendAI/
├── src/
│   ├── assets/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
├── app.py
├── requirements.txt
└── .gitignore
```

## Installation

1.  Clone the repository:

``` bash
git clone https://github.com/dhruvlearner-05/AI-Based-Attendance-Management-System.git
cd AI-Based-Attendance-Management-System
```

2.  Create a virtual environment:

``` bash
python -m venv venv
```

3.  Activate it:

Windows:

``` bash
venv\Scripts\activate
```

Linux/macOS:

``` bash
source venv/bin/activate
```

4.  Install dependencies:

``` bash
pip install -r requirements.txt
```

5.  Configure Streamlit secrets (`.streamlit/secrets.toml`):

``` toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
```

6.  Run the application:

``` bash
streamlit run app.py
```
# 👨‍💻 Author

**Dhruv Jain**



